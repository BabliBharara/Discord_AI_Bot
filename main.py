# app_id: 1427226781470949396
# public_key: a7fe5c78080883d72545abdc2033a0bb613b9bc188eae064467b207d0324a571
import discord
import os
from openai import OpenAI

file=input("enter the 1,2or3 for loading the chat:\n")
match(file):
  case "1":
    file="chat1.txt"
  case "2":
    file="chat2.txt"
  case "3":
    file="chat3.txt"
  case _:
    print("invalid input")
    exit()
with open(file, "r") as f:
  chat= f.read()

openrouter_client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("openai_key"),
)

token = os.getenv("secret")

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as{ self.user}!')

    async def on_message(self, message):
        global chat
        chat += f"{message.author}: {message.content}\n"
        print(f'Message from{message.author}: {message.content}')
        if self.user!= message.author:
            if self.user in message.mentions:
              print(chat)
              channel = message.channel
              user_message = message.content.replace(f"<@{self.user.id}>", "").strip()
              completion = openrouter_client.chat.completions.create(
                  
                  extra_body={},
                  model="openai/gpt-oss-20b:free",
                  messages=[
                    {
                      "role": "user",
                      "content":f"{chat}\nBabli's: "
                    }
                  ]
                )
              messageToSend = completion.choices[0].message.content
              for i in range(0, len(messageToSend), 2000):
               await channel.send(messageToSend[i:i + 2000])

                
        

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(token)

#Discord AI Bot

A smart and interactive **Discord bot** powered by **OpenAI** and developed using **Replit**.  
This bot can hold intelligent conversations with users inside a Discord server by using chat memory files and OpenAI’s advanced language models.

#Features

-  AI-powered chat responses using **OpenAI API**
-  Multiple conversation memory files (`chat1.txt`, `chat2.txt`, `chat3.txt`)
-  Easy setup with Replit or any Python environment
-  Environment variable support for secure API keys
-  Simple and modular Python structure

#Tech Stack

- Python 3
- Discord.py (for bot communication)
- OpenAI / OpenRouter API (for AI responses)
- Replit (for development and optional hosting)


#Project Structure
```
Discord_AI_Bot/
│
├── main.py # Main bot script
├── chat1.txt # Chat memory file 1
├── chat2.txt # Chat memory file 2
├── chat3.txt # Chat memory file 3
├── pyproject.toml # Project dependencies
├── .gitignore # Ignored files (optional)
├── generated-icon.png # Bot icon
└── README.md # Project documentation
```

#How to Run
1. **Clone the repository**
   ```bash
   git clone https://github.com/BabliBharara/Discord_AI_Bot.git
   cd Discord_AI_Bot

2.Install dependencies:
   bash
   pip install discord openai
   
3.Add your secrets:
    openai_key → Your OpenAI API key
    secret → Your Discord bot token

4.Run the bot:
  bash
  python main.py



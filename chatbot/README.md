# Chatbot

AI-powered chatbot using OpenAI's GPT-3.5 Turbo model.

## Features
- 🤖 Conversational AI using GPT-3.5 Turbo
- 💬 Maintains conversation context
- 🔄 Updated for OpenAI API v1.0+
- 🔐 Secure API key handling via environment variables

## Requirements
```bash
pip install openai
```

## Setup

1. Get your OpenAI API key from: https://platform.openai.com/api-keys

2. Set the environment variable:
```bash
export OPENAI_API_KEY='your-api-key-here'
```

Or on Windows:
```bash
set OPENAI_API_KEY=your-api-key-here
```

## Usage
```bash
python chatbot.py
```

Type your messages and the AI will respond. Type 'exit', 'quit', or 'bye' to end the conversation.

## Example
```
AI CHATBOT

You: Hello!
Chatbot: Hello! How can I help you today?

You: What is Python?
Chatbot: Python is a high-level, interpreted programming language...

You: exit
Chatbot: Goodbye! Have a great day!
```

## Features
- ✅ Updated for latest OpenAI API (v1.0+)
- ✅ Conversation history maintained
- ✅ Error handling
- ✅ Environment variable for API key (secure)
- ✅ Simple command-line interface

## Note
This requires an active OpenAI API key and will incur API usage costs.

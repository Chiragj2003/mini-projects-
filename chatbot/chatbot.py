import os
try:
    from openai import OpenAI
except ImportError:
    print("Error: openai package not installed. Install with: pip install openai")
    exit(1)

# Get API key from environment variable
api_key = os.environ.get('OPENAI_API_KEY')

if not api_key:
    print("Error: OPENAI_API_KEY environment variable not set")
    print("Set it with: export OPENAI_API_KEY='your-api-key-here'")
    exit(1)

# Initialize OpenAI client (updated for v1.0+)
client = OpenAI(api_key=api_key)

# Conversation history
conversation_history = [
    {"role": "system", "content": "You are a helpful chatbot."}
]

def chat_with_gpt(user_input):
    """Send message to ChatGPT and get response"""
    # Add user message to history
    conversation_history.append({"role": "user", "content": user_input})
    
    try:
        # Use updated API (openai v1.0+)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=conversation_history
        )
        
        # Extract assistant's reply
        assistant_reply = response.choices[0].message.content
        
        # Add to conversation history
        conversation_history.append({"role": "assistant", "content": assistant_reply})
        
        return assistant_reply
    except Exception as e:
        return f"Error: {str(e)}"

# Start a conversation with the chatbot
print("="*50)
print("AI CHATBOT".center(50))
print("="*50)
print("Type 'exit', 'quit', or 'bye' to end the conversation\n")

while True:
    user_input = input("You: ").strip()
    
    if user_input.lower() in ['exit', 'quit', 'bye']:
        print("Chatbot: Goodbye! Have a great day!")
        break
    
    if not user_input:
        continue
    
    response = chat_with_gpt(user_input)
    print(f"Chatbot: {response}\n")
from pickle import HIGHEST_PROTOCOL
import openai

api_key = "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"
openai.api_key = api_key

def chat_with_gpt(user_input):
    # Define the initial system message and user message
    messages = [
        {"role": "system", "content": "You are a helpful chatbot."},
        {"role": "user", "content": user_input}
    ]

    # Send the messages to ChatGPT
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    # Extract and return the assistant's reply
    assistant_reply = response["choices"][0]["message"]["content"]
    return assistant_reply

# Start a conversation with the chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = chat_with_gpt(user_input)
    print("Chatbot:", response)
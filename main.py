import openai

# Set up your OpenAI API key
openai.api_key = 'sk-khbe--N9T6s0GgIipW3uUottFwnrFVLICV2oBZwV2gT3BlbkFJZ5snrdoFvw5qoCob4SHsOrbZFdIUQ-ey23ohhRDAsA'

# Function to generate a response from OpenAI
def generate_response(messages):
    response = openai.ChatCompletion.create(
        model="gpt-4o-2024-08-06",
        messages=messages,
        max_tokens=150,
        temperature=0.7,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6
    )
    message = response.choices[0].message['content'].strip()
    return message

# Start the conversation
def start_chat():
    print("Hi! I am your chatbot Zoe. Type 'quit' to exit.")
    messages = [{"role": "system", "content": "You are a helpful assistant."}]
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Lewis: Goodbye!")
            break
        
        messages.append({"role": "user", "content": user_input})
        
        response = generate_response(messages)
        print(f"Lewis: {response}")
        
        messages.append({"role": "assistant", "content": response})

# Run the chatbot
if __name__ == "__main__":
    start_chat()

from flask import Flask, request, jsonify, render_template
import openai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# Set up your OpenAI API key
openai.api_key = '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'

# Function to generate a response from OpenAI with error handling
def generate_response(messages):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=messages,
            max_tokens=150,
            temperature=0.7,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6
        )
        message = response.choices[0].message['content'].strip()
        return message
    except Exception as e:
        return f"Error: {str(e)}"

# Route to serve the HTML page
@app.route('/')
def home():
    return render_template('index.html')  # Renders the index.html in the 'templates' folder

# API route for chatbot
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    messages = [{"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}]
    
    # Get response from the chatbot
    response = generate_response(messages)
    
    # Return response as JSON
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True, port=5001)

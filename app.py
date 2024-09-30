from flask import Flask, request, jsonify, render_template
from transformers import T5ForConditionalGeneration, T5Tokenizer

# Initialize the Flask application
app = Flask(__name__)

# Load the trained model and tokenizer
tokenizer = T5Tokenizer.from_pretrained('t5-small')  # Use your model path if fine-tuned
model = T5ForConditionalGeneration.from_pretrained('t5-small')  # Use your model path if fine-tuned

# Define a function to answer questions
def answer_question(question, context):
    context = "SUI stands for Stress Urinary Incontinence."
    input_text = f"question: {question} context: {context}"
    input_ids = tokenizer.encode(input_text, return_tensors='pt')

    # Generate the output
    output_ids = model.generate(input_ids)
    answer = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    
    return answer

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    question = data.get('question')
    context = data.get('context', '')  # Optional context

    if not question:
        return jsonify({'error': 'No question provided'}), 400
    
    # Get the answer from the model
    answer = answer_question(question, context)

    return jsonify({'answer': answer})

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

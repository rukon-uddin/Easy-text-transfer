from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

stored_text = ""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send_text():
    global stored_text
    data = request.json
    stored_text = data['text']
    return jsonify({'message': 'Text received successfully'})

@app.route('/receive')
def receive_text():
    global stored_text
    return jsonify({'text': stored_text})


# if __name__ == "__main__":
#     app.run(debug=True)
from flask import Flask, render_template, request, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
import time

app = Flask(__name__)

scheduler = BackgroundScheduler()
scheduler.start()

stored_text = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send_text():
    global stored_text
    data = request.json
    stored_text[data['uid']] = {'text': data['text'], 'timestamp': time.time()}
    print(stored_text)
    return jsonify({'message': 'Text received successfully'})

@app.route('/receive', methods=['POST'])
def receive_text():
    global stored_text
    data = request.json
    print(stored_text)
    try:
        text = stored_text[data["uid"]]["text"]
    except:
        text = "ZqgQ9QOE2$sq5kr8p3Vg*GgGNq&"
    return jsonify({'text': text})

def clear_stored_data():
    global stored_text
    current_time = time.time()
    keys_to_delete = [key for key, value in stored_text.items() if (current_time - value['timestamp']) > 250]
    for key in keys_to_delete:
        del stored_text[key]

scheduler.add_job(clear_stored_data, 'interval', minutes=5)

# if __name__ == "__main__":
#     app.run(debug=True)
from flask import Flask, render_template, request, jsonify
import time
import redis

# stored_text = {}

app = Flask(__name__)


ext = "redis://red-cjk4je337aks73ek7ilg:6379"
redis_client = redis.StrictRedis.from_url(ext)

# redis_client = redis.StrictRedis(host="localhost", port=6379, db=0)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send_text():
    # global stored_text
    # keys_to_delete = [key for key, value in stored_text.items() if (current_time - value['timestamp']) > 60]
    keys_to_delete = []
    try:
        for key, value in redis_client.hgetall('stored_text').items():
            current_time = time.time()
            entry_parts = value.decode('utf-8').split('4099058')
            timestamp = float(entry_parts[2])

            if (current_time - timestamp) > 300:
                keys_to_delete.append(key.decode('utf-8'))
                
        for key in keys_to_delete:
            redis_client.hdel('stored_text', key)
    except:
        print("No data found")
    
    data = request.json
    # stored_text[data['uid']] = {'text': data['text'], 'timestamp': time.time()}
    entry = {
        "uid": data['uid'],
        "text": str(data['text']),
        "timestamp": str(time.time())
    }
    redis_client.hset('stored_text', data['uid'], "4099058".join(entry.values()))
    
    # print(redis_client.hgetall('stored_text'))
    return jsonify({'message': 'Text received successfully'})



@app.route('/receive', methods=['POST'])
def receive_text():
    data = request.json
    stored_entry = redis_client.hget('stored_text', data["uid"])
    # print(redis_client.hgetall("stored_text"))
    if stored_entry is None:
        text = "ZqgQ9QOE2$sq5kr8p3Vg*GgGNq&"
    else:
        stored_entry = stored_entry.decode('utf-8').split('4099058')
        text = stored_entry[1]
        redis_client.hdel("stored_text", stored_entry[0])
    
    
    return jsonify({'text': text})



# if __name__ == "__main__":
#     app.run(debug=True)
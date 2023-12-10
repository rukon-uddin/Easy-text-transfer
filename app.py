from flask import Flask, render_template, request, jsonify
import time
import redis
import itertools
import string
import random
import qrcode
import os

glob_counter = 0
characters = string.ascii_letters + string.digits + string.punctuation
combinations = itertools.product(characters, repeat=2)
combinations_as_strings = [''.join(combination) for combination in combinations]
random_char_len = len(combinations_as_strings)


app = Flask(__name__)


# ext = "redis://red-cjk4je337aks73ek7ilg:6379"
# redis_client = redis.StrictRedis.from_url(ext)
# ext = "redis://red-cljlrd1ll56s73blvii0:6379"
ext = "redis://localhost:6379/0" 
redis_client = redis.StrictRedis.from_url(ext)


# redis_client = redis.StrictRedis(host="localhost", port=6379, db=0)


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/share_text')
def shareText():
    return render_template("shareText.html")

@app.route('/get_text')
def getText():
    return render_template("getText.html")

@app.route('/send', methods=['POST'])
def send_text():
    global glob_counter
    global combinations_as_strings
    global random_char_len

    keys_to_delete = []
    try:
        for key, value in redis_client.hgetall('stored_text').items():
            current_time = time.time()
            entry_parts = value.decode('utf-8').split('4099058')
            timestamp = float(entry_parts[2])

            if (current_time - timestamp) > 120:
                keys_to_delete.append(key.decode('utf-8'))
                
        for key in keys_to_delete:
            redis_client.hdel('stored_text', key)
    except:
        print("No data found")
    
    rand_number = random.randint(0 , random_char_len-1)
    unique_id = combinations_as_strings[rand_number]

    while redis_client.hget("stored_text", unique_id) != None:
        rand_number = random.randint(0 , random_char_len-1)
        unique_id = combinations_as_strings[rand_number]

    data = request.json
    entry = {
        "uid": unique_id,
        "text": str(data['text']),
        "timestamp": str(time.time())
    }
    redis_client.hset('stored_text', unique_id, "4099058".join(entry.values()))

    qr_path = f"static/qrcode_{unique_id}.png"
    text_qr = f"http://192.168.10.92:8080/qrText?param1={unique_id}"
    qr_img = qrcode.make(text_qr)
    qr_img.save(qr_path)
    # print(redis_client.hgetall('stored_text'))
    return jsonify({'message': unique_id, 'qr_path': qr_path})



@app.route('/receive', methods=['POST'])
def receive_text():

    data = request.json

    stored_entry = redis_client.hget('stored_text', data["uid"])

    if stored_entry is None:
        text = "ZqgQ9QOE2$sq5kr8p3Vg*GgGNq&"
    else:
        stored_entry = stored_entry.decode('utf-8').split('4099058')
        os.remove(f"static/qrcode_{data['uid']}.png")
        text = stored_entry[1]
        redis_client.hdel("stored_text", stored_entry[0])
    
    
    return jsonify({'text': text})

@app.route('/qrText', methods=["GET"])
def qrText():
    param1 = request.args.get('param1')

    stored_entry = redis_client.hget('stored_text', param1)

    if stored_entry is None:
        text = "ZqgQ9QOE2$sq5kr8p3Vg*GgGNq&"
    else:
        stored_entry = stored_entry.decode('utf-8').split('4099058')
        os.remove(f"static/qrcode_{param1}.png")
        text = stored_entry[1]
        redis_client.hdel("stored_text", stored_entry[0])

    print("***** ", text)
    return render_template('qrShow.html', result=text, uid=param1)


# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0", port=8080)

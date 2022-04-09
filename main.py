import json
from flask import Flask, request, jsonify, render_template
from random import randint


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form
        w = data['word']
        m = data['meaning']
        # append to file
        mean_data = json.load(open('words.json'))
        with open('words.json', 'w') as f:
            mean_data[w] = m
            json.dump(mean_data, f)

    # read json file 'words.json'
    with open('words.json') as f:
        data = json.load(f)
    keys = list(data.keys())
    values = list(data.values())
    
    # get random word from json file
    if len(keys) > 0:
        r = randint(0, len(keys) - 1)
        w = keys[r]
        m = values[r]
    else:
        w = 'No word'
        m = 'No meaning'

    return render_template('index.html', word=w, meaning=m)


@app.route('/2', methods=['GET', 'POST'])
def index2():
    if request.method == 'POST':
        data = request.form
        w = data['word']
        m = data['meaning']
        # append to file
        mean_data = json.load(open('words.json'))
        with open('words.json', 'w') as f:
            mean_data[w] = m
            json.dump(mean_data, f)

    # read json file 'words.json'
    with open('words.json') as f:
        data = json.load(f)
    keys = list(data.keys())
    values = list(data.values())
    
    # get random word from json file
    if len(keys) > 0:
        ws = keys
        ms = values
    else:
        ws = ['No word']
        ms = ['No meaning']

    words = zip(ws, ms, list(range(len(ws))))

    return render_template('index2.html', words=words)


app.run(host='0.0.0.0', port=80, debug=False, threaded=False)

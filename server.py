#!/usr/bin/env python3
from flask import Flask, request, render_template
from generativepoetry.decomposer import cutup as cut
from markov import Markov_Class as MarkovDictionary
from textvomit import clean

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route("/markov", methods=['POST'])
def markov():
    markov = MarkovDictionary()
    wordcount = int(request.args.get('wordcount'))
    format = request.args.get('format')
    return markov.generate_output(clean(request.get_data().decode(encoding='UTF-8'), format), wordcount, format)

@app.route("/cutup", methods=['POST'])
def cutup():
    cleaned_input = clean(request.get_data().decode(encoding='UTF-8'), format)
    cutup_min_size = False if request.args.get('cutupmin') == "false" else int(request.args.get('cutupmin'))
    cutup_max_size = False if request.args.get('cutupmin') == "false" else int(request.args.get('cutupmax'))
    if cutup_min_size:
        return " ".join(cut(cleaned_input, min_cutout_words=cutup_min_size, max_cutout_words=cutup_max_size))

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=7878,
        debug=True
    )


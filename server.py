#!/usr/bin/env python2.7

from flask import Flask, request, render_template
from markov import Markov_Class as MarkovDictionary
from cutup import Cutup_Class
from textvomit import clean

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route("/markov", methods=['POST'])
def markov():
  cutup_min_size = False if request.args.get('cutupmin') == "false" else int(request.args.get('cutupmin'))
  cutup_max_size = False if request.args.get('cutupmin') == "false" else int(request.args.get('cutupmax'))
  if cutup_min_size:
    cutup = Cutup_Class()
    return cutup.generate_output(clean(request.get_data().decode(encoding='UTF-8'), False, False), cutup_min_size, cutup_max_size)
  else:
    markov = MarkovDictionary()
    wordcount = int(request.args.get('wordcount'))
    format = request.args.get('format')
    return markov.generate_output(clean(request.get_data().decode(encoding='UTF-8'), format), wordcount, format)


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=8080,
        debug=True
    )

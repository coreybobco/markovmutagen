#!/usr/bin/env python3
from flask import Flask, request, render_template
from generativepoetry.decomposer import cutup as cutup_technique
from generativepoetry.decomposer import markov as markov_technique
from formatter import *

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route("/markov", methods=['POST'])
def markov():
    cleaned_input = clean(request.get_data().decode(encoding='UTF-8'))
    ngram_size = int(request.args.get('ngram_size'))
    output_format = request.args.get('output_format')
    output = " ".join(markov_technique(cleaned_input, ngram_size=ngram_size))
    if output_format == 'aphorisms':
        output = format_aphorisms(output)
    return output


@app.route("/cutup", methods=['POST'])
def cutup():
    cleaned_input = clean(request.get_data().decode(encoding='UTF-8'))
    cutup_min_size =  int(request.args.get('cutupmin'))
    cutup_max_size =  int(request.args.get('cutupmax'))
    output = " ".join(cutup_technique(cleaned_input, min_cutout_words=cutup_min_size, max_cutout_words=cutup_max_size))
    output_format = request.args.get('output_format')
    if output_format == 'aphorisms':
        output = format_aphorisms(output)
    return output

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=7878,
        debug=True
    )


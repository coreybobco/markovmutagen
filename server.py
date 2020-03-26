#!/usr/bin/env python3
from flask import Flask, request, render_template
from generativepoetry.decomposer import cutup as cutup_technique
from generativepoetry.decomposer import markov as markov_technique

def clean(source_text):
  # fix punctuation
  print(source_text)
  sentence_delimiters = [".", "?", "!"]
  clause_delimiters = ["...", ";", "--"]
  source_text = source_text.replace("---","--").replace("..", "...").replace("....", "...")
  for char in (sentence_delimiters + clause_delimiters):
    source_text = source_text.replace(char, char + " ")
  # strip useless characters
  source_text = source_text.replace("\n", " ")
  if format == 'chat':
    useless = ["\t", "\"", "\'"]
  else:
    useless = ["\t", "\n", "\""]
  for char in useless:
    source_text = source_text.replace(char, "")
  word_list = source_text.split(" ")
  return " ".join(word_list)

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route("/markov", methods=['POST'])
def markov():
    cleaned_input = clean(request.get_data().decode(encoding='UTF-8'))
    ngram_size = int(request.args.get('ngram_size'))
    return " ".join(markov_technique(cleaned_input, ngram_size=ngram_size))

@app.route("/cutup", methods=['POST'])
def cutup():
    cleaned_input = clean(request.get_data().decode(encoding='UTF-8'))
    cutup_min_size =  int(request.args.get('cutupmin'))
    cutup_max_size =  int(request.args.get('cutupmax'))
    if cutup_min_size:
        return " ".join(cutup_technique(cleaned_input, min_cutout_words=cutup_min_size,
                                        max_cutout_words=cutup_max_size))

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=7878,
        debug=True
    )


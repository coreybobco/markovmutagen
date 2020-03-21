#!/usr/bin/env python3
from flask import Flask, request, render_template
from generativepoetry.decomposer import cutup as cut

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
  return word_list

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route("/markov", methods=['POST'])
def markov():
    cleaned_input = clean(request.get_data().decode(encoding='UTF-8'))
    return markov(cleaned_input)

@app.route("/cutup", methods=['POST'])
def cutup():
    cleaned_input = clean(request.get_data().decode(encoding='UTF-8'))
    cutup_min_size =  int(request.args.get('cutupmin'))
    cutup_max_size =  int(request.args.get('cutupmax'))
    if cutup_min_size:
        return " ".join(cut(cleaned_input, min_cutout_words=cutup_min_size, max_cutout_words=cutup_max_size))

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=7878,
        debug=True
    )


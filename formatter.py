import random
import nltk

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
  useless = ["\t", "\n", "\""]
  for char in useless:
    source_text = source_text.replace(char, "")
  word_list = source_text.split(" ")
  return " ".join(word_list)

def format_aphorisms(text):
  sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
  sentences = sent_detector.tokenize(text)
  formatted_output = ""
  aphorism_number = 1
  while(len(sentences)):
    formatted_output += "—" + str(aphorism_number) + "—\n"
    for i in range(random.randint(0,2)):
      formatted_output += sentences.pop(0) + " "
    formatted_output += '\n\n'
    aphorism_number += 1
  return formatted_output


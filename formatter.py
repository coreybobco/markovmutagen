import random
import re
import nltk


def clean(source_text):
  # fix punctuation
  print(source_text)
  sentence_delimiters = ["?", "!"]
  clause_delimiters = ["...", ";", "--"]

  # strip useless characters
  cleaned_text = source_text.replace("\n", " ")
  useless = ["\t", "\n", "\""]
  for char in useless:
    cleaned_text = cleaned_text.replace(char, "")
  # Replace .... and .. with ...
  cleaned_text = re.sub(r'(?<=[\sA-Za-z])\.\.(?=[\sA-Za-z])', '...', cleaned_text)
  cleaned_text = re.sub(r'(?<=[\sA-Za-z])\.\.\.\.(?=[\sA-Za-z])', '...', cleaned_text)
  # Replace --- with --
  cleaned_text = re.sub(r'(?<=[\sA-Za-z])---(?=[\sA-Za-z])', '--', cleaned_text)
  for char in (sentence_delimiters + clause_delimiters):
    cleaned_text = cleaned_text.replace(char, char + " ")
  return cleaned_text

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


def sample_document(document, format, sample_size):
  sample = ''
  if format == 'random_paragraphs':
    for i in range(sample_size - 1):
      sample += document.random_paragraph()
  elif format == 'random_sentences':
    for i in range(sample_size - 1):
      sample += document.random_sentence()
  else:
    sample = document.raw_text
  return sample
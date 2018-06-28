#!/usr/bin/python
import string
import sys
import argparse
import re
from random import randint
from markov import Markov_Class
from cutup import Cutup_Class

def main():
  parser = argparse.ArgumentParser(description="order of textual operations")
  parser.add_argument("-m", "--markov", help="use markov chains to generate text output of a specified length", type=int)
  parser.add_argument("-c", "--cutup", nargs=2, help="cut up input with cut up block size between X and Y", type=int)
  parser.add_argument("-p", "--poem", help="produce the output in the form of a poem", action="store_true")
  parser.add_argument("-cl", "--chatlog", help="produce the output in the form of a chatlog (requires chat format)", action="store_true")
  parser.add_argument("-sf", "--sample_file", help="grab random excerpt of length X for markov processing", type=int)
  parser.add_argument("-a", "--aphorisms", help="accept input as aphorisms, also output as aphorisms", action="store_true")
  format = False
  while not format:
    format = 'poem' if request.args.get('poem') else False
    format = 'chat' if request.args.get('chat') else False
    format = 'aphorisms' if request.args.get('aphorisms') else False
  args = parser.parse_args()
  markov_obj = Markov_Class()
  cutup_obj = Cutup_Class()
  if args.sample_file:
    word_list = clean(sample_file(args.sample_file, args.aphorisms))
  else:
    word_list = (clean(take_input()), args.chatlog, args.aphorisms)
  if args.markov:
    output_length = args.markov
    print(markov_obj.generate_output(word_list, output_length, format))
  if args.cutup:
    cutup_obj.generate_output(word_list, args.cutup[0], args.cutup[1])

def sample_file(sample_length, aphorisms):
  print('Enter filename (file must be in relative path)')
  filename = "./" + input()
  file = open(filename, "r")
  file_string = file.read()
  if aphorisms:
    file_string = re.sub('\+?\d.', '', file_string)
  file_length = len(file_string)
  sample_position = randint(0, file_length - sample_length)
  end_of_word = False
  if end_of_word and file_string[sample_position - 1] != " ":
    sample_position = sample_position
  else:
    sample_position = sample_position
    end_of_word = True
  return file_string[sample_position:sample_position + sample_length]

def take_input():
  print('Enter text input below. Hit ctrl-c when done.')
  input_lines = []
  try:
    while True:
      input_lines.append(input())
  except KeyboardInterrupt:
      return " ".join(input_lines)

def clean(source_text, format):
  # fix punctuation
  print(source_text)
  sentence_delimiters = [".", "?", "!"]
  clause_delimiters = ["...", ";", "--"]
  source_text = source_text.replace("---","--").replace("..", "...").replace("....", "...")
  for char in (sentence_delimiters + clause_delimiters):
    source_text = source_text.replace(char, char + " ")
  if format == 'aphorisms':
    source_text = re.sub('\^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$', '', source_text)
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

if __name__ == "__main__":
    main()

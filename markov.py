#!/usr/bin/env python
import json
import random
import string
import sys

class Markov_Class:
  def __init__(self):
    return

  def contains_character(self, character_list, word):
    for character in character_list:
      if character in word:
        return True
    return False

  def ends_with_character_type(self, word, character_list):
    for character in character_list:
      if word.endswith(character):
        return True
    return False

  def starts_with_character_type(self, word, character_list):
    for character in character_list:
      if word.startswith(character):
        return True
    return False

  def create_sample_pool(self, word_map):
    sample_pool = []
    for word in word_map.keys():
      count = word_map[word]
      for i in range(count):
        sample_pool.append(word)
    return sample_pool

  def generate_output(self, word_array, output_length, format):
    probs = { }
    sentence_starters = {}
    clause_starters = {}

    if not format == 'chat':
      sentence_delimiters = [".", "?", "!"]
      clause_delimiters = ["...", ";", "--", ","]
      quotation_marks = ['"', "'", "“", "”", "‘", "’"]
    else:
      sentence_delimiters = []
      clause_delimiters = []
      quotation_marks = []
    word_array = [word for word in word_array if word != ""]
    last_word = word_array[-1];
    sentence_starters[word_array[0]] = 1;
    # record frequencies / classify words
    for word in word_array:
      if len(last_word) > 0 and last_word[-1] in sentence_delimiters:
        if word not in sentence_starters.keys():
          sentence_starters[word] = 1
        else:
          sentence_starters[word] += 1
      if len(last_word) > 0 and self.contains_character(clause_delimiters, last_word):
        if word not in clause_starters.keys():
          clause_starters[word] = 1
        else:
          clause_starters[word] += 1
      if not last_word in probs.keys():
        probs[last_word] = {}
        probs[last_word][word] = 1
      else:
        if word not in probs[last_word].keys():
          probs[last_word][word] = 1
        else:
          probs[last_word][word] += 1
      last_word = word

    generated_list = [random.choice(self.create_sample_pool(sentence_starters))]
    beginning_quotation = False
    words_on_line = 0
    for i in range(output_length):
      last_word = generated_list[-1]
      next_word = ""
      if self.contains_character(sentence_delimiters, last_word) or last_word not in probs:
        words_on_line +=1
        if format == 'poem':
          next_word = "\n"
          words_on_line = 1
        next_word += random.choice(self.create_sample_pool(sentence_starters))
      elif self.contains_character(clause_delimiters, last_word):
        words_on_line += 1
        if format == 'poem':
          next_word = "\n"
          words_on_line = 1
        next_word += random.choice(self.create_sample_pool(clause_starters))
      elif last_word in probs:
        words_on_line += 1
        if format == 'poem' and words_on_line == 10:
          next_word = "\n"
          words_on_line = 1
        next_word += random.choice(self.create_sample_pool(probs[last_word]))

      # Check quotes
      if self.ends_with_character_type(next_word, quotation_marks):
        if beginning_quotation:
          if beginning_quotation == "‘":
            next_word = next_word[:-1] + "’"
          elif beginning_quotation == "“":
            next_word = next_word[:-1] + "”"
          else:
            next_word = next_word[:-1] + beginning_quotation
          beginning_quotation = False
        else:
          next_word = next_word[:-1]
      if self.starts_with_character_type(next_word, quotation_marks):
        if beginning_quotation == False:
          beginning_quotation = next_word[0]
        else:
          next_word = next_word[1:]
      if beginning_quotation and self.ends_with_character_type(next_word, clause_delimiters):
        if random.random() > .5:
          if beginning_quotation == "‘":
            next_word += "’"
          elif beginning_quotation == "“":
            next_word += "”"
          else:
            next_word += beginning_quotation
          beginning_quotation = False
      elif beginning_quotation and self.ends_with_character_type(next_word, sentence_delimiters):
        if beginning_quotation == "‘":
          ending_quote = "’"
        elif beginning_quotation == "“":
          ending_quote = "”"
        else:
          ending_quote = beginning_quotation
        if next_word.endswith("."):
          next_word += ending_quote
        else:
          next_word += ending_quote + " ."
        beginning_quotation = False
      generated_list.append(next_word)
    for i in range(50):
      print("\n")

    if format == 'chat':
      chat_list = []
      for word in generated_list:
        if word.startswith("<"):
          print(word)
          chat_list.append("\n" + word)
        else:
          chat_list.append(word)
      return(" ".join(chat_list))
    if format == 'aphorisms':
      aphorism_counter = 1
      aphorism_list = [str(aphorism_counter) + "\n\n"]
      sentence_delimiters = [".", "?", "!"]
      aphorism_sentence_length = random.randint(1, 5)
      current_sentence_length = 0
      sentence_starter = True
      for word in generated_list:
        if word[len(word) - 1] in sentence_delimiters:
          current_sentence_length += 1
          if current_sentence_length >= aphorism_sentence_length:
            aphorism_counter += 1
            aphorism_list.append(word + " \n\n" + str(aphorism_counter) + "\n\n")
            current_sentence_length = 0
            sentence_starter = True
          elif sentence_starter == True:
            aphorism_list.append(word.capitalize())
            sentence_starter = False
          else:
            aphorism_list.append(word)
        else:
          aphorism_list.append(word)
      return " ".join(aphorism_list)
    else:
      return " ".join(generated_list)
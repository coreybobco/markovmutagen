#!/usr/bin/python
import re
import json
import random
import string
import sys

class Cutup_Class:
  def generate_output(self, word_array, min_block_size, max_block_size):
    current_position = 0
    chunks = []
    while True:
      next_length = self.random_chunk_length(min_block_size, max_block_size)
      next_position = current_position + next_length
      if next_position > len(word_array):
        break
      chunks.append(word_array[current_position:next_position])
      current_position = next_position
    random.shuffle(chunks)
    chunks = " ".join(map(lambda x: " ".join(x), chunks))
    return chunks

  def random_chunk_length(self, min_block_size, max_block_size):
    return random.choice(list(range(min_block_size, max_block_size + 1)))

"""A rhyming dictionary which identifies slant rhymes as well as new rhymes

Usage: 
python RhymesWithOrange.py <word to rhyme> 
"""

import os
import re
import sys
import urllib

def find_word(input):
  f = open('cmudict.txt')
  for line in f:
    list = line[:-1].split(" ")
    if input.upper() == list[0]:
      return (line, list)
      
def extract_rhyme(syllables):
  i = 0
  for syllable in syllables:
    match = re.search(r"\w\w1", syllable)
    if match:
      return syllables[i:]
    i += 1
    
# returns all rhymes in a list of lists organized by syllable.
# list_of_lists[0] = all 1 syllable words
# list_of_lists[1] = all 2 syllable words
# etc...
def find_perfect_rhyme(rhyme, input):
  f = open('cmudict.txt')
  # make list of 14 lists. The number 14 was chosen because 14 is the largest amount of 
  # syllables contained in one word in the CMU dictionary.
  l = []
  list_of_lists = []
  for i in range(14):
    list_of_lists.append(l[:])
  for line in f:
    line_list = line[:-1].split(" ") #line_list = this line as a list split by spaces
    if len(line_list) >= len(rhyme) + 2:
      if line_list[-len(rhyme):] == rhyme and line_list[0] != input.upper():
        list_of_lists[count_vowels(line) - 1].append(line_list[0])
  return list_of_lists

def find_assonance(vowels, input):
  f = open('cmudict.txt')
  l = []
  list_of_lists = []
  for i in range(14):
    list_of_lists.append(l[:])
  for line in f:
    line_list = line[:-1].split(" ")
    cur_word = line_list[0]
    cur_vowels = get_vowels(line)
    if len(cur_vowels) >= len(vowels):
      if cur_vowels[-len(vowels):] == vowels and cur_word != input.upper():
        list_of_lists[len(cur_vowels) - 1].append(cur_word)
  return list_of_lists
        
def count_vowels(line):
  vowels = re.findall(r"\w\w\d", line)
  return len(vowels)
  
def get_vowels(pronunciation):
  vowels = re.findall(r"\w\w\d", pronunciation)
  return vowels

  
def value(tuple):
  return tuple[1]

def main():
  args = sys.argv[1:]
  
  if not args:
    print('usage: please enter a word')
    sys.exit(1)

  
  input_tuple = find_word(args[0])
  if not input_tuple:
    print("There are no matches for this word")
    sys.exit(1)
  
  rhyme = extract_rhyme(input_tuple[1])
  if not rhyme:
    print("Error in database: no primary stress for word", args[0])
  if len(args) > 1:
    if args[1] == 'p':
      print('Pronunciation of  "' + args[0] + '":')
      print(rhyme)
      print("\n")
  
  print('Perfect Rhymes:\n')
  rhymes = find_perfect_rhyme(rhyme, args[0])
  for idx, syllable_group in enumerate(rhymes):
    if syllable_group:
      print(idx + 1, "Syllable Words")
      txt = ""
      for word in syllable_group:
        txt += word + ' '
      print(txt +"\n")
  assrhyme = get_vowels(input_tuple[0])
  assonances = find_assonance(assrhyme, args[0])
  print("Assonance Rhymes:\n")
  for idx, syllable_group in enumerate(assonances):
    if syllable_group:
      print(idx + 1, "Syllable Words")
      txt = ""
      for word in syllable_group:
        txt += word + ' '
      print(txt +"\n")
    

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()

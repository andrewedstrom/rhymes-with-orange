"""
finds the word with the most syllables in cmudict
"""

import os
import re
import sys
import urllib

def count_vowels(line):
  list = re.findall(r"\w\w\d", line)
  return len(list)
  
def main():
  longest = 0
  f = open('cmudict.txt')
  for line in f:
    numSyls = count_vowels(line)
    if numSyls > longest:
      longest = numSyls
  print longest
  
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()

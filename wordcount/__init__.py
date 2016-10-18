from flask import Flask, jsonify
from flask import request
from fileinput import filename

import sys
import os
sys.path.append(os.path.join(sys.path[0],'wordcount', 'build'))
import cppExtUtil

app = Flask(__name__)

@app.route('/')
def index():
    return 'Wordcount service is online'

def print_words(filename):
  wordCountDict = create_word_count_dict(filename)
  for key in sorted(wordCountDict):
    print key + ' ' + str(wordCountDict[key])

def print_top(filename):
  wordCountDict = create_word_count_dict(filename)
  sortedWordCountDict = sorted(wordCountDict, key=wordCountDict.get, reverse=True)
  resultDictionary = {}
  for key in sortedWordCountDict[:20]:
    resultDictionary[key] = wordCountDict[key]
    #print >> sys.stderr, key, str(resultDictionary[key])

  return resultDictionary

def print_top_cpp(filename):
  # Build dictionary using c++ from cppExtUtil
  wordCountDict = cppExtUtil.create_word_count_dictionary(filename);
  sortedWordCountDict = sorted(wordCountDict, key=wordCountDict.get, reverse=True)
  resultDictionary = {}
  for key in sortedWordCountDict[:20]:
    resultDictionary[key] = wordCountDict[key]
    #print >> sys.stderr, key, str(resultDictionary[key])

  return resultDictionary

def create_word_count_dict(filename):
  # Create a word count dictionary from filename
  # Also implemented in cppExtUtil
  f = open(filename)
  wordCountDict = {}

  for line in f:
    wordList = line.split()
    for word in wordList:
      word = word.lower()
      if word not in wordCountDict.keys():
        wordCountDict[word] = 1
      else:
        wordCountDict[word] = wordCountDict.get(word) + 1

  f.close()
  return wordCountDict

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
@app.route('/count', methods=['GET'])
def count_words():
  option = request.args.get('cmd', '')
  filename = 'alice.txt'
  scriptdir = os.path.dirname(os.path.abspath(__file__))
  sp_file = os.path.join(scriptdir, filename)
  filename = sp_file
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    result = print_top(filename)
    return jsonify(result)
  elif option == '--topcountcpp':
    result = print_top_cpp(filename)
    return jsonify(result)
  else:
    return 'unknown option: ' + option

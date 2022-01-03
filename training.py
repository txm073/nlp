# Standard
import os
import json
import time
import pickle
import random
import string

start = time.time()

# Natural language processing
from nltk import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer

"""
# Neural network
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation
from tensorflow.keras.optimizers import SGD
import numpy as np
"""

try:
    os.chdir(os.path.dirname(__file__))
except OSError:
    pass

# ----- Pre-processing -----

alphabet = list("abcdefghijklmnopqrstuvwxyz ")
char_to_int = dict((c, i) for i, c in enumerate(alphabet))
int_to_char = dict((i, c) for i, c in enumerate(alphabet))

def OHEncode(string):
    int_encoded = []
    for char in string:
        int_encoded.append(char_to_int[char])

    bin_encoded = []
    for value in int_encoded:
        row = [0] * len(alphabet)
        row[value] = 1
        bin_encoded.append(row)    
    
    return bin_encoded

def OHDecode(array):
    string = ""
    for row in array:
        one_pos = row.index(1)
        string += int_to_char[one_pos]
        return string

def training_pairs(string, slider_size=2):
    words = word_tokenize(string)
    samples = []
    for count, value in enumerate(words):
        word_samples = []
        
        for i in range(-slider_size, slider_size+1):
            sub_count = count + i
            if sub_count >= 0 and sub_count < len(words) and value != words[sub_count]:
                word_samples.append((value, words[sub_count]))
        samples.append(word_samples)
    
    return samples

string = "hey guys whats going on today"
print(f"Beginning preprocessing on '{string}'")
samples = training_pairs(string)
training = []
for sample in samples:
    training_sample = []
    for tup in sample:
        target_word, context_word = tup
        training_sample.append([OHEncode(target_word), OHEncode(context_word)])
    training.append(training_sample)

print(f"Finished preprocessing for '{string}'")

#print(training)

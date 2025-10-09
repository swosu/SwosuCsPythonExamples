# we want to crack a ceasar cipher
# L ORYH PDWKP

# we don't know what the offset is, so we will try all 25 possible offsets
# now check all of those results to see which one makes sense using a imported dictinoary or somthing
import string
from collections import Counter
import nltk
from nltk.corpus import words
nltk.download('words')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
import re
import enchant
import itertools
import math
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from difflib import SequenceMatcher
import Levenshtein
import pyenchant

# Load English dictionary
d = enchant.Dict("en_US")
english_words = set(words.words())
vectorizer = CountVectorizer().fit_transform(english_words)
vectors = vectorizer.toarray()
csim = cosine_similarity(vectors)
word_list = list(english_words)
word_index = {word: i for i, word in enumerate(word_list)}
d = pyenchant.Dict("en_US")
alphabet = string.ascii_uppercase
alphabet_lower = string.ascii_lowercase
alphabet_size = len(alphabet)
alphabet_size_lower = len(alphabet_lower)
punctuation = string.punctuation + "“”‘’—"
common_words = set(nltk.corpus.brown.words())
common_words = {word.lower() for word in common_words if word.isalpha()}

def caesar_decrypt(ciphertext, offset):
    decrypted = []
    for char in ciphertext:
        if char in alphabet:
            index = (alphabet.index(char) - offset) % alphabet_size
            decrypted.append(alphabet[index])
        elif char in alphabet_lower:
            index = (alphabet_lower.index(char) - offset) % alphabet_size_lower
            decrypted.append(alphabet_lower[index])
        else:
            decrypted.append(char)
    return ''.join(decrypted)

def score_text(text):
    words = re.findall(r'\b\w+\b', text.lower())
    if not words:
        return 0
    word_count = len(words)
    valid_word_count = sum(1 for word in words if d.check(word))
    valid_word_ratio = valid_word_count / word_count

    common_word_count = sum(1 for word in words if word in common_words)
    common_word_ratio = common_word_count / word_count

    avg_word_length = sum(len(word) for word in words) / word_count

    punctuation_count = sum(1 for char in text if char in punctuation)
    punctuation_ratio = punctuation_count / len(text) if len(text) > 0 else 0

    score = (valid_word_ratio * 0.5 + common_word_ratio * 0.3 + (1 - abs(avg_word_length - 4) / 4) * 0.1 + (1 - punctuation_ratio) * 0.1)
    return score

def crack_caesar_cipher(ciphertext):
    best_score = -1
    best_offset = 0
    best_decryption = ""
    for offset in range(1, 26):
        decrypted_text = caesar_decrypt(ciphertext, offset)
        current_score = score_text(decrypted_text)
        if current_score > best_score:
            best_score = current_score
            best_offset = offset
            best_decryption = decrypted_text
    return best_offset, best_decryption

ciphertext = "L ORYH PDWKP"

offset, decrypted_message = crack_caesar_cipher(ciphertext)
print(f"Best Offset: {offset}")
print(f"Decrypted Message: {decrypted_message}")
# Expected output:
# Best Offset: 3
# Decrypted Message: I LOVE MATHE
# Note: The actual decrypted message will depend on the input ciphertext.
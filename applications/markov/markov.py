import random

import re
from collections import defaultdict

# Read in all the words in one go
with open("input.txt", 'r') as f:
    if f.mode == 'r':
        words = f.read()
        # print(words, end=' ')
tokenized_text = [
    word
    for word in re.split('\W+', words)
    if word != ''
]

graph = defaultdict(lambda: defaultdict(int))

last_word = tokenized_text[0].lower()
for word in tokenized_text[1:]:
    word = word.lower()
    graph[last_word][word] += 1
    last_word = word

limit = 3
random_word = random.choices(words)
for first_word in random_word:
    next_words = list(graph[first_word].keys())[:limit]
    for next_word in next_words:
        print(first_word, next_word)

# TODO: analyze which words can follow other words
# Your code here

    



# TODO: construct 5 random sentences
# Your code here


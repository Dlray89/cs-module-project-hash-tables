import random


# Read in all the words in one
text_file = open('input.txt', encoding='utf8').read()

new_words = text_file.split()

def make_pairs(new_words):
    for i in range(len(new_words) - 1):
        yield(new_words[i], new_words[i + 1])

pairs = make_pairs(new_words)

word_dict = {}

for word_1, word_2 in pairs:
    if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
    else:
        word_dict[word_1] = [word_2]

first_word = random.choice(new_words)

while first_word.islower():
    first_word = random.choice(new_words)

chain = [first_word]
print(chain)
n_words = 20

for i in range(n_words):
    chain.append(random.choice(word_dict[chain[-1]]))

' '.join(chain)

new_chain = ' '.join(chain)


print(new_chain)



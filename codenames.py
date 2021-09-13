import itertools
import random

def load_words(filename):
    with open(filename) as f:
        words = [line.split() for line in f]
    return ([word for word, count in words],
            list(itertools.accumulate(int(count) for word, count in words)))

adjs, adjs_weights = load_words('words/adj.txt')
nouns, nouns_weights = load_words('words/noun.txt')

for _ in range(20):
    while True:
        adj = random.choices(adjs, cum_weights=adjs_weights)[0]
        noun = random.choices(nouns, cum_weights=nouns_weights)[0]
        if len(adj) >= 3 and len(noun) >= 3:
            break
    print(adj, noun)

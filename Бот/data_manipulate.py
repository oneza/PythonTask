import pickle
import razdel
import os
import collections
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from keras.preprocessing.sequence import pad_sequences
from random import shuffle
sns.set(color_codes=True)

def load_obj(name):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)
    
def tokenize(text):
    return [SEQUENCE_START] + [t.text for t in razdel.tokenize(text.lower())] + [SEQUENCE_END]
    
def do_vocab():
    PAD_INDEX = 0
    all_words = [y for x in tokenized for y in x] #vocab size 40-120
    
    token_counts = collections.Counter(all_words)
    vocabulary = {'PAD': PAD_INDEX, 'UNKNOWN': UNKNOWN_INDEX}
    for token, count in token_counts.most_common():
        if count > 1:
            vocabulary[token] = len(vocabulary)
        
    VOCABULARY_SIZE = len(vocabulary)
    print(VOCABULARY_SIZE)
    with open('vocabulary.pkl', 'wb') as handle:
        pickle.dump(vocabulary, handle)
        
UNKNOWN_INDEX = 1
SEQUENCE_START = '<START>'
SEQUENCE_END = '<END>'

data = load_obj('data_bot')
names_and_recipes = []
for recipe in data:
    try:
        intstructions = ''
        for sentence in recipe['recipeInstructions']:
            intstructions += sentence
    except:
        continue
    n_a_r = recipe['name'] + ':' + intstructions
    names_and_recipes.append(n_a_r)
shuffle(data)

tokenized = []
for recipe in names_and_recipes:
    t = tokenize(recipe)
    #if (len(t) >= 40 and len(t) < 100):
    if (len(t) >= 100 and len(t) <= 120):
        tokenized.append(t)
    
print(len(tokenized))

vocabulary = load_obj('vocabulary')

MAX_TEXT_LENGTH = 120
samples = []
targets = []
for recipe in tokenized:
    for tokens in recipe:
        indices = np.array([vocabulary.get(token, UNKNOWN_INDEX) for token in recipe],dtype=np.uint16)
        for i in range(1, len(recipe)):
            targets.append(indices[i])
            samples.append(indices[:min(MAX_TEXT_LENGTH,i)])
            
X_train, X_test, y_train, y_test = train_test_split(samples, targets, test_size=0.1)
np.save('y_train_120_100_120',y_train)
np.save('y_test_120_100_120',y_test)
del y_train
del y_test
del samples
del targets

X_test = pad_sequences(X_test, MAX_TEXT_LENGTH,dtype=np.uint16)
np.save('X_test_120_100_120',X_test)
del X_test
X_train = pad_sequences(X_train, MAX_TEXT_LENGTH,dtype=np.uint16)
np.save('X_train_120_100_120',X_train)
del X_train

t = []
l = [] # words in a sentence in a recipes whose len: 40<=len<=120
max_sentences = []
max_recipe = ''
for recipe in names_and_recipes:    
    temp = recipe.split('.')
    for real_sentence in temp:
        temp_l = len(real_sentence.split())
        if (temp_l > 0):
            l.append(temp_l)
        if temp_l > 100:
            max_sentences.append(real_sentence)
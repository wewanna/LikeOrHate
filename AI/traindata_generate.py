import csv
import nltk
from gensim.models import Word2Vec
from nltk.tokenize import RegexpTokenizer
import numpy as np
import pickle

datafile = open('train_data.csv', 'r', encoding='utf-8')
data = list(csv.reader(datafile))
data = list(map(lambda x: [int(x[0]), x[1]], data[1:]))
print(len(data))
datafile.close()

train_labels = []
sentences = []
tokenizer = RegexpTokenizer("[\w]+")
for s in data:
    sentences.append(tokenizer.tokenize(s[1]))
    train_labels.append(s[0])
print(sentences[:5])

model = Word2Vec(sentences=sentences, size=100, window=5, workers=4, iter=100, sg=0)
train_data = np.zeros((len(sentences), 100))
np.seterr(divide='ignore', invalid='ignore')
for i in range(len(sentences)):
    sentence = sentences[i]
    count = 0
    for w in sentence:
        if not model.wv.__contains__(w):
            continue
        vec = model.wv.__getitem__(w)
        count += 1
        for j in range(100):
            train_data[i, j] += vec[j]
    train_data[i] /= count
print(train_data[0])

with open('train_data.dataset', 'wb') as f:
    pickle.dump(train_data, f)
with open('train_labels.dataset', 'wb') as f:
    pickle.dump(train_labels, f)






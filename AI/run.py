import tensorflow as tf
import numpy as np
from tensorflow import keras

imdb = keras.datasets.imdb

word_index = imdb.get_word_index()

word_index = {k:(v+3) for k,v in word_index.items()}
word_index["<PAD>"] = 0
word_index["<START>"] = 1
word_index["<UNK>"] = 2  # unknown
word_index["<UNUSED>"] = 3

model = tf.keras.models.load_model('model-logs/latest-likeorhate-model.h5')

def encode_review(text):
    temp = text.split()
    change = []
    for i in range(0, len(temp)):
        change.append(word_index[temp[i]])
    return change

def predict(text):
    model = tf.keras.models.load_model('model-logs/latest-likeorhate-model.h5')
    predictions = model.predict_classes(encode_review(text))
    print(predictions[np.argmax(predictions)])
    return predictions[np.argmax(predictions)]
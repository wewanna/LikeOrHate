import tensorflow as tf
import numpy as np
import pickle
from tensorflow import keras
import matplotlib.pyplot as plt

label_list = []
value_list = []

with open('train_labels.dataset', 'rb') as f:
    data = pickle.load(f)
    label_list = data

with open('train_data.dataset', 'rb') as f:
    data = pickle.load(f)
    value_list = data

print(label_list)
print(value_list)


vocab_size = 100

model = keras.Sequential()
model.add(keras.layers.Dense(64, activation=tf.nn.relu, input_shape=(100,)))
model.add(keras.layers.Dense(128, activation=tf.nn.relu))
model.add(keras.layers.Dense(1, activation=tf.nn.sigmoid))

model.summary()

model.compile(optimizer=tf.train.AdamOptimizer(),
              loss='binary_crossentropy',
              metrics=['acc'])

x_val = value_list[:100]
partial_x_train = value_list[100:]

y_val = label_list[:100]
partial_y_train = label_list[100:]

print(x_val)
print(partial_x_train)
print(y_val)
print(partial_y_train)


history = model.fit(partial_x_train,
                    partial_y_train,
                    epochs=100,
                    batch_size=1024,
                    validation_data=(x_val, y_val),
                    verbose=1)


results = model.evaluate(value_list, label_list)

print(results)


history_dict = history.history
history_dict.keys()


acc = history_dict['acc']
val_acc = history_dict['val_acc']
loss = history_dict['loss']
val_loss = history_dict['val_loss']

epochs = range(1, len(acc) + 1)

# "bo"는 "파란색 점"입니다
plt.plot(epochs, loss, 'bo', label='Training loss')
# b는 "파란 실선"입니다
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.show()


plt.clf()   # 그림을 초기화합니다

plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()

plt.show()

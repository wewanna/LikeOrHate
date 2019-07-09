import pickle

with open('train_data.dataset', 'rb') as f:
    data = pickle.load(f)
    print(data)
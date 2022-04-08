import pickle
fileobj = open("Batch.pkl", 'rb')
print(pickle.load(fileobj))

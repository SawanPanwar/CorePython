import pickle
c = ["viaksh", "shivani", "mohit", "tina"]
fileobj = open("Batch.pkl", 'wb')
pickle.dump(c, fileobj)
fileobj.close()
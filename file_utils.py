import os
import pickle

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def save_to_pickle(file_name, object):
    with open(file_name, 'wb') as f:
        pickle.dump(object, f, protocol=pickle.HIGHEST_PROTOCOL)

def read_from_pickle(file_name):
    with open(file_name, 'rb') as f:
        return pickle.load(f)

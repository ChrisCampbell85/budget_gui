import pickle

def pickle_expenses(data, filename, frame=None):
    save_file = open(f'{filename}.pkl', 'wb')
    pickle.dump(data, save_file)
    save_file.close()
    if frame:
        frame.destroy()

def unpickle_expenses(filename):
    file_ = open(filename, 'rb')
    read_file = pickle.load(file_)
    file_.close()
    return read_file


    
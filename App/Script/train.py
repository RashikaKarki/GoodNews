import pickle

def train_using_logistic_regression(data):
    LR =  pickle.load(open("Model/logistic_regression.pkl", "rb"))
    return LR.predict(data)
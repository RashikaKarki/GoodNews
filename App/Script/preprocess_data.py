import pandas as pd
# Removing Punctuations and converting all word to lowercase
import string
import nltk
import spacy
import pickle
import re 

def remove_nonwords(str_):
    return re.sub("[^A-Za-z ]\w+[^A-Za-z]*", ' ', str_)

# Lemmatization and Removing stop words and non words
def text_preprocessing(text):
    nlp = spacy.load("en_core_web_sm")
    text = remove_nonwords(text)
    tokenized_text = [token.lemma_ for token in nlp(text)]
    no_stopwords_list = [i.lower() for i in tokenized_text if i not in nlp.Defaults.stop_words]
    lemma_text = ' '.join(no_stopwords_list)
    return lemma_text

def remove_punctuation(text):
    no_punctuation_text = ''.join([i for i in str(text) if i not in string.punctuation])
    return no_punctuation_text.lower()

def clean_data(data):
    edit_data = pd.Series(data).apply(remove_punctuation)
    edit_data = edit_data.apply(text_preprocessing)
    edit_data = vectorize_data(edit_data)
    return edit_data

def vectorize_data(data):
    vectorizer =  pickle.load(open("Model/vectorizer.pkl", "rb"))
    chi_selector =  pickle.load(open("Model/chi_selector.pkl", "rb"))
    data = vectorizer.transform(data)
    data = chi_selector.transform(data)
    return data
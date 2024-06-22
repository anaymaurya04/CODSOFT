import random
import json
import numpy as np
import pickle
import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD

lematizer= WordNetLemmatizer()
with open('AI ChatBot/intents.json', 'r') as file:
    intents = json.load(file)

words=[]
classes=[]
documents=[]
ignore=['?','!','.',","]
for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list= nltk.word_tokenize(pattern)
        words.extend(word_list)
        documents.append((word_list,intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])
words = [lematizer.lemmatize(word) for word in words if word not in ignore]
words =sorted(set(words))
classes = sorted(set(classes))
pickle.dump(words,open('words.pkl','wb'))
pickle.dump(words,open('classes.pkl','wb'))
training=[]
output_empty=[]
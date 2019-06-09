from collections import Counter
import os
import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn import svm
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split


def main_model():
    data = pd.read_csv(('training_data.tsv'), header=0, delimiter="\t", quoting=3)

    # drops the nan values
    data.dropna(inplace=True)
    data.reset_index(drop=True, inplace=True)  # resetting the index because dropna doesnot change the index

    # if the phrase is found replace it with the phrases with 'Found' label
    data.loc[data['label'] != 'Not Found', 'label'] = 'Found'

    # generating random training set and test set
    X = data['sent']
    y = data['label']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.02, random_state=0)

    clean_train_data = []
    # preparing the data for count vectorizer
    print("Cleaning and parsing the training data...\n")
    for i in (X_train):
        clean_train_data.append(i)

    # Creating a bag of words from the training set
    print("Creating the bag of words...\n")

    # initializing the count vectorizer to represent bag of words tool.
    vectorizer = CountVectorizer(ngram_range=(1, 2))  # n-grams Bag of word
    train_data_features = vectorizer.fit_transform(clean_train_data)  # expects a list of strings
    np.asarray(train_data_features)  # Tfidf expects an array hence we convert it

    # representing the n-grams wrt to the frequency of occurrence
    tfidf_transformer = TfidfTransformer()
    X_train_tfidf = tfidf_transformer.fit_transform(train_data_features)

    # training the stochastic gradient descent model
    clf = svm.LinearSVC(loss='hinge').fit(X_train_tfidf, y_train)

    import pickle
    file = open('my_classifier.pickle', 'wb')
    pickle.dump(clf, file)
    file.close()

    file = open('my_vectorizer.pickle', 'wb')
    pickle.dump(vectorizer, file)
    file.close()
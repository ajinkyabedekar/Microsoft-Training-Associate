import os
import pickle
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

# regex generation
import generator
training_data_tsv_path = os.getcwd()+'/training_data.tsv'
eval_data_path = os.getcwd()+'/eval_data.txt'
generator.main_generator(training_data_tsv_path)

# regex extraction
import matcher
print('inside_extraction....This might take a while')
extractions_from_regex = matcher.main_matcher(eval_data_path)
print('extracted')

# training the Machine Learning model
import training_classifier
# gets trained classifier model
training_classifier.main_model()
f = open('my_classifier.pickle', 'rb')
clf = pickle.load(f)
f.close()

# geting the vectorizer
f = open('my_vectorizer.pickle', 'rb')
vectorizer = pickle.load(f)
f.close()

# loads the data
data = []
master_data = open(eval_data_path, 'r')
for sent in master_data:
    data.append(' '.join(sent.split()))  # to remove the \n from the txt file
df = pd.DataFrame(data)  # loads the data to the dataFrame
df = df[0]  # getting the dimensions right for prediction

clean_test_data = []
for i in df:
    clean_test_data.append(i)
# print (clean_train_data)

# taking a bag of words for the test set, and converting it to a numpy array
test_data_features = vectorizer.transform(clean_test_data)
np.asarray(test_data_features)

tfidf_transformer = TfidfTransformer()
X_test_tfidf = tfidf_transformer.fit_transform(test_data_features)

# predicting from the classifier
result = clf.predict(X_test_tfidf)

# saving the result in a dataFrame
output = pd.DataFrame(data={"sent": df, "label": result})
predicted_result = list(result)  # converting the n dimensional array into a list
output.to_csv('Bag_of_Words_model_new.csv', index=False, quoting=3, escapechar='\\')

# final submission
final_result = []
for idx, prediction in enumerate(predicted_result):
    if prediction == 'Not Found':
        final_result.append('Not Found')
    else:
        final_result.append(extractions_from_regex[idx])
# loading the final output into df
final_output = pd.DataFrame(data={"sent": df, "label": final_result})
final_output.to_csv('submission.csv', index=False, quoting=3, escapechar='\\')
print("submission done")

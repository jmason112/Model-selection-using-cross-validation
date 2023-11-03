#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.feature_selection import SelectKBest, SelectPercentile, chi2, mutual_info_classif
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import BernoulliNB
from sklearn import pipeline
import matplotlib.pyplot as plt

# Read the data from the reduceddataset.csv file
data = pd.read_csv('reduceddataset.csv')

# Extract the features only by dropping the MD5 hash, label, and target columns
features_only = data.drop(['MD5', 'label', 'Target'], axis=1)

# Extract the target column
target = data['Target']

# Perform StratifiedKFold to split the data into 10 folds
skf = StratifiedKFold(n_splits=10)
for train_index, test_index in skf.split(features_only, target):
    X_train, X_test = features_only.iloc[train_index], features_only.iloc[test_index]
    y_train, y_test = target.iloc[train_index], target.iloc[test_index]

# Declare two lists, one to store the name of the method used and the second to store the selected features
titles = []
cases = []

# Perform SelectKBest Chi2 selection and append the results to the lists
titles.append("SelectKBest Chi2")
selector = SelectKBest(chi2, k=15)
selector.fit(X_train, y_train)
cases.append(selector)

# Perform SelectKBest Mutual info selection and append the results to the lists
titles.append("SelectKBest Mutual info")
selector = SelectKBest(mutual_info_classif, k=15)
selector.fit(X_train, y_train)
cases.append(selector)

# Perform SelectPercentile Mutual info selection and append the results to the lists
titles.append("SelectPercentile Mutual info")
selector = SelectPercentile(mutual_info_classif, percentile=15)
selector.fit(X_train, y_train)
cases.append(selector)

# Create a for loop to run each model using your pipeline, and calculate the scores using cross_val_score
models = [DecisionTreeClassifier(), RandomForestClassifier(), SVC(kernel="linear"), BernoulliNB()]
scores = []
for i in range(len(cases)):
    for model in models:
        pipe = pipeline.Pipeline([('selector', cases[i]), ('classifier', model)])
        score = cross_val_score(pipe, X_train, y_train, cv=skf)
        scores.append(score)

# Print the scores and use numpy to calculate the mean and std of the scores
for i in range(len(titles)):
    print(f"Method: {titles[i]}, Mean score: {np.mean(scores[i*4:(i+1)*4])}, Standard deviation: {np.std(scores[i*4:(i+1)*4])}")

# Create a boxplot to display and compare the scores
plt.boxplot(scores, labels=titles*4)
plt.title('Comparison of Classification Algorithms')
plt.xlabel('Feature Selection Method')
plt.ylabel('Accuracy')
plt.show()

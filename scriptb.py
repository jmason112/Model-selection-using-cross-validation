#!/usr/bin/env python3

import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.feature_selection import SelectKBest, SelectPercentile, chi2, mutual_info_classif
from sklearn.svm import SVC
from sklearn import pipeline
from sklearn.metrics import make_scorer, f1_score

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

# Declare two lists, one to store the name of the method used and second to store the selected features
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

# Send the lists to the SVC classifier model
clf = SVC(kernel="linear")

# Use a for loop to call the cross_val_score function with the pipeline and the k-fold object
for i in range(len(cases)):
    pipe = pipeline.Pipeline([('selector', cases[i]), ('classifier', clf)])
    scores = cross_val_score(pipe, X_train, y_train, cv=skf, scoring=make_scorer(f1_score))

    # Use numpy to calculate the mean and standard deviation of the F1 score
    mean_score = np.mean(scores)
    std_dev = np.std(scores)

    # Print the mean and standard deviation of the F1 score
    print(f"Method: {titles[i]}, Mean F1 score: {mean_score}, Standard deviation: {std_dev}")

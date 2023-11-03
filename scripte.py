#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.svm import SVC
import pickle

# Load the data from reduceddataset.csv into a data frame object
data = pd.read_csv('reduceddataset.csv')

# Read the label "target" where 0 is benignware and 1 is malware
target = data['Target']

# Extract the features only by dropping the MD5 hash, label, and target columns
features_only = data.drop(['MD5', 'label', 'Target'], axis=1)

# Perform feature selection using SelectKBest and chi2 with k=15
selector = SelectKBest(chi2, k=15)
selector.fit(features_only, target)
selected_features = features_only.columns[selector.get_support(indices=True)]

# Train the classifier using SVC with a linear kernel
classifier = SVC(kernel='linear')
classifier.fit(features_only[selected_features], target)

# Persist the SVC model in a file called saved_detector.pkl
with open("saved_detector.pkl", "wb") as f:
    pickle.dump((classifier, selected_features), f)

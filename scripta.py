#!/usr/bin/env python3

import pandas as pd

# Read the data from the dataset.csv file
data = pd.read_csv('dataset.csv')

# Obtain 30 random samples of benignware which is "0"
benignware_samples = data[data['Target'] == 0].sample(n=30)

# Obtain 30 random samples of malware which is "1"
malware_samples = data[data['Target'] == 1].sample(n=30)

# Combine the benignware and malware samples
combined_samples = pd.concat([benignware_samples, malware_samples])

# Remove the selected samples from the original data frame
reduced_data = data.drop(combined_samples.index)

# Write the reduced data to a new CSV file named "reduceddataset.csv"
reduced_data.to_csv("reduceddataset.csv", index=False)

# Write the MD5 hash and label columns of the selected samples to a new CSV file named "samples.csv"
selected_samples = combined_samples[['MD5', 'label']]
selected_samples.to_csv("samples.csv", index=False)

# Print the combined samples and the reduced data
print("Combined samples:")
print(combined_samples)
print("\nReduced data:")
print(reduced_data)

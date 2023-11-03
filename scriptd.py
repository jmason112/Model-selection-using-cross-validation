#!/usr/bin/env python3

import os
import hashlib
import pandas as pd
import shutil

def md5_hash(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
        md5 = hashlib.md5(data).hexdigest()
    return md5

# Read the samples.csv file
samples = pd.read_csv('samples.csv')

# Define the folder paths for the benignware and malware samples
folder_path_benignware = '/home/osboxes/Downloads/malware_data_science/ch8/data/benignware/'
folder_path_malware = '/home/osboxes/Downloads/malware_data_science/ch8/data/malware/'

# Define the folder path for the samples folder
folder_path_samples = 'samples/'

# Create the samples folder if it does not exist
if not os.path.exists(folder_path_samples):
    os.makedirs(folder_path_samples)

# Scan each file in the benignware and malware folders
for folder_path in [folder_path_benignware, folder_path_malware]:
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                # Generate the md5 hash of the file
                md5 = md5_hash(file_path)
                
                # Check if the file's md5 hash is in the samples.csv file
                if md5 in samples['MD5'].values:
                    # Copy the file to the samples folder
                    shutil.copy(file_path, folder_path_samples)
                    print(f'Copied file {file_path} to {folder_path_samples}')
            except Exception as e:
                print(f'Error processing file: {file_path}')
                print(e)

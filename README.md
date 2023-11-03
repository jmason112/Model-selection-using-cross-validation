<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
</head>
<body>
<h1>Project Documentation: Model Selection Using Cross-Validation</h1>
<p>This project includes scripts for model selection using cross-validation techniques. The scripts are designed to handle dataset sampling, model training, evaluation, and comparison of different models.</p>

<h2>Script A: Data Sampling</h2>
<p><code>scripta.py</code> is responsible for creating a reduced dataset by sampling from the original dataset and segregating samples for further analysis.</p>

<h3>Dependencies</h3>
<p>The script requires the following Python library:</p>
<ul>
<li>pandas</li>
</ul>

<h3>Usage</h3>
<p>Ensure that the dataset is available as <code>dataset.csv</code> in the working directory. Run the script using the command:</p>
<pre><code>python scripta.py</code></pre>

<h3>Functionality</h3>
<p>The script performs the following operations:</p>
<ol>
<li>Reads the entire dataset.</li>
<li>Selects a fixed number of samples for benignware and malware.</li>
<li>Creates a new dataset excluding the selected samples.</li>
<li>Saves the reduced dataset and the selected samples into separate CSV files.</li>
</ol>

<h3>Expected Outputs</h3>
<p>The script will output two CSV files: <code>reduceddataset.csv</code> for the reduced dataset and <code>samples.csv</code> for the selected samples. It also prints the combined samples and the reduced dataset to the console.</p>

<h2>Script B: Feature Selection and Cross-Validation</h2>
<p><code>scriptb.py</code> applies feature selection methods and evaluates models using StratifiedKFold cross-validation.</p>

<h3>Dependencies</h3>
<p>The script requires the following Python libraries:</p>
<ul>
<li>numpy</li>
<li>pandas</li>
<li>sklearn</li>
</ul>

<h3>Usage</h3>
<p>Ensure that the reduced dataset is available as <code>reduceddataset.csv</code> in the working directory. Run the script using the command:</p>
<pre><code>python scriptb.py</code></pre>

<h3>Functionality</h3>
<p>The script performs the following operations:</p>
<ol>
<li>Reads the reduced dataset.</li>
<li>Separates features and target variables.</li>
<li>Splits the data into folds for cross-validation.</li>
<li>Uses feature selection methods and SVM for classification.</li>
<li>Evaluates the model using cross-validation and computes the F1 score.</li>
</ol>

<h3>Expected Outputs</h3>
<p>The script outputs the F1 scores for each fold and may include other evaluation metrics as well.</p>

<h2>Script C: Cross-Validation with Multiple Models</h2>
<p><code>scriptc.py</code> evaluates multiple machine learning models using cross-validation to determine their performance on the dataset.</p>

<h3>Dependencies</h3>
<p>The script requires the following Python libraries:</p>
<ul>
<li>pandas</li>
<li>numpy</li>
<li>sklearn</li>
<li>matplotlib (for potential visualization)</li>
</ul>

<h3>Usage</h3>
<p>Ensure that the reduced dataset is available as <code>reduceddataset.csv</code> in the working directory. Run the script using the command:</p>
<pre><code>python scriptc.py</code></pre>

<h3>Functionality</h3>
<p>The script performs the following operations:</p>
<ol>
<li>Reads the reduced dataset.</li>
<li>Separates features and target variables.</li>
<li>Splits the data into folds for cross-validation.</li>
<li>Evaluates different models: SVM, Decision Tree, Random Forest, and Bernoulli Naive Bayes.</li>
<li>Compares the performance of each model using cross-validation.</li>
</ol>

<h3>Expected Outputs</h3>
<p>The script outputs the cross-validation scores for each model to assess their performance.</p>


<h2>Script D: File Hashing and Organization</h2>
<p><code>scriptd.py</code> handles the organization of sample files by calculating their MD5 hashes and potentially relocating them for analysis.</p>

<h3>Dependencies</h3>
<p>The script requires the following Python libraries:</p>
<ul>
<li>os (for directory operations)</li>
<li>hashlib (for MD5 hash calculation)</li>
<li>pandas (for reading CSV files)</li>
</ul>

<h3>Usage</h3>
<p>Ensure that the sample file list is available as <code>samples.csv</code> and the directories for benignware and malware are correctly set up. Run the script using the command:</p>
<pre><code>python scriptd.py</code></pre>

<h3>Functionality</h3>
<p>The script performs the following operations:</p>
<ol>
<li>Calculates MD5 hashes of files.</li>
<li>Reads the list of sample files to be organized.</li>
<li>Checks and creates a directory for storing organized samples.</li>
<li>Scans and matches files in the benignware and malware directories with the sample list.</li>
<li>May perform file operations such as moving or copying based on matches.</li>
</ol>

<h3>Expected Outputs</h3>
<p>The script may output a status report of file operations and will organize the sample files into the specified directory.</p>

<h2>Script E: Feature Selection and Model Training</h2>
<p><code>scripte.py</code> focuses on selecting the most influential features and training a machine learning model.</p>

<h3>Dependencies</h3>
<p>The script requires the following Python libraries:</p>
<ul>
<li>pandas</li>
<li>numpy</li>
<li>sklearn</li>
<li>pickle (for model serialization)</li>
</ul>

<h3>Usage</h3>
<p>Ensure that the reduced dataset is available as <code>reduceddataset.csv</code> in the working directory. Run the script using the command:</p>
<pre><code>python scripte.py</code></pre>

<h3>Functionality</h3>
<p>The script performs the following operations:</p>
<ol>
<li>Loads the dataset and prepares the features and target.</li>
<li>Applies feature selection to identify the most significant features.</li>
<li>Trains an SVM classifier on the selected features.</li>
<li>Saves the trained model to a file for later use.</li>
</ol>

<h3>Expected Outputs</h3>
<p>The script will save the trained classifier as <code>saved_detector.pkl</code>, which can be loaded for future predictions.</p>

<h2>Script F: Performance Evaluation</h2>
<p><code>scriptf.py</code> assesses the performance of a classification model by generating a classification report and confusion matrix.</p>

<h3>Dependencies</h3>
<p>The script requires the following Python libraries:</p>
<ul>
<li>pandas</li>
<li>numpy</li>
<li>json (for handling JSON data)</li>
<li>sklearn (for metrics and performance evaluation)</li>
<li>matplotlib (for visualization)</li>
</ul>

<h3>Usage</h3>
<p>Ensure that the sample data is available as <code>samples.csv</code> and the log file <code>detector.log</code> is present. Run the script using the command:</p>
<pre><code>python scriptf.py</code></pre>

<h3>Functionality</h3>
<p>The script performs the following operations:</p>
<ol>
<li>Loads the sample data and processes labels.</li>
<li>Reads prediction logs and processes them into a prediction vector.</li>
<li>Calculates performance metrics such as precision, recall, and F1-score.</li>
<li>Outputs a classification report and confusion matrix.</li>
</ol>

<h3>Expected Outputs</h3>
<p>The script will print the classification report and confusion matrix to the console, providing an evaluation of the classifier's performance.</p>

</body>
</html>

# Document retrieval system using python and flask.

Here is a brief description for the code provided, including the steps to install each module I had imported in my code and the purpose why they are imported in the code:

## Importing Modules

Here are the steps to install the modules I had used in my code:

* Open a terminal window.
* Navigate to the directory where you want to install the modules.
* Run the following commands:
``` bash
pip install flask
pip install nltk
pip install sklearn
```
## once i had installed them i had imported the following specific modules:
from flask import Flask, render_template, request
import os
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

## Purpose of Importing these modules were:

* Flask:
  
Flask is a microframework for Python that makes it easy to create web applications. It provides a number of features that are useful for My document retrieval systems, such as routing, templates, and request handling.

* render_template:
  
The render_template() function from the Flask framework is used to render a template file. This is useful for displaying the results of document retrieval query to the user.

* request:
  
The request object from the Flask framework is used to get the query parameters from the user. This is useful for getting the query string from the user so that it can be used to search for documents.

* os:
  
The os module provides functions for interacting with the operating system. This is useful for tasks such as reading and writing files, and creating directories.

* nltk:
  
The nltk module provides functions for natural language preprocessing. This is useful for tasks such as tokenizing text, removing stop words, and stemming words.

* stopwords:
  
The stopwords module from the nltk library provides a list of stop words. Stop words are common words that do not add much meaning to a document, such as "the", "and",  "of", etc ..., Removing stop words can improve the performance of a document retrieval system by reducing the number of irrelevant documents that are returned.

* TfidfVectorizer:
  
The TfidfVectorizer class from the sklearn.feature_extraction.text module is used to create a TF-IDF vectorizer. TF-IDF stands for term frequency-inverse document frequency. It is a statistical measure that is used to calculate the importance of a word in the document. The TF-IDF vectorizer is used to create a vector representation of each document in the file_collection. This vector representation can then be used to calculate the similarity between the documents.

* cosine_similarity:

  The cosine_similarity() function from the sklearn.metrics.pairwise module is used to calculate the cosine similarity between two vectors. The cosine similarity is a measure of the similarity between two vectors. It is calculated by taking the dot product of the two vectors and dividing it by the product of their norms.


## description of The Code

The code I had provided implements a simple document search engine. It first indexes a collection of documents by reading them from a directory named ../IR_PROJECT/file_collection/ and storing them in a dictionary. The documents are then preprocessed by removing stop words and converting all words to lowercase. Finally, queries are processed by first preprocessing the query and then using TF-IDF to calculate the similarity between the query and each document in the collection. The documents are then ranked by their similarity scores and the top results are returned. means the documments are returned descending order of thier similarity scores.

## The following are the key steps in the code:

* Indexing the documents:
  
  The documents are first indexed by reading them from a "../IR_PROJECT/file_collection/" and storing them in a dictionary. The dictionary maps the filename of each document to its content.

* Preprocessing the documents:
  
The documents are then preprocessed by removing stop words and converting all words to lowercase. Stop words are common words that do not add much meaning to the documents, such as "the", "and", and "of". Converting all words to lowercase ensures that words with different capitalizations are treated as the same word.

* Processing the queries:
  
The queries are processed by first preprocessing the query and then using TF-IDF to calculate the similarity between the query and each document in the collection. TF-IDF is a statistical measure that calculates the importance of a word in our document. The similarity between two documents is calculated by taking the cosine of the angle between their TF-IDF vectors.

* Ranking the results:
  
    The documents are then ranked by their similarity scores and the top results are returned.

MY code also includes a function to highlight  (on `index.html`) the exact match of query in our file content. This is done by replacing each word in the file content that matches the query with a marked span.

## Authors :black_nib:

* __SAMUELL ABERRA__ <[samkiyya](https://github.com/samkiyya)>

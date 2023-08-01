from flask import Flask, render_template, request
import os
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__)

# Step 1: Indexing the Documents
documents = []
document_dir = '../IR_Project/file_collection/'
for filename in os.listdir(document_dir):
    if filename.endswith('.txt'):
        with open(os.path.join(document_dir, filename), 'r') as file:
            content = file.read()
            documents.append({
                'title': filename,
                'content': content
            })

# Step 2: Preprocessing the Documents
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    tokens = nltk.word_tokenize(text)
    tokens = [token.lower() for token in tokens if token.isalpha()]
    tokens = [token for token in tokens if token not in stop_words]
    return ' '.join(tokens)

preprocessed_documents = {
    doc['title']: preprocess_text(doc['content'])
    for doc in documents
}

# Step 3: Processing the Queries
def process_query(query):
    preprocessed_query = preprocess_text(query)
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(list(preprocessed_documents.values()))
    query_vector = tfidf_vectorizer.transform([preprocessed_query])
    similarities = cosine_similarity(query_vector, tfidf_matrix)
    relevance_scores = similarities[0]
    ranked_indices = relevance_scores.argsort()[::-1]  # Get indices in descending order of relevance

    ranked_documents = [
        (documents[idx]['title'], relevance_scores[idx])
        for idx in ranked_indices
        if relevance_scores[idx] != 0  # Exclude documents with relevance score of 0
    ]

    return ranked_documents
# highlight the exact match of query in content
def highlight_text(text, query):
    highlighted_text = text
    query_tokens = nltk.word_tokenize(query.lower())

    for token in query_tokens:
        highlighted_text = highlighted_text.replace(token, f'<span class="marked">{token}</span>')

    return highlighted_text
@app.route('/read/<filename>')
def read_document(filename):
    for doc in documents:
        if doc['title'] == filename:
            content = doc['content']
            preprocessed_content = preprocess_text(content)
            query = request.args.get('query')
            if query:
                highlighted_content = highlight_text(preprocessed_content, query)
            else:
                highlighted_content = content

            return render_template('read.html', title=filename, content=highlighted_content)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        query = request.form['query']
        results = process_query(query)

        if len(results) == 0:
            result = "No documents found matching the query."
        else:
            result = []
            for doc_title, relevance_score in results:
                document = next((doc for doc in documents if doc['title'] == doc_title), None)
                if document:
                    content = document['content']
                    lines = content.split('\n')[:5]  # Retrieve up to 5 lines of content
                    preprocessed_content = preprocess_text('\n'.join(lines))
                    highlighted_content = highlight_text(preprocessed_content, query)
                    result.append((doc_title, f'{relevance_score:.4f}', highlighted_content))

        return render_template('index.html', result=result)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run()

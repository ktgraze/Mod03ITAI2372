# import libraries
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from flask import Flask, render_template, request
import os

# Dataset (manually generated)
symptom_database = {
    "headache fever": ("Possible flu", "non-urgent"),
    "chest pain breathing difficulty": ("Heart issue", "emergency"),
    "cough sore throat": ("Cold/Allergies", "non-urgent"),
    "runny nose sneezing": ("Flu/Cold", "non-urgent"),
    "fatigue tiredness": ("Fatigue - Could be sleep debt or low energy", "non-urgent")
}

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def process_symptoms(text):
    # Tokenize the text
    tokens = word_tokenize(text)

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [w for w in tokens if not w.lower() in stop_words]

    # Lemmatize the tokens
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(w) for w in filtered_tokens]

    return lemmatized_tokens

def analyze_symptoms(symptoms):
    processed_symptoms = process_symptoms(symptoms)

    best_match = None
    highest_similarity = 0

    for phrase, (diagnosis, triage) in symptom_database.items():
        similarity = sum(1 for word in processed_symptoms if word in phrase.split())

        if similarity > highest_similarity:
            highest_similarity = similarity
            best_match = (diagnosis, triage)

    if best_match:
        return best_match
    else:
        return ("Could not determine a likely condition. Please consult a doctor.", "non-urgent")

# Define the path to the templates directory
template_dir = os.path.abspath('/Users/ktgraze/Projects/Mod03ITAI2372/env/templates')

app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def index():
    return render_template('indexv3.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    user_symptoms = request.form['symptoms']
    diagnosis, triage_level = analyze_symptoms(user_symptoms)
    return render_template('result.html', diagnosis=diagnosis, triage_level=triage_level)

if __name__ == '__main__':
    app.run(debug=True)
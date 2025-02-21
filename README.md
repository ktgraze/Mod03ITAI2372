Following along with the Module 03 weekend project assignment aid, I created the setup and environment using Visual Studio Code, along with the help of GitHub Copilot. After some trial and error, as this was my first time working with Flask, I managed to create a simple Flask app webpage. I ran into trouble rendering the HTML code for the `results.html` page, but did manage to get the home page/ index (`indexv3.html`) to render (example below).


<img width="843" alt="Screenshot 2025-02-20 at 3 27 49 PM" src="https://github.com/user-attachments/assets/e21e9134-a2a3-4c6a-bd21-b117a545b642" />

# Symptom Checker

This project is a simple symptom checker web application built using Flask and NLTK. It allows users to input their symptoms and receive a possible diagnosis and triage level.

## Project Structure

- `Symptom_Checker.py`: The main application file.
- `env/`: The virtual environment directory.
- `env/templates/`: The directory containing HTML templates.
- `env/nltk_data/`: The directory containing NLTK data.

## Setup Instructions

### 1. Clone the Repository

Clone the project repository to your local machine.

```sh
git clone <repository_url>
cd <repository_directory>
```

### 2. Set up Virtual Environment

Create a virtual environment:
`python -m venv env`

Activate the virtual environment:
- On Windows:
`.\env\Scripts\activate`
- On macOS/Linux:
  `source env/bin/activate`

### 3. Install Dependencies
Install the required packages using `requirements.txt`:
`pip install -r requirements.txt`

### 4. Download NLTK Data
Ensure the necessary NLTK data is downloaded. This is already handled in `Symptom_Checker.py` with:
```sh
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
```
### 5. Run the Application
Run the Flask Application:
`python Symptom_Checker.py`

#### Usage:
1. Open your web browser and navigate to [http://127.0.0.1:5000/].
2. Enter your symptoms in the input field and submit the form.
3. View the diagnosis and triage level on the result page.

##### Disclaimer:
This project is a simple symptom checker web application built using Flask and NLTK. It allows users to input their symptoms and receive a possible diagnosis and triage level.


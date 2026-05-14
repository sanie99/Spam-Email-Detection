# Spam-Email-Detection

A simple **Email Spam Detection** project that uses a trained machine learning model to classify an email as **Spam** or **Not Spam**.

The app is deployed as a **Streamlit** web interface and loads the trained models from the `models/` folder.

---

## Features

- Web app UI to paste an email and get a prediction
- Uses a TF-IDF vectorizer + a trained classifier
- Trained model files are included in `models/`

---

## Tech Stack

- **Python**
- **Streamlit** (UI)
- **scikit-learn** (ML models)
- **NLTK** (text processing utilities)
- **pandas** (data handling)

---

## Project Structure

- `app/`
  - `app.py` Streamlit application (loads models and predicts)
- `models/`
  - `tfidf_model.pkl` trained TF-IDF vectorizer
  - `multinomial_model.pkl` trained classifier
- `data/`
  - dataset files used during training
  - (may include `raw/` and `processed/`)
- `notebooks/`
  - Jupyter notebooks for exploration, preprocessing, training, and evaluation

---

## Setup

From the project root:

1. Create a virtual environment (recommended)

```bash
python -m venv .venv
```

2. Activate it

- Windows (cmd):

```bash
.venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Streamlit App

From the project root:

```bash
streamlit run app/app.py
```

Open the URL shown in the terminal and:

1. Paste an email into the text area
2. Click **Predict**
3. See whether the email is classified as **Spam** or **Not Spam**

---

## How Predictions Work (High Level)

The app:

1. Loads `models/tfidf_model.pkl` and `models/multinomial_model.pkl`
2. Converts your input text into TF-IDF features
3. Predicts using the trained classifier

---

## Retraining the Model

If you want to retrain the model, use the notebooks in `notebooks/` (in order):

- `01_data_exploration.ipynb`
- `02_preprocessing.ipynb`
- `03_model_training.ipynb`
- `04_model_evaluation.ipynb`

After training, ensure you save the updated artifacts back to:

- `models/tfidf_model.pkl`
- `models/multinomial_model.pkl`

---

## Requirements

See `requirements.txt` for the exact dependencies.

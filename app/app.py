import streamlit as st
import pickle
import pandas as pd

st.title("Email Spam Detection")
st.write("This application detects whether an email is spam or not using a trained machine learning model.")
st.write("Please enter the email content below:")

 # Load the trained models
tfidf_model = pickle.load(open('models/tfidf_model.pkl', 'rb'))
multinomial_model = pickle.load(open('models/multinomial_model.pkl', 'rb'))

email_content = st.text_area("Email Content")

if st.button("Predict"):
    if email_content:

        # Vectorize the input email content
        email_vectorized = tfidf_model.transform([email_content])

        # Predict using the trained model
        prediction = multinomial_model.predict(email_vectorized)

        # Display the result
        if prediction[0] == 1:
            st.error("This mail is classified as: **Spam**")
        else:
            st.success("This email is classified as: **Not Spam**")
    else:
        st.warning("Please enter the email content to predict.")
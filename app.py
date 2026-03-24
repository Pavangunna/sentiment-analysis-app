import streamlit as st
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load files
model = load_model("sentiment_model.h5")
tokenizer = pickle.load(open("tokenizer.pkl", "rb"))
le = pickle.load(open("label_encoder.pkl", "rb"))

# Prediction function
def predict_sentiment(text):
    seq = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(seq, maxlen=100)
    result = model.predict(padded)
    label = result.argmax()
    return le.inverse_transform([label])[0]

# UI
st.title("Sentiment Analysis App")

user_input = st.text_input("Enter text")

if st.button("Predict"):
    if user_input:
        result = predict_sentiment(user_input)
        st.write("Sentiment:", result)
    else:
        st.write("Please enter text")
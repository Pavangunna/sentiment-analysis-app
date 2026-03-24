import streamlit as st

# Page configuration
st.set_page_config(page_title="Sentiment Analysis App", page_icon="💬")

# Title
st.title("💬 Sentiment Analysis App")
st.write("Enter a sentence to check whether it is Positive, Negative, or Neutral")

# Prediction function (lightweight, no TensorFlow)
def predict_sentiment(text):
    text = text.lower()

    positive_words = ["good", "great", "amazing", "excellent", "love", "awesome", "happy"]
    negative_words = ["bad", "worst", "poor", "hate", "terrible", "awful", "sad"]

    if any(word in text for word in positive_words):
        return "Positive 😊"
    elif any(word in text for word in negative_words):
        return "Negative 😞"
    else:
        return "Neutral 😐"

# User input
user_input = st.text_area("✍️ Enter your text here:")

# Button action
if st.button("🔍 Analyze Sentiment"):
    if user_input.strip() != "":
        result = predict_sentiment(user_input)

        st.subheader("Result:")
        st.success(result)
    else:
        st.warning("⚠️ Please enter some text")

# Footer
st.markdown("---")
st.caption("Built using Streamlit 🚀")
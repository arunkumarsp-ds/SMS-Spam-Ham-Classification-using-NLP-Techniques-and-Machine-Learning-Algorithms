import pickle
import streamlit as st

model = pickle.load(open("nb_spam_model.pkl","rb"))
vectorizer = pickle.load(open("bow_vectorizer.pkl","rb"))

st.title("📩-Spam Detection APP")

user_input = st.text_area("Enter the message to check wheather it is a spam or ham")

if st.button("Predict"):

    if user_input.strip() == "" :
        st.warning("Please Enter your Message For Prediction")
    else:
        vectorized_input =  vectorizer.transform([user_input])

        prediction = model.predict(vectorized_input)[0]

        if prediction == 1:
            result = "Spam"
        else:
            result = "Ham"
            
        st.subheader(f"The Given Message is :{result}")
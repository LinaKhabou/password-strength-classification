import streamlit as st
import pickle
import numpy as np

loaded_model=pickle.load(open("models/model.pkl","rb"))
loaded_vec=pickle.load(open("models/tfidf_vectorizer.pkl","rb"))

def Password_Strength_Prediction(input_data):
    password_vec=loaded_vec.transform([input_data])
    prediction=loaded_model.predict(password_vec)
    return prediction



def main():

    st.title("🔐 Password Strength Prediction")
    st.caption("Enter your password and discover its strength level instantly with the power of Machine Learning.")

    password=st.text_input(
        "Enter your password",
        placeholder="Example: P@ssword123"
    )

    if st.button("🔍 Predict Strength", use_container_width=True, type="primary"):
        if password=="":
            st.warning("Please enter a password first.")
        else :
            pred = Password_Strength_Prediction(password)
            if pred[0]==0:
                st.error("❌ Weak password")
                st.write("Try adding uppercase letters, numbers, and symbols.")

            elif pred[0]==1:
                st.warning("⚠️ Medium password")
                st.write("Your password is acceptable but can be improved.")

            else:
                st.success("✅ Strong password")
                st.write("Great! Your password looks secure.")




if __name__ == "__main__":
    main()
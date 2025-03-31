import streamlit as st
import pickle
import numpy as np

def main():
    # Load the model
    with open('../outputs/models/model_dt.pkl', 'rb') as file:
        model = pickle.load(file)

    st.title("🚢 Titanic Survival Prediction")

    # Input fields for the features
    pclass = st.selectbox("Passenger Class (Pclass)", [1, 2, 3], index=2)
    age = st.number_input("Age", min_value=0.0, max_value=100.0, value=25.0)
    fare = st.number_input("Fare", min_value=0.0, max_value=600.0, value=50.0)

    # Predict button
    if st.button("Predict"):
        features = np.array([[pclass, age, fare]])
        prediction = model.predict(features)

        if prediction[0] == 1:
            st.success("🎉 Survived")
        else:
            st.error("💀 Did not survive")

if __name__ == "__main__":
    main()

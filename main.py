import streamlit as st
import numpy as np
import pandas as pd
from utils import (
    accuracy_and_visualization, 
    train_model,
    model_table
    )


def page_one():

    st.title("User Login")

    UseCaseName = st.text_input("Use Case Name")

    if UseCaseName:
        st.write(f"You Entered: {UseCaseName}")

    col1, col2 = st.columns(2)

    with col1:
        FirstName = st.text_input("First Name")
    
    with col2:
        LastName = st.text_input("Last Name")
    

    with st.container():
        st.write(FirstName ,LastName)

    
    # st.markdown("<br>", unsafe_allow_html = True)

    if 'clicked' not in st.session_state:
        st.session_state.clicked = False

    def click_button():
        st.session_state.clicked = True

    st.button("Next", key="Next Button", on_click = click_button, help="Click to go on next section")

    if st.session_state.clicked:
        st.session_state.page = "page_two"


def page_two():

    st.title("Dataset & Model Parameter")

    st.header("Dataset", divider = "orange")

    st.text_input("Dataset Path:")

    st.header("Model", divider = "orange")
    st.selectbox("Model Type:", ["XGBoost", "Random Forest Classifier", "Logistic Regression"])

    col3, col4, col5 = st.columns(3)

    with col3:
        st.number_input("LR:", min_value = 0.00000001, max_value = 0.00023, step=0.000001)


    if 'clicked' not in st.session_state:
        st.session_state.clicked = False

    def click_button():
        st.session_state.clicked = True

    st.button("Train", key="train_button", on_click = click_button, help="Click to start training the network")

    if st.session_state.clicked:
        st.session_state.page = "page_three"

def page_three():

    st.header("Model Traning", divider = "orange")

    st.subheader("Model Table", divider = "orange")

    with st.container(border = True):
        model_table()

    col1, col2 = st.columns((2,1))
    with col1:
        st.write("MODEL: ")

    with col2:
        train_status = st.radio("Model Training", ["Trained", "Not Trained"])

        if train_status == "Train":
            success = train_model()

            # Change radio button color based on training success
            if success:
                st.markdown('<style>div[data-baseweb="radio"] label {color: green;}</style>', unsafe_allow_html=True)
            else:
                st.markdown('<style>div[data-baseweb="radio"] label {color: red;}</style>', unsafe_allow_html=True)

    accuracy_and_visualization()

    if 'clicked' not in st.session_state:
        st.session_state.clicked = False

    def click_button():
        st.session_state.clicked = True

    st.button("Prediction", key="prediction_button", on_click = click_button, help="Click on button for model predition")

    if st.session_state.clicked:
        st.session_state.page = "page_four"


def page_four():

    def click_button():
        st.session_state.clicked = True

    st.header("Model Prediction", divider = "orange")

    col1, col2 = st.columns((2,1))
    with col1:
        Predition_Data_Path = st.text_input("Prediction Dataset Path:")
    
    with col2:
        st.button("Submit", key="submit_button", help="Click on button to submit dataset")

    if 'clicked' not in st.session_state:
        st.session_state.clicked = False

    st.button("Predict", key="predict_button", on_click = click_button, help="Click on button for getting prediction result")

    if st.session_state.clicked:
        #TODO :- Add functionality for drawing graphs from predction result
        accuracy_and_visualization()



def main():

    st.set_page_config(
        page_title="App",
        layout="centered",
        page_icon=":rocket:",
        initial_sidebar_state="expanded"
    )

    # st.title("Lead Generation")


    if "page" not in st.session_state:
        st.session_state.page = "page_one"

    if st.session_state.page == "page_one":
        page_one()

    elif st.session_state.page == "page_two":
        page_two()
    
    elif st.session_state.page == "page_three":
        page_three()

    elif st.session_state.page == "page_four":
        page_four()



if __name__ == "__main__":
    main()
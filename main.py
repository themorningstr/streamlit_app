import streamlit as st
# from sklearn.metrics import plot_confusion_matrix, plot_roc_curve, plot_precision_recall_curve
import numpy as np
import pandas as pd


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
        parameter = st.number_input("LR:", min_value = 0.00000001, max_value = 0.00023, step=0.000001)


    if 'clicked' not in st.session_state:
        st.session_state.clicked = False

    def click_button():
        st.session_state.clicked = True

    st.button("Train", key="train_button", on_click = click_button, help="Click to start training the network")

    if st.session_state.clicked:
        st.session_state.page = "page_three"

def page_three():

    st.header("Model Traning", divider = "orange")

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

def train_model():
    success = True  
    return success


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


def accuracy_and_visualization():

    with st.container(border = True):
        precision, recall = st.columns(2)

        with precision:
            st.number_input("Precision:")
        
        with recall:
            st.number_input("Recall:")

        f1, accuracy = st.columns(2)

        with f1:
            st.number_input("F1-Score:")
        
        with accuracy:
            st.number_input("Accuracy:")

    with st.container(border = True):
        st.subheader("ROC Curve", divider = "orange")
        # plot_roc_curve(model, x_test, y_test)
        st.bar_chart(np.random.randn(50, 3))
        # st.pyplot()

    with st.container(border = True):
        st.subheader("Confusion Matrix", divider = "orange")
        # plot_confusion_matrix(model, x_test, y_test, display_labels = class_names)
        chart_data = pd.DataFrame(
        {
            "col1": np.random.randn(20),
            "col2": np.random.randn(20),
            "col3": np.random.choice(["A", "B", "C"], 20),
        }
        )

        st.area_chart(chart_data, x="col1", y="col2", color="col3")

        # st.pyplot()

    with st.container(border = True):
        st.subheader("Precision-Recall Curve", divider = "orange")
        # plot_precision_recall_curve(model, x_test, y_test)
        chart_data = pd.DataFrame(
        {
            "col1": np.random.randn(20),
            "col2": np.random.randn(20),
            "col3": np.random.choice(["A", "B", "C"], 20),
        }
        )

        st.line_chart(chart_data, x="col1", y="col2", color="col3")
        # st.pyplot()



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
import streamlit as st
from streamlit.components.v1 import components
# from first import page_one
# from second import page_two


def page_one():

    st.title("Churn Data")

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

    
    st.markdown("<br>", unsafe_allow_html = True)

    if 'clicked' not in st.session_state:
        st.session_state.clicked = False

    def click_button():
        st.session_state.clicked = True

    st.button("Next", key="Next Button",on_click=click_button, help="Click to go on next section")

    if st.session_state.clicked:
        st.session_state.page = "page_two"


def page_two():

    st.header("Dataset", divider = "orange")

    Data_Path = st.text_input("Dataset Path:")

    st.header("Model", divider = "orange")
    Model_type = st.selectbox("Model Type:", ["XGBoost", "Random Forest Classifier", "Logistic Regression"])

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

    st.header("Model Traning")







    if 'clicked' not in st.session_state:
        st.session_state.clicked = False

    def click_button():
        st.session_state.clicked = True

    st.button("Prediction", key="prediction_button", on_click=click_button, help="Click on button for model predition")

    if st.session_state.clicked:
        st.session_state.page = "page_four"


    

def page_four():

    def PredictionResult():

        pass

    st.header("Model Prediction")

    col1, col2 = st.columns((2,1))
    with col1:
        Predition_Data_Path = st.text_input("Prediction Dataset Path:")
    
    with col2:
        submit_button = st.button("Submit", key="submit_button", help="Click on button to submit dataset")
        # st.write("Text submitted:", Predition_Data_Path)
        
        # if col2.button("Submit", use_container_width=True):
        #     st.write("Text submitted:", Predition_Data_Path)



    predict_button = st.button("Predict", key="predict_button", on_click = PredictionResult, help="Click on button for getting prediction result")

   








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
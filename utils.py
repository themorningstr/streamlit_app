import streamlit as st
import numpy as np
import pandas as pd
# from sklearn.metrics import plot_confusion_matrix, plot_roc_curve, plot_precision_recall_curve




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


def train_model():
    success = True  
    return success


def model_table():
    Deploy = []

    data = {
        "Model" : ["M1", "M2", "M3"],
        "TimeStamp" : ["xxx", "yyy", "zzz"]
    }

    df = pd.DataFrame(data)

    for i in range(len(df)):
        Deploy.append(st.radio(f"M{i+1}" , ["Deploy"]))

    df["Deploy"] = Deploy

    st.table(df)

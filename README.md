# SALES PREDICTION APP

## Sales Prediction

This is a Streamlit web application that predicts sales using a machine-learning model trained on a TV advertising sales dataset.

## How It Works

1. The application uses a TV advertising dataset containing:
   - TV Advertising Budget
   - Radio Advertising Budget
   - Newspaper Advertising Budget
   - Sales

2. The trained machine-learning model analyzes the advertising budgets to identify their relationship with product sales.

3. The user enters the advertising budget values through the Streamlit interface.

4. The application processes the input data and passes it to the trained machine-learning model.

5. Streamlit displays the predicted sales based on the entered advertising budgets.

## Main Files

- `app.py` – Contains the Streamlit interface and sales prediction logic.
- `sales_model.pkl` – Stores the trained machine-learning model.
- `requirements.txt` – Lists the required Python packages.

## Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Joblib

## Project Overview

This project demonstrates an end-to-end machine-learning regression workflow, including data preprocessing, exploratory data analysis (EDA), model training, prediction, and deployment using Streamlit.

The application helps estimate product sales based on advertising expenditure across different marketing channels.
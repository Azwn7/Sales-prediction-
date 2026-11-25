import streamlit as st
import pandas as pd
import joblib
model=joblib.load('Tv_sales.pkl')
st.title('TV SALES APP')
st.write('SIUUUU')
tv=st.number_input('TV SALES',min_value=0.0,value=2.0)
if st.button('Predict'):
    input_data=pd.DataFrame({'TV': [tv]})
    prediction=model.predict(input_data)[0]
    predicted_value=prediction.item()
    st.success(f"Predicted : ${predicted_value:,.2f}")
%%writefile app.py
import streamlit as streamlitimport joblib
mpdel = joblib.load('virat')
st.title('Virat Centuries')
input = st.text_input('enter the score and Batting order')
output = model.predict([input])
if st.button('predict'):
  st.title(output[0])         

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

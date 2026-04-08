import streamlit as st

st.header('st.button')

if st.button('Say hello'):
     st.write('Why hello there 12')
else:
     st.write('Goodbye')
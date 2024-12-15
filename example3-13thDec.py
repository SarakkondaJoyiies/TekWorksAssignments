import streamlit as st
st.title("Bill Calculator")
salary=st.number_input("Enter the salary amount:")
sum1=0
bill1=st.number_input("Enter the bill1:")
bill2=st.number_input("Enter the bill2:")
bill3=st.number_input("Enter the bill3:")
sum=bill1+bill2+bill3
if st.button("submit"):
    percent=(sum/salary)*100
    st.success(percent)



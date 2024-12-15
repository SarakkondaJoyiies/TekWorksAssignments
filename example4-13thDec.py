import streamlit as st
st.title("Gross Salary Calculator")
basicsalary=st.number_input("Enter the basic salary:")
if st.button("proceed"):
     if basicsalary<10000:
         hra= (67/100)*basicsalary
         da= (73/100)*basicsalary
     elif basicsalary<20000:
         hra = (69 / 100) * basicsalary
         da = (76 / 100) * basicsalary
     else:
         hra = (73 / 100) * basicsalary
         da = (89 / 100) * basicsalary
     gs = hra + da + basicsalary
     st.subheader(f"The Gross Salary will be: {gs}")
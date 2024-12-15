import streamlit as st
st.title("Score calculator")
projectscore = st.number_input("Enter the project score:")
internalscore =st.number_input("Enter the internal score:")
externalscore=st.number_input("Enter the external score:")
if st.button("submit"):
   if projectscore>=50 and internalscore>=50 and externalscore>=50:
        total_marks=float((0.7*projectscore)+(0.1*internalscore)+(0.2*externalscore))
        st.subheader(total_marks)
        if total_marks>90.0:
           st.write("A grade")
        elif total_marks>80.0:
           st.write("B grade")
        elif total_marks>70.0:
           st.write("C grade")
        else:
           st.write("D grade")
   else:
        if projectscore<50:
           st.write("failed in project with score",projectscore)
        if internalscore<50:
           st.write("failed in internal with score", internalscore)
        if externalscore<50:
           st.write("failed in external with score", externalscore)

import streamlit as st
from openai_helper import get_answer


st.set_page_config(page_title="Student Information", page_icon=":ℹ")

st.markdown("""
        <span style='color:yellow'>Arman Habib, Himel, Sani, Mamun, Tuhin, Rifat, Monir</span> <span style='color:orange'>This are all students name. and if you want to get this information,</span> <span style='color:red'>such as :</span> 
        GPA, Semester, total fees, Pending fees, paid amount status you will get this result via MySQL Database. Thank you so much!
""", unsafe_allow_html=True)

st.subheader("Example Questions :-")
st.write("""
   1) What was Arman Habib's GPA in semester 1?
   2) average gpa in third semester?
   3) how much is Arman Habib's pending fees in the first semester?
   4) how much was Arman Habib's due fees in the first semester?
   5) what is the purpose of a balance sheet?"
""")

st.subheader("ChatGPT and MySQL Student Information: Q&A System")

question = st.text_input("Question:", placeholder="Type your Question here....")

if question:
    answer = get_answer(question)
    st.text("Answer:")
    st.write(answer)
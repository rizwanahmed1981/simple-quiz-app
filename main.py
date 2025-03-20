import streamlit as st
import random
from questions import *


import time
st.title("📑 QUIZ APPLICATION 📑")

if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)

question = st.session_state.current_question

st.subheader(question['question'])

selected_option = st.radio("Choose Your Answer", question["options"], key="answer")

if st.button("Submit answer"):
    if selected_option == question["answer"]:
        st.success("✅ Correct")

    else:
        st.error("❌ Incorrect! The Correct Answer is" + question["answer"])
    
    time.sleep(5)
    st.session_state.current_question = random.choice(questions)
    st.rerun()
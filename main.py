import streamlit as st
import random
from questions import *
import time

st.title("📑 QUIZ APPLICATION 📑")

# Initialize session state variables
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)
if "total_score" not in st.session_state:
    st.session_state.total_score = 0

question = st.session_state.current_question

st.subheader(question['question'])

selected_option = st.radio("Choose Your Answer", question["options"], key="answer")

if st.button("Submit answer"):
    if selected_option == question["answer"]:
        st.session_state.total_score += 5
        st.success(f"✅ Correct! Your Score is {st.session_state.total_score}")
    else:
        st.session_state.total_score -= 3
        st.error(f"❌ Incorrect! The Correct Answer is {question['answer']}. Score is {st.session_state.total_score}")
    time.sleep(2)
    st.session_state.current_question = random.choice(questions)
    st.rerun()

st.success(f"Total Score: {st.session_state.total_score}")
st.write("ℹ️ For every right answer You will get a score of 5 and for every wrong answer the score will be deducted by 3 ℹ️")
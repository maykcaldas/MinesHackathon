import os
import streamlit as st

#import RubricGuide
from prelabTutor import PreLabReport, questions, rubrics

# Streamlit app
st.title("Pre-lab Report Assistant")

# make new container to store scratch
st.write(
    """Hi! I am the Lab Report Assistant for the Lab: Determination of the Molar Mass of an Unknown Acid through Acid-Base Titration. Please upload your lab report and I will guide you through the rubric and help you improve your report. Let me know when you're ready!"""
)

# Get the student name and a student ID in two text inputs side by side
# make these fields required
col1, col2 = st.columns(2)
student_name = col1.text_input("Student Name")
student_id = col2.text_input("Student ID")

# make a dropdown menu with the questions numbers
questionID = st.selectbox("Select a question", list(questions.keys()), index=0)

# Use the questionID to display the question and rubric
st.write(f"Question {questionID}: {questions[questionID]}")
# st.write(f"Rubric: {rubrics[questionID]}")

# make a text input for the student's answer
answer = st.text_area("Enter your answer here")

# make a button to run the tutor
if st.button("Run Tutor"):
    # check if student_name and student_id are not empty
    if not student_name or not student_id:
        st.error("Please enter your name and your ID")
    # check if answer is not empty
    if not answer:
        st.error("Please enter your answer")
    # save a file with the student's name and the questionID and the answer
    filename = f"experiments/{student_name}{student_id}_{questionID}.txt"
    print(filename)
    # check if filename exists, if it does, append a number to the end, if not, create the file
    mode = "w" if not os.path.exists(filename) else "a"
    with open(filename, mode) as f:
        f.write(f"############################################\n")
        f.write(f"Student Name: {student_name}\n")
        f.write(f"Student ID: {student_id}\n")
        f.write(f"Question: {questionID}\n")
        f.write(f"Answer: {answer}\n")
        f.write(f"############################################\n\n")

    # Visual feedback that tutor is running
    feedback_placeholder = st.empty()  # Create an empty placeholder
    feedback_placeholder.write("Running tutor...")  # Display temporary message

    # Running the tutor
    tutor = PreLabReport(questionID=questionID, answer=answer)
    response = tutor.run()

    # Clear the temporary message and display the tutor response
    feedback_placeholder.empty()  # Clear the message
    st.write(response)


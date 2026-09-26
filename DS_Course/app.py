import streamlit as st

st.title('DATA SCIENCE 101')
st.write('welcome to this dedicated course to know everything you need to know before getting into data science ! In this course we will see what is data science, the why behind it, tools and quick look with examples, On your right you can see couple pages, each one is designed for learning one part of data science (DS)')

st.write('first tell me your name ! ')

name = st.text_input('what is your name?')

if name:
    st.write(f'nice to meet you {name}!')
    st.write('''Before you start learning Data Science, lets understand
              'what youre actually getting into.

            Well explore:
            🧠 What Data Science is
            ❓ Why it exists
            📜 Where it came from
            🛠️ Which tools are used and why
            📊 How data is analyzed
            🤖 How Machine Learning fits into the picture

             And throughout the journey, we'll work with one real dataset:

             Advertising → Sales

             By the end, you'll have seen how a Data Scientist can go from raw data to an actual prediction. ''')




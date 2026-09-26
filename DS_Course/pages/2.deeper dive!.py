import streamlit as st

st.title('Data Analysis , ML , DL')

st.header('now what are all these consepts people in data scinece keep talking about?')
st.subheader('''
don't worry about these consepts people use to look smart, its simple! not that simple but simple ! 👻''')

st.write(
    """
    Now that we understand what Data Science is,
    let's look at some of its most important components.

    We will explore:

    - Data Analysis
    - Machine Learning
    - Deep Learning
    - Programming languages
    - Common Data Science tools
    """
)

st.divider()

st.header('Data Analysis !')

st.write('''
 like we take oil to extract gazoline or diesel a data analyst also takes row data to reveal informations, you take
 row data which is 99% of times messy and unreadable! you clean it organize it and start mining for unformations,
 patterns and  relationships, then you communicate the results you found so people can make a better decisions''')
st.write('''
so..Data Analysis is the process of examining data to understand what happened, what is happening, and why.''')
st.write('in the process we will have : ')
st.markdown('''
Raw Data
   ↓
Clean the Data
   ↓
Explore the Data
   ↓
Find Patterns
   ↓
Visualize
   ↓
Interpret Results
   ↓
Make Decisions
''')

st.subheader('A simple example :')

st.write('imagine your company has : ')

st.code('''
TV advertising
Radio advertising
Newspaper advertising
Sales
''')

st.write(' A data analyst might ask : ')
st.markdown('''
How much are we spending on advertising?
Which channel is associated with higher sales?
Are sales increasing or decreasing?
Are there unusual values?
Are some variables related to each other?
What patterns can we find in the data?
''')
st.divider()

st.header('MACHINE LEARNING (ML)')

st.write('''
think about how you learn in school.. a professor gives you knowledge and it keeps teaching you until the knowledge finish or the time runsout
then the teacher makes a test for you, if you passed it means you learned, if you failed it means you did not learn enough
in a way that make professor trust your answers ! ''')

st.write('''
well..Machine learning is the same we give the machine data and it uses math( this math called models) and it learns about the data
it captures the patterns or the segments of the data, after that the machine will be tested by trying to make a predictions.
the better the results the more we trust the model to predict future outcomes ! ''')

st.subheader('imagine we have :')
st.code('''
TV advertising    Radio    Newspaper    Sales
230.1             37.8     69.2         22.1
44.5              39.3     45.1         10.4
17.2              45.9     69.3         12.0
...
''')

st.write('''
We give the machine many examples.

It tries to learn the relationship between:
''')
st.markdown('Advertising spending → Sales')

st.write('then, if we give it a new situation : ')
st.code('''
TV = 200
Radio = 30
Newspaper = 40''')
st.write('the model can make predictions : ')
st.markdown('Predicted Sales = ?')
st.subheader('that is machine learning')

st.write(''' what makes it diffrent from traditional programming is that you don't have to write all the specific rules
the machine will learn new things by its own. ''')
st.divider()
st.header('The three categories of ML')

st.subheader('Supervised Learning')
st.write('''
you take the sells data it has the variable we want to predict (sales) so you teach the model to predict sales based on 
other variables (tv, radio,...) when you have the main variable (often called target variable) its supervised''')

st.subheader('Unsupervised Learning')
st.write('''
unlike the supervised we don't have the target variable you just have data and the model try to divide them to groupes
let's say you have data of diffrent ages from 1 to 100 years old, if you give the data to unsupervised model it will group them
into categories of infants, teenagers, young, kohol and so.....''')

st.subheader('Reinforcement Learning')

st.write('''
it is the closets to how human learn,there is no data, for example you throw a robot in a room and tell him he has to learn how to get out
through the door if he wins he get points if he fails of stuck in the room he loses points, over times it learns
to maximize points ! ''')
st.write('SO...')
col5 , col6 , col7 = st.columns(3)
with col5 :
    st.subheader('Supervised learning')
    st.write('''you have clear target variable.
    'there are a lot of models like 
    linear regression, KNN, decision tree, random forest,..''')
with col6 : 
    st.subheader('Unsupervised Learning')
    st.write('''
    you don't have target you just group the data
    to groupes like a dog trying to orginize the pack of sheep 🐶''')
with col7 : 
    st.subheader('Reinforcement Learning')
    st.write('It can learn to play chess better then you !')

st.divider()

st.header('Now for Deep Learning ! ')

st.subheader('it is so vast we will not cover it here but...')

st.write('''
DL is using artificial neural networks (like the one in human brain) to do what ML can't.
Deal with unclassified data it can process images, videos, and texts''')

st.divider()

st.header('Languages you will need !')

col8 , col9 , col10 = st.columns(3)

with col8 : 
    st.subheader('Pyhton 🐛')
    st.write('''
    it is used for data analysis, machine learning
     and most importantly deep learning, mostly you need these libraries: 
     pandas , numpy, sklearn, matplotlib, seaborn''')
with col9 : 
    st.subheader('R 🐧')
    st.write('''
     it's great for statistical analysis, machine learning, and visualizations,
     but for heavy ML or DL pyhton is better''')
with col10 : 
    st.subheader('SQL 🦄')
    st.write('''
    it is not real programming language but 
    its close enough, its used to talk to databases, 
    manupilate data inside the database and push or pull data,
     without it you are useless''')
st.divider()
st.header('Data Science Tools')
st.subheader('Data Scientists use different tools depending on the stage of a project.')

st.markdown('''
- **RStudio** — An environment for writing R code, analyzing data, creating visualizations, and building statistical models.

- **Jupyter Notebook** — An interactive environment where we can write code, run it step by step, visualize results, and document our analysis.

- **Power BI** — A Business Intelligence tool used to analyze data and create interactive dashboards and reports.

- **SPSS** — A statistical software widely used for data analysis, statistical testing, and research.

- **Web Scraping** — The process of automatically collecting data from websites using code.

- **Google Colab** — A cloud-based environment that allows you to write and run Python code in your browser without needing to set up a local environment.''')

st.success('WOW that was a lot of talking 🫠 now lets do practical exercise in the next page 😒')

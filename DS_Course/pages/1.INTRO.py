import streamlit as st
import matplotlib.pyplot as plt

st.title('WHAT IS DATA SCIENCE?')
st.write(
    ''' Data Science is the process of using data, programming, statistics,
    and domain knowledge to extract useful information, answer questions,
    and build solutions.
    so to make it simple..you have data and you need to extract information from it who you call? a data scientist, so 
    we can say we use DS to turn row data to meaningful informations, the power is in information beacuse it can answer a problem, find a solution, 
    or just understand something, well a data scientists need tools to extract information from data'''
)

st.divider()

st.header('so...what does a data scientist actualy do?')

st.write('''
          everything, every movment in this world produce data, it is the trace, the proove that something had happend, when you walk on send your footprint stays on send
          it is a proove that a person had walked this route, if we bring a skilled one to track you he will find you based on the data
          you left ( the footprint), when you get sick you feel weak, maybe you caugh these are evidences of a sickness, when a company make a sell
          it produce data in process (what product i sold, how much , how many , for who , when, ...) these data came in two main forms:
          stractural data :
          it is always represented in tables (matrix) every structual data comes in tables with columns called variables and rows called cases or observations.
          unstructual data : it is every other form of data a text, an image, video, audio,...
          so to answer the question what data scientist do is that he use tools that suits the structure or type of the data to inspact data and extract the information these data can provides.''')

st.divider()

st.header('what is data science process?')

st.write('''DS has its own approach to follow..
          before touching data, before chosing what code to write what tool to use you must understand the BUSINESS PROBLEM
          you have to ask what i want to understand, to solve, or to identify? the origine of DS process is understanding what problem are we looking at
          usualy in real scenarios the business problem is provided by the business owner for example a manager can reach you and say i want to know if our new
          marketing compaine is working. Then you have to understand where to get the data from you need to identify the source of data you might need
          is it in company data base? in company's social media accounts? or somewhere else. 
          then you need to make assumptions about the results , these assumptions must be logical.
          After that you start looking at the data, explortion, analysis, modeling, prediction, evaluation, and deployment.
          explore your data and take a good look at it, make an anlysis moving toward your answer, if making a model is necessary do it but
          chose the right one, make predictions with your model, evaluate it, then deploy it and communicate results with the one how is looking for it
          communication is crucial skill for talented data scientist.''')


st.write('so the process is like this : ')
st.markdown('''
 **❓ Questions**

    ↓

 **📦 Data**
    
    ↓
    
**🔎 Exploration**
    
    ↓
    
**📊 Analysis**
    
    ↓
    
**💡 Insights**
    
    ↓
    
**🤖 Models / Predictions**
    
    ↓
    
**🎯 Decisions**
 ''')
st.divider()

st.header('let us use a real example')
st.write('''
through this course we will try to use a generated data to learn 
the data is about advertising , a company spend its money a advertise through three channels: newspaper, radio, and TV and it keeps tracking sells in the process
''')
col1 , col2 , col3 = st.columns(3)
with col1:
    st.subheader('📺 TV')
    st.write('money spent on TV advertising')
with col2 :
    st.subheader('📻 Radio')
    st.write('money spent on radio advertising')
with col3 : 
    st.subheader('📰 Newspaper')
    st.write('money spent on newspaper advertising')

st.write('our dataset therefore containes : ')

st.code('''
TV        Radio        Newspaper        Sales
230.1     37.8         69.2             22.1
44.5      39.3         45.1             10.4
17.2      45.9         69.3             12.0
151.5     41.3         58.5             16.9
180.8     10.8         58.4             17.9''')

st.divider()
st.header('now we can start asking question')
st.write('for example  : ')
st.markdown('''
 - 📺 Does TV advertising have a relationship with sales?
    
    - 📻 Does radio advertising have a relationship with sales?
    
    - 📰 What about newspaper advertising?
    
    - 🔎 Which advertising channel appears to be most strongly related to sales?
    
    - 📈 How does sales change when advertising spending changes?
    
    - 🤖 Can we build a model that predicts sales?
''')

st.divider()

st.header('what do we need to use to answer these questions ?')

col3  , col4 = st.columns(2)

with col3 :
    st.subheader("🐍 Programming")
    st.write(
        """
        Programming allows us to manipulate data, automate tasks,
        perform analysis, build models, and create applications.
        
        Common languages include Python and R.
        """
    )

    st.subheader("📐 Statistics & Mathematics")
    st.write(
        """
        Statistics helps us understand distributions, relationships,
        uncertainty, and whether patterns in our data are meaningful.
        """
    )
with col4: 
     st.subheader("🗄️ Data")
     st.write(
        """
        Data is the raw material of Data Science.
        
        It can come from databases, CSV files, APIs, websites,
        sensors, experiments, and many other sources.
        """
    )

     st.subheader("🧠 Domain Knowledge")
     st.write(
        """
        We also need to understand the problem itself.
        
        Knowing the mathematics is not enough if we don't understand
        what the data represents and what the business or scientific
        problem actually is.
        """
    )

st.divider()

st.header("Data Science is bigger than Machine Learning")

st.write(
    """
    One of the most important things to understand from the beginning:
    **Data Science is not just Machine Learning.**
    """
)

st.markdown(
    """
    **Data Science**
    
    ├── 📥 Data Collection
    
    ├── 🧹 Data Cleaning
    
    ├── 📊 Data Analysis
    
    ├── 📐 Statistics
    
    ├── 📈 Data Visualization
    
    ├── 🤖 Machine Learning
    
    └── 💬 Communication
    """
)

st.divider()

st.success(
    """
    The main idea:
    
    **Data Science turns data into useful knowledge and solutions.**
    """
)

st.write(
    """
    In the next pages, we will look at the different parts of Data Science
    and understand what each one is actually used for.
    """
)

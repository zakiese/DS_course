import streamlit as st
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# --------------------------------------------------
# PAGE TITLE
# --------------------------------------------------

st.title(' Practical Exercise — Advertising & Sales')

st.write(
    '''
    Now let's put what we learned into practice.

    We will work with a real dataset containing advertising spending
    and sales data.
    '''
)

st.divider()


# --------------------------------------------------
# 1. LOAD THE DATA
# --------------------------------------------------

st.header('1️⃣ Load the Dataset')

BASE_DIR = Path(__file__).resolve().parent.parent

data_path = BASE_DIR / "advertising_sales_data.csv"

df = pd.read_csv(data_path)
st.success('Dataset loaded successfully!')

st.write('Here are the first rows of our dataset:')

st.dataframe(df.head())


st.divider()


# --------------------------------------------------
# 2. UNDERSTAND THE DATA
# --------------------------------------------------

st.header('2️⃣ Understand the Dataset')

st.write(
    '''
    Before analyzing a dataset, we need to understand what it contains.
    '''
)

st.write('### Dataset shape')

rows, columns = df.shape

col1, col2 = st.columns(2)

with col1:
    st.metric('Rows', rows)

with col2:
    st.metric('Columns', columns)


st.write('### Columns')

st.write(list(df.columns))


st.divider()


# --------------------------------------------------
# 3. BASIC STATISTICS
# --------------------------------------------------

st.header('3️⃣ Basic Statistics')

st.write(
    '''
    Descriptive statistics help us get a quick overview of the numerical data.
    '''
)

st.dataframe(df.describe())


st.divider()


# --------------------------------------------------
# 4. CHECK MISSING VALUES
# --------------------------------------------------

st.header('4️⃣ Check Data Quality')

missing = df.isnull().sum()

if missing.sum() == 0:
    st.success('There are no missing values in the dataset.')
else:
    st.warning('The dataset contains missing values.')

    st.dataframe(missing)


st.divider()


# --------------------------------------------------
# 5. VISUALIZE THE DATA
# --------------------------------------------------

st.header('5️⃣ Explore the Data')

st.write(
    '''
    Visualization helps us understand relationships and patterns
    that may be difficult to see from a table.
    '''
)

variable = st.selectbox(
    'Choose an advertising channel:',
    ['TV', 'radio', 'newspaper']
)


fig, ax = plt.subplots()

ax.scatter(df[variable], df['sales'])

ax.set_xlabel(variable)
ax.set_ylabel('Sales')
ax.set_title(f'{variable} Advertising vs Sales')

st.pyplot(fig)


st.write(
    '''
    Each point represents one observation from our dataset.

    We can use this graph to visually examine whether advertising
    spending appears to be related to sales.
    '''
)


st.divider()


# --------------------------------------------------
# 6. CORRELATION
# --------------------------------------------------

st.header('6️⃣ Correlation')

st.write(
    '''
    Correlation measures the strength and direction of a linear
    relationship between two numerical variables.

    Values closer to 1 indicate a strong positive relationship,
    values closer to -1 indicate a strong negative relationship,
    and values around 0 indicate little linear relationship.
    '''
)

correlation = df.corr(numeric_only=True)

st.dataframe(correlation)


st.divider()


# --------------------------------------------------
# 7. MACHINE LEARNING
# --------------------------------------------------

st.header('''7️⃣ Let's Build a Machine Learning Model ''')

st.write(
    '''
    Now we will use Machine Learning to predict sales.

    Our input variables will be:

    - TV advertising
    - Radio advertising
    - Newspaper advertising

    Our target will be:

    - Sales
    '''
)

X = df[['TV', 'radio', 'newspaper']]

y = df['sales']


# --------------------------------------------------
# TRAIN / TEST SPLIT
# --------------------------------------------------

st.subheader('Train / Test Split')

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

st.write(f'Training data: {len(X_train)} rows')
st.write(f'Testing data: {len(X_test)} rows')


# --------------------------------------------------
# TRAIN MODEL
# --------------------------------------------------

model = LinearRegression()

model.fit(X_train, y_train)


# --------------------------------------------------
# MAKE PREDICTIONS
# --------------------------------------------------

predictions = model.predict(X_test)


st.success('The model has been trained!')


# --------------------------------------------------
# 8. MODEL EVALUATION
# --------------------------------------------------

st.subheader('Model Evaluation')

mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
rmse = mse ** 0.5
r2 = r2_score(y_test, predictions)


col1, col2, col3 = st.columns(3)

with col1:
    st.metric('MAE', round(mae, 2))

with col2:
    st.metric('RMSE', round(rmse, 2))

with col3:
    st.metric('R²', round(r2, 2))


st.write(
    '''
    These metrics help us evaluate how well our model predicts sales.

    **MAE** tells us the average absolute prediction error.

    **RMSE** gives more weight to larger errors.

    **R²** indicates how much of the variation in sales is explained
    by the model.
    (like test result on your exam same logic)
    '''
)


st.divider()


# --------------------------------------------------
# 9. MAKE A NEW PREDICTION
# --------------------------------------------------

st.header('9️⃣ Try the Model Yourself')

st.write(
    '''
    Enter advertising spending values and let the model predict the
    expected sales.
    '''
)

tv_input = st.number_input(
    'TV advertising',
    min_value=0.0,
    value=100.0
)

radio_input = st.number_input(
    'Radio advertising',
    min_value=0.0,
    value=20.0
)

newspaper_input = st.number_input(
    'Newspaper advertising',
    min_value=0.0,
    value=30.0
)


if st.button('Predict Sales'):

    new_data = pd.DataFrame(
        {
            'TV': [tv_input],
            'radio': [radio_input],
            'newspaper': [newspaper_input]
        }
    )

    prediction = model.predict(new_data)

    st.success(
        f'Predicted Sales: {prediction[0]:.2f}'
    )


st.divider()


# --------------------------------------------------
# CONCLUSION
# --------------------------------------------------

st.header(' What Did We Do?')

st.markdown(
    '''
    We followed a simplified Data Science workflow:

    ** Load Data**

    ↓

    ** Understand the Data**

    ↓

    ** Check Data Quality**

    ↓

    ** Explore & Visualize**

    ↓

    ** Analyze Relationships**

    ↓

    ** Build a Machine Learning Model**

    ↓

    ** Evaluate the Model**

    ↓

    ** Make Predictions**
    '''
)

st.write(
    '''
    This is the basic idea of a complete Data Science project:
    turning raw data into information, analysis, and eventually
    a useful predictive model.
    '''
)

st.success('Now go and be a data scientist ! 😗')

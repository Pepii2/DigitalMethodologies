import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set page title
st.title('Exploratory Data Analysis on Food Waste Survey')

# Load the dataset
st.sidebar.header("Upload CSV File")
uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    data_translated = pd.read_csv(uploaded_file)
    
    # Display first 5 rows
    st.subheader('First 5 Rows of the Dataset')
    st.write(data_translated.head())

    # Summary statistics
    st.subheader('Summary Statistics')
    st.write(data_translated.describe(include='all'))

    # Missing values check
    st.subheader('Missing Values')
    st.write(data_translated.isnull().sum())

    # Univariate Analysis
    st.subheader("Univariate Analysis: Distribution of Variables")

    # Age Group Distribution (matching column name)
    st.write("### Age Group Distribution")
    plt.figure(figsize=(8, 6))
    sns.countplot(x='What is your age?', data=data_translated)
    plt.xticks(rotation=45)
    st.pyplot(plt.gcf())
    plt.clf()  # Clear figure

    # Distribution of Food Waste Practices (matching column name)
    st.write("### Practices to Reduce Food Waste")
    plt.figure(figsize=(8, 6))
    sns.countplot(
        y=' ¿Cuáles de las siguientes prácticas implementas en tu hogar para reducir el desperdicio de alimentos? (Selecciona todas las que apliquen)', 
        data=data_translated, 
        order=data_translated[' ¿Cuáles de las siguientes prácticas implementas en tu hogar para reducir el desperdicio de alimentos? (Selecciona todas las que apliquen)'].value_counts().index
    )
    st.pyplot(plt.gcf())
    plt.clf()

    # Motivation for Reducing Food Waste (matching column name)
    st.write("### Motivation for Reducing Food Waste")
    plt.figure(figsize=(8, 6))
    sns.countplot(x='What would be your main motivation to reduce food waste?', data=data_translated)
    plt.xticks(rotation=45)
    st.pyplot(plt.gcf())
    plt.clf()

    # Likelihood of Using a Service (matching column name)
    st.write("### Likelihood of Using a Service for Food Waste Management")
    plt.figure(figsize=(8, 6))
    sns.countplot(x='How likely are you to use a service or app that helps you manage your purchases better and reduce food waste?', data=data_translated)
    plt.xticks(rotation=45)
    st.pyplot(plt.gcf())
    plt.clf()

    # Numeric Analysis
    st.subheader("Numeric Analysis: Distribution of Food Wasted")

    if 'What percentage of the food you buy do you end up throwing away?' in data_translated.columns:
        st.write("### Percentage of Food Wasted")
        plt.figure(figsize=(8, 6))
        sns.histplot(data_translated['What percentage of the food you buy do you end up throwing away?'], bins=10, kde=True)
        st.pyplot(plt.gcf())
        plt.clf()

    # Bivariate Analysis
    st.subheader("Bivariate Analysis: Relationships Between Variables")

    # Relationship between Age and Likelihood of Using a Service (matching column name)
    st.write("### Age Group vs Likelihood of Using a Service")
    plt.figure(figsize=(8, 6))
    sns.countplot(x='What is your age?', hue='How likely are you to use a service or app that helps you manage your purchases better and reduce food waste?', data=data_translated)
    plt.xticks(rotation=45)
    st.pyplot(plt.gcf())
    plt.clf()

    # Relationship between Age and Food Waste Motivation (matching column name)
    st.write("### Age Group vs Motivation for Reducing Food Waste")
    plt.figure(figsize=(8, 6))
    sns.countplot(x='What is your age?', hue='What would be your main motivation to reduce food waste?', data=data_translated)
    plt.xticks(rotation=45)
    st.pyplot(plt.gcf())
    plt.clf()

    # Correlation Analysis
st.subheader("Correlation Analysis")

# Ensure that there are numeric columns available for correlation
if 'What percentage of the food you buy do you end up throwing away?' in data_translated.columns:
    # Compute correlation matrix
    correlation_matrix = data_translated.corr(numeric_only=True)
    
    if correlation_matrix.empty:
        st.write("No numeric columns available for correlation analysis.")
    else:
        st.write("### Correlation Heatmap")
        plt.figure(figsize=(10, 6))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
        st.pyplot(plt.gcf())
else:
    st.write("No numeric columns for correlation analysis.")

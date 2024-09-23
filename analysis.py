# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (if not already loaded)
data_translated = pd.read_csv("Augmented_data2.csv")  # Uncomment if loading from a file

# Display the first few rows of the dataset
print("First 5 rows of the dataset:")
print(data_translated.head())

# Get the summary of the dataset
print("\nSummary statistics:")
print(data_translated.describe(include='all'))

# Check for missing values
print("\nMissing values:")
print(data_translated.isnull().sum())

# 1. Univariate Analysis: Distribution of categorical variables

# Age Group Distribution
plt.figure(figsize=(8, 6))
sns.countplot(x='What is your age?', data=data_translated)
plt.title("Distribution of Age Groups")
plt.xlabel("Age Group")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# Distribution of Food Waste Practices
plt.figure(figsize=(8, 6))
sns.countplot(y='Which of the following practices do you implement at home to reduce food waste? (Select all that apply)', data=data_translated,
              order=data_translated['Which of the following practices do you implement at home to reduce food waste? (Select all that apply)'].value_counts().index)
plt.title("Practices to Reduce Food Waste")
plt.xlabel("Count")
plt.ylabel("Practices")
plt.show()

# Motivation for Reducing Food Waste
plt.figure(figsize=(8, 6))
sns.countplot(x='What would be your main motivation to reduce food waste?', data=data_translated)
plt.title("Motivations for Reducing Food Waste")
plt.xlabel("Motivation")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# Likelihood of Using a Service for Food Waste Management
plt.figure(figsize=(8, 6))
sns.countplot(x='How likely are you to use a service or app that helps you manage your purchases and reduce food waste?', data=data_translated)
plt.title("Likelihood of Using a Service")
plt.xlabel("Likelihood")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# 2. Numeric Analysis: Distribution of numeric variables
# Percentage of Food Wasted
plt.figure(figsize=(8, 6))
sns.histplot(data_translated['What percentage of the food you buy do you end up throwing away?'], bins=10, kde=True)
plt.title("Distribution of Percentage of Food Wasted")
plt.xlabel("Percentage of Food Wasted")
plt.ylabel("Frequency")
plt.show()

# 3. Bivariate Analysis: Relationships between variables

# Relationship between Age and Likelihood of Using a Service
plt.figure(figsize=(8, 6))
sns.countplot(x='What is your age?', hue='How likely are you to use a service or app that helps you manage your purchases and reduce food waste?', data=data_translated)
plt.title("Age Group vs Likelihood of Using a Service")
plt.xlabel("Age Group")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# Relationship between Food Waste Motivation and Age
plt.figure(figsize=(8, 6))
sns.countplot(x='What is your age?', hue='What would be your main motivation to reduce food waste?', data=data_translated)
plt.title("Age Group vs Motivation for Reducing Food Waste")
plt.xlabel("Age Group")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# 4. Correlation Analysis (for numeric columns)

# Check if there are numeric columns
if 'What percentage of the food you buy do you end up throwing away?' in data_translated.columns:
    plt.figure(figsize=(10, 6))
    correlation_matrix = data_translated.corr(numeric_only=True)
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title("Correlation Matrix")
    plt.show()
else:
    print("No numeric columns for correlation analysis.")

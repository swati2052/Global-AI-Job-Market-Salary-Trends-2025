# data_visualization.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

sns.set(style="darkgrid")

# ✅ Correct CSV filename
df = pd.read_csv("ai_job_dataset.csv")  # Ensure this file exists in your folder

# Data overview
print("Shape:", df.shape)
print(df.info())
print(df.describe())
print(df.isnull().sum())

# ✅ Data Cleaning with correct column names
df = df.dropna(subset=['job_title', 'salary_usd', 'experience_level', 'company_location', 'remote_ratio'])

# ✅ Visualization 1: Top 10 Countries Hiring
top_countries = df['company_location'].value_counts().head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_countries.values, y=top_countries.index, palette="Blues_d")
plt.title("Top 10 Countries Hiring for AI Jobs")
plt.xlabel("Number of Jobs")
plt.ylabel("Country")
plt.tight_layout()
plt.show()

# ✅ Visualization 2: Experience Level Distribution
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='experience_level', palette='Set2')
plt.title("AI Job Experience Level Distribution")
plt.xlabel("Experience Level")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# ✅ Visualization 3: Remote vs On-site Jobs
# Convert remote_ratio to readable categories
df['remote_type'] = df['remote_ratio'].apply(lambda x: 'On-site' if x == 0 else 'Hybrid' if x == 50 else 'Remote')

plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='remote_type', palette='Set3')
plt.title("Remote vs On-site AI Jobs")
plt.xlabel("Job Type")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# ✅ Visualization 4: Salary Distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['salary_usd'], bins=30, kde=True, color='green')
plt.title("Distribution of AI Job Salaries (USD)")
plt.xlabel("Salary (USD)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# ✅ Visualization 5: WordCloud of Job Titles
text = " ".join(df['job_title'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Most Common AI Job Titles")
plt.tight_layout()
plt.show()

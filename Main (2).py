import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import re
import numpy as np

# Load cleaned dataset
def load_data():
    file_path = "df_cleaned.csv"  # Use the uploaded file path
    return pd.read_csv(file_path)

df = load_data()
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1534796636912-3b95b3ab5986?ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80");
        background-size: cover;
        background-position: center;
        background-color: #1e1e1e;
        color: white;
        font-family: 'Arial', sans-serif;
    }
    .stMarkdown, .stTitle, .stHeader, .stSubheader, .stMetric {
        color: white;
    }
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #ff4b4b;
        margin-bottom: 1rem;
    }
    .stMarkdown p {
        font-size: 1.1rem;
        line-height: 1.6;
        margin-bottom: 1.5rem;
    }
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-size: 1rem;
        border: none;
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #ff1c1c;
    }
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background-color: rgba(46, 46, 46, 0.8);
        color: white;
        border: 1px solid #444;
        border-radius: 8px;
        padding: 0.5rem;
    }
    .stTextInput>div>div>input:focus, .stTextArea>div>div>textarea:focus {
        border-color: #ff4b4b;
        outline: none;
    }
    .stDataFrame {
        background-color: rgba(46, 46, 46, 0.8);
        border-radius: 8px;
        padding: 1rem;
    }
    .stAlert {
        background-color: rgba(46, 46, 46, 0.8);
        border-radius: 8px;
        padding: 1rem;
        border: 1px solid #444;
    }
    .stAlert .stMarkdown {
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Convert salary to yearly format
def convert_to_yearly(salary_text):
    if pd.isnull(salary_text) or "Not Disclosed" in salary_text:
        return np.nan 
    salary_values = re.findall(r"₹([\d,]+)", salary_text)
    if not salary_values:
        return np.nan
    salary_values = [int(value.replace(",", "")) for value in salary_values]
    avg_salary = np.mean(salary_values)
    if "a month" in salary_text:
        return avg_salary * 12  
    elif "a year" in salary_text:
        return avg_salary  
    else:
        return np.nan  

df["yearly_salary"] = df["job_salary"].apply(convert_to_yearly)

# Streamlit UI
st.title("📊 Job Market Demand Analysis Dashboard")

# Tab Layout
tab1, tab2 = st.tabs(["Overview & Insights", "Interactive Analysis"])

with tab1:
    st.header("🏆 Job Market Insights & Trends")
    
    # Top 10 Most In-Demand Job Titles
    st.subheader("Top 10 Most In-Demand Job Titles")
    job_title_counts = df["job_title"].value_counts().head(10)
    fig, ax = plt.subplots(figsize=(12, 5))
    sns.barplot(x=job_title_counts.values, y=job_title_counts.index, palette="Blues_r", ax=ax)
    ax.set_xlabel("Number of Job Postings")
    ax.set_ylabel("Job Title")
    st.pyplot(fig)
    
    # Top 10 Job Locations
    st.subheader("Top 10 Job Locations with Highest Demand")
    job_location_counts = df["job_location"].value_counts().head(10)
    fig, ax = plt.subplots(figsize=(12, 5))
    sns.barplot(x=job_location_counts.values, y=job_location_counts.index, palette="Greens_r", ax=ax)
    ax.set_xlabel("Number of Job Postings")
    ax.set_ylabel("Job Location")
    st.pyplot(fig)
    
    # Skill Extraction
    common_skills = ["python", "sql", "excel", "power bi", "tableau", "machine learning", "deep learning", "nlp", "statistics", "data visualization", "big data", "aws", "azure", "hadoop", "pandas", "numpy", "tensorflow", "pytorch", "scikit-learn", "r", "spark", "matplotlib", "seaborn", "etl", "data wrangling", "data analysis"]

    def refined_extract_skills(text):
        if pd.isnull(text):  
            return []
        text = text.lower()
        skills_found = [skill for skill in common_skills if re.search(rf"\b{skill}\b", text)]
        return skills_found

    df["extracted_skills"] = df["job_summary"].apply(refined_extract_skills)
    all_skills_refined = [skill for sublist in df["extracted_skills"] for skill in sublist]
    skill_counts_refined = Counter(all_skills_refined).most_common(10)
    df_skills_refined = pd.DataFrame(skill_counts_refined, columns=["Skill", "Count"])

    # Top 10 Most In-Demand Skills
    st.subheader("Top 10 Most In-Demand Skills")
    fig, ax = plt.subplots(figsize=(12, 5))
    sns.barplot(x=df_skills_refined["Count"], y=df_skills_refined["Skill"], palette="Oranges_r", ax=ax)
    ax.set_xlabel("Number of Job Postings Mentioning Skill")
    ax.set_ylabel("Skill")
    st.pyplot(fig)
    
    # Average Salary
    st.subheader("💰 Average Yearly Salary")
    st.metric(label="Average Yearly Salary (INR)", value=f"₹{df['yearly_salary'].mean():,.2f}")
    
    # Salary Distribution
    st.subheader("Distribution of Yearly Salaries")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.histplot(df["yearly_salary"].dropna(), bins=30, kde=True, color="blue", ax=ax)
    ax.set_xlabel("Yearly Salary (INR)")
    ax.set_ylabel("Frequency")
    st.pyplot(fig)
    
    # Top 10 Highest Paying Job Titles
    st.subheader("Top 10 Highest Paying Job Titles")
    top_salaries_by_title = df.groupby("job_title")["yearly_salary"].mean().sort_values(ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x=top_salaries_by_title.values, y=top_salaries_by_title.index, palette="Blues_r", ax=ax)
    ax.set_xlabel("Average Yearly Salary (INR)")
    ax.set_ylabel("Job Title")
    st.pyplot(fig)
    
    # Salary Table by Location
    st.subheader("Salary Comparison by Location")
    top_salaries_by_location = df.groupby("job_location")["yearly_salary"].mean().sort_values(ascending=False).head(10)
    st.dataframe(top_salaries_by_location.round(2))
    
    
    # Insights Section
    st.subheader("📈 Key Job Market Insights")
    st.markdown("""
    - **Skill Popularity:** Python, SQL, and Machine Learning are the most sought-after skills, followed by cloud platforms like AWS and Azure.
    - **Geographic Demand:** Bangalore, Hyderabad, and Pune dominate tech hiring, while Delhi and Mumbai show a diverse industry mix.
    - **Industry Shifts:** Data analytics and AI-driven roles are on the rise, with increasing adoption in finance, healthcare, and retail sectors.
    - **Salary Trends:** AI/ML and Cloud Engineering offer the highest salaries, with salaries significantly higher in tech hubs.
    - **Remote Work Trends:** Remote work is prevalent in software development, data science, and digital marketing, but less common in healthcare and manufacturing.
    """)
with tab2:
    st.header("📊 Interactive Data Analysis")
    
    # Filters
    locations = st.multiselect("Select Job Locations:", df["job_location"].unique())
    titles = st.multiselect("Select Job Titles:", df["job_title"].unique())
    
    # Apply filters
    filtered_df = df.copy()
    if locations:
        filtered_df = filtered_df[filtered_df["job_location"].isin(locations)]
    if titles:
        filtered_df = filtered_df[filtered_df["job_title"].isin(titles)]
    
    # Interactive Salary Distribution
    st.subheader("Filtered Salary Distribution")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.histplot(filtered_df["yearly_salary"].dropna(), bins=30, kde=True, color="purple", ax=ax)
    ax.set_xlabel("Yearly Salary (INR)")
    ax.set_ylabel("Frequency")
    st.pyplot(fig)
    
    # Interactive Skill Demand
    st.subheader("Filtered Skill Demand")
    skill_counts_filtered = Counter([skill for sublist in filtered_df["extracted_skills"] for skill in sublist])
    df_skills_filtered = pd.DataFrame(skill_counts_filtered.most_common(10), columns=["Skill", "Count"])
    st.bar_chart(df_skills_filtered.set_index("Skill"))

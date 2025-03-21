#https://construct-week-project-unit-4-xu46r9cuuuhvrzvtstvhrs.streamlit.app/

# Job Market Demand Analysis

## Overview
This project aims to analyze job market demand using web-scraped job listings, perform Exploratory Data Analysis (EDA), and visualize insights using a Streamlit dashboard. The dataset contains job titles, locations, required skills, salaries, and posting dates.

## Project Workflow
1. **Web Scraping Job Listings**
2. **Data Cleaning & Preprocessing**
3. **Exploratory Data Analysis (EDA)**
4. **Building a Streamlit Dashboard**

---

## 1️⃣ Web Scraping Job Listings
We collected job postings from an online job portal using Python libraries such as `requests`, `BeautifulSoup`, and `Selenium`.

### Steps:
- Sent HTTP requests to job listing pages.
- Parsed HTML responses to extract job details (title, location, salary, posting date, etc.).
- Stored extracted data in a CSV file (`job_dataset.csv`).

---

## 2️⃣ Data Cleaning & Preprocessing
### Key Tasks:
- **Handling Missing Values:** Dropped or imputed missing values.
- **Parsing Dates:** Converted posting dates into structured format.
- **Extracting Skills:** Used regex to identify common skills in job descriptions.
- **Standardizing Salaries:** Converted all salary data to yearly figures.

**Saved the cleaned dataset as** `cleaned_job_dataset.csv`.

---

## 3️⃣ Exploratory Data Analysis (EDA)
We performed various analyses to derive insights:

### 📌 Job Demand Analysis
- Identified the **top 10 most in-demand job titles** and **top hiring locations**.
- Extracted **top 10 most required skills** from job descriptions.

### 📌 Salary Analysis
- Converted salaries into a **yearly format**.
- Visualized the **distribution of yearly salaries**.
- Identified **top 10 highest-paying job titles**.
- Compared **average salaries across locations**.

---

## 4️⃣ Streamlit Dashboard
The insights are visualized in an interactive **Streamlit** app.

### Features:
📊 **Tab 1 - The Top 10 Insights**
- Top 10 most in-demand job titles.
- Top 10 hiring locations.
- Top 10 most required skills.
- Average salary indicator.
- Salary distribution.
- Top 10 highest-paying job titles.

📊 **Tab 2 - Detailed Analysis**
- Users can filter data by job title & location.
- Interactive visualizations to explore trends.

---

## How to Run the Project
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Pandas
- Matplotlib
- Seaborn
- Streamlit
- BeautifulSoup & Selenium (if scraping is required)

### Steps to Run:
1. **Clone the repository**
   ```bash
   git clone https://github.com/your-repo/job-market-analysis.git
   cd job-market-analysis
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Streamlit Dashboard**
   ```bash
   streamlit run job_market_dashboard.py
   ```

This will launch the interactive dashboard in your web browser.

---

## Conclusion
This project provides valuable insights into job market trends, skill demand, and salary distributions. The dashboard helps users explore data interactively and make data-driven career decisions.

🚀 **Future Improvements:**
- Automate web scraping for real-time updates.
- Enhance filtering options in the dashboard.
- Incorporate more job portals for a broader dataset.

🎯 **Contributions are welcome!**


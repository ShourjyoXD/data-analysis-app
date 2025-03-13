# data-analysis-app
Basic Data Analysis with Pandas & Matplotlib

Introduction
This project explores a sample dataset containing employee information to extract meaningful insights using Pandas and Matplotlib. The analysis reveals trends in age, salary, experience, and department distribution.

Dataset Overview
The dataset contains the following columns:
Name: Employee's name
Age: Employee's age
Salary: Employee's salary
Department: Employee's department
Experience_Years: Years of professional experience

Data Summary
Entries: 5 rows
missing values
No duplicate entries
Outlier detection: No extreme values requiring removal

Key Findings
Basic Statistics
| Metric        | Age | Salary | Experience_Years |
|---------------|-----|--------|------------------|
|   Count       | 5   | 5      | 5                |
|    Mean       | 35  | 70,000 | 8                |
|    Min        | 25  | 50,000 | 2                |
|   Max         | 45  | 90,000 | 15               |

Observations
Age Distribution: The dataset shows a balanced age range between 25 to 45 years, with most employees in their 30s.
Salary Distribution: Salaries range from ₹50,000 to ₹90,000, with most employees earning around ₹70,000.
Experience vs. Salary: Employees with more experience tend to have higher salaries, reinforcing the expected relationship between experience and earnings.
Department Analysis: The dataset indicates a balanced workforce distribution across departments.
Correlation Analysis: Age, Salary, and Experience show positive correlations, suggesting these factors are closely linked.

Visualizations
1. Bar Chart: Age distribution across employees.
2. Scatter Plot: Salary vs. Experience to observe career growth patterns.
3. Heatmap: Correlation analysis highlighting positive trends.

 Recommendations
1. Talent Retention Strategy: Since experienced employees command higher salaries, investing in talent retention strategies such as bonuses, upskilling programs, and leadership development can help retain top performers.
2. Departmental Growth: With balanced workforce distribution, the company can explore strategic expansion in key teams.
3. Future Data Collection: Adding features like job roles, education levels, and performance ratings can provide deeper insights for improved workforce planning.

How to Run the Project
1. Install the required libraries:
```bash
pip install pandas matplotlib
```
2. Clone this repository:
```bash
git clone <repository_url>
```
3. Run the Python script:
```bash
python data_analysis.py
```

Conclusion
This project demonstrates effective data analysis using Python tools like Pandas and Matplotlib. The insights gained offer valuable information for decision-making, emphasizing the importance of data-driven strategies in workforce management.

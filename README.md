# Business Analytics Dashboard

📈 **Business Analytics Dashboard** is an interactive web application built using Streamlit. This dashboard provides insights into employee data, including metrics, visualizations, and the ability to filter and analyze data dynamically.

## Features

### Interactive Filters:
- Filter by Department, Country, Business Unit, Age, and Salary Range.
- Apply multiple filters to refine your analysis.

### Key Metrics:
- **Total Employees**
- **Total Annual Salary**
- **Average Age**
- **Average Tenure (in years)**

### Visualizations:
- **Gender Distribution:** A pie chart showing the proportion of male and female employees.
- **Salary by Department:** A bar chart displaying total salaries by department.
- **Employee Tenure Distribution:** A histogram showing the tenure of employees.

### Detailed Data View:
- View filtered data in a table format.
- Download the filtered data as a CSV file.
- Display summary statistics for the selected data.

## Installation

### Clone the Repository:
```bash
git clone https://github.com/FadyHassanein/business-analytics-dashboard.git
cd business-analytics-dashboard
```

### Install Dependencies:
Ensure you have Python installed. Then, install the required libraries:
```bash
pip install -r requirements.txt
```

### Run the Application:
Start the Streamlit app:
```bash
streamlit run app.py
```

### Access the App:
Open the app in your browser at:
```
http://localhost:8501
```

## File Structure
- **app.py:** The main Streamlit application code.
- **customers.csv:** Sample dataset used for analysis.
- **style.css:** Custom CSS for styling the dashboard.
- **requirements.txt:** List of required Python packages.

## Usage

### Overview:
- Access key metrics at a glance.
- Explore visualizations for gender distribution, salary by department, and tenure analysis.

### Detailed Data:
- View and analyze the filtered dataset.
- Export filtered data to a CSV file for further analysis.

## Dataset
The app uses a sample dataset (`customers.csv`) with the following columns:
- **EEID:** Employee ID
- **FullName:** Full name of the employee
- **JobTitle:** Job title
- **Department:** Department name
- **BusinessUnit:** Business unit name
- **Gender:** Gender of the employee
- **Ethnicity:** Ethnicity of the employee
- **Age:** Age of the employee
- **HireDate:** Date the employee was hired
- **AnnualSalary:** Annual salary of the employee
- **Bonus:** Bonus percentage
- **Country:** Country of the employee
- **City:** City of the employee

## Requirements
- Python >= 3.7
- Streamlit
- Pandas
- Plotly
- Numerize


## Customization
- Modify the dataset (`customers.csv`) to use your own data.
- Adjust the visualizations or filters in `app.py` to match your specific needs.

import streamlit as st
import pandas as pd
from numerize.numerize import numerize
import plotly.express as px
from datetime import datetime

# Set Streamlit Page Configuration
st.set_page_config(page_title="Business Analytics Dashboard", page_icon="🌎", layout="wide")
st.subheader("📈 Business Analytics Dashboard")

# Load CSS Style
with open('style.css') as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load Data
df = pd.read_csv('customers.csv')

# Convert HireDate to datetime and calculate tenure
df['HireDate'] = pd.to_datetime(df['HireDate'])
df['Tenure'] = (datetime.now() - df['HireDate']).dt.days // 365

# Sidebar Filters
st.sidebar.header("Filter Options")

department = st.sidebar.multiselect(
    "Filter Department",
    options=df["Department"].unique(),
    default=df["Department"].unique()
)

country = st.sidebar.multiselect(
    "Filter Country",
    options=df["Country"].unique(),
    default=df["Country"].unique()
)

business_unit = st.sidebar.multiselect(
    "Filter Business Unit",
    options=df["BusinessUnit"].unique(),
    default=df["BusinessUnit"].unique()
)

age_range = st.sidebar.slider(
    "Age Range",
    min_value=int(df['Age'].min()),
    max_value=int(df['Age'].max()),
    value=(20, 60)
)

salary_range = st.sidebar.slider(
    "Salary Range",
    min_value=int(df['AnnualSalary'].min()),
    max_value=int(df['AnnualSalary'].max()),
    value=(50000, 200000)
)

# Apply Filters
df_selection = df[
    (df['Department'].isin(department)) &
    (df['Country'].isin(country)) &
    (df['BusinessUnit'].isin(business_unit)) &
    (df['Age'].between(*age_range)) &
    (df['AnnualSalary'].between(*salary_range))
]

# Metrics
def metrics():
    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        label="Total Employees",
        value=df_selection["EEID"].count()
    )

    col2.metric(
        label="Total Annual Salary",
        value=f"${df_selection['AnnualSalary'].sum():,.0f}"
    )

    col3.metric(
        label="Average Age",
        value=f"{df_selection['Age'].mean():.1f} years"
    )

    col4.metric(
        label="Average Tenure",
        value=f"{df_selection['Tenure'].mean():.1f} years"
    )

# Pie Chart for Gender Distribution
def gender_pie_chart():
    fig = px.pie(df_selection, names='Gender', title='Gender Distribution')
    st.plotly_chart(fig, use_container_width=True)

div1, div2 = st.columns(2)

def pie():
    with div1:
        theme_plotly = None  
        fig = px.pie(df_selection, values='AnnualSalary', names='Department', title='Customers by Country')
        fig.update_layout(legend_title="Country", legend_y=0.9)
        fig.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Bar Chart for Department Salary
def department_bar_chart():
    fig = px.bar(df_selection, x='Department', y='AnnualSalary', title="Salary by Department", text_auto=True)
    st.plotly_chart(fig, use_container_width=True)

# Tenure Histogram
def tenure_histogram():
    fig = px.histogram(df_selection, x='Tenure', nbins=10, title="Employee Tenure Distribution")
    st.plotly_chart(fig, use_container_width=True)

# Download Filtered Data
def download_data():
    st.download_button(
        label="Download Filtered Data",
        data=df_selection.to_csv(index=False),
        file_name='filtered_customers.csv',
        mime='text/csv'
    )

# Main Dashboard Sections
st.sidebar.title("Navigation")
options = st.sidebar.radio("Go to", ['Overview', 'Detailed Data'])

if options == 'Overview':
    st.header("Overview of Business Analytics")

    # Display Metrics
    metrics()

    # Visualizations
    col1, col2 = st.columns(2)
    with col1:
        gender_pie_chart()
    with col2:
        department_bar_chart()

    st.header("Employee Tenure Analysis")
    tenure_histogram()

elif options == 'Detailed Data':
    st.header("Filtered Data View")
    download_data()

    st.dataframe(df_selection, use_container_width=True)

    st.header("Data Summary")
    st.write(df_selection.describe())


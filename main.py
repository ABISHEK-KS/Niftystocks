import streamlit as st
import pandas as pd
import time
import streamlit.components.v1 as components

# Load CSS 
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("externalcss.css")

# Read file and convert date column to datetime
filed = pd.read_csv('Combined.csv')
filed['Date'] = pd.to_datetime(filed['Date'], format='%d-%m-%Y', errors='coerce')

# Buttons
home = st.sidebar.button('Home')
pbi = st.sidebar.button('Power-Bi Dashboard')
Docs = st.sidebar.button('Docs')
Prof = st.sidebar.button('YDTP Report')

# Function to split list into chunks
def split_into_chunks(lst, chunk_size):
    return [lst[i[i + chunk_size] for i in range(0, len(lst), chunk_size)]]

# Set default page
default_page = "Home"

# Determine selected page
if home:
    selected_page = "Home"
elif pbi:
    selected_page = "Power-Bi Dashboard"
elif Docs:
    selected_page = "Docs"
elif Prof:
    selected_page = "YDTP Report"
else:
    selected_page = default_page

# Home page
def show_home():
    st.header('NIFTY 2000-2021')
    st.image('imag.jpg')
    l = {
        "Dev": "ABISHEK K S",
        "Deployment": "Streamlit Cloud",
        "Pre-req": "Ref : Docs section",
    }
    st.table(l)

    st.info(' ')
    st.markdown("<h1 style='text-align: center; color: white;'>Stocks Available</h1>", unsafe_allow_html=True)
    splits = split_into_chunks(list(set(filed['Symbol'])), 5)
    st.table(splits)

    st.info(' ')
    st.markdown("<h1 style='text-align: center; color: white;'>Dataset Basics</h1>", unsafe_allow_html=True)
    st.table(filed.describe())

    st.info(' ')
    st.markdown("<h1 style='text-align: center; color: white;'>Correlation Matrix</h1>", unsafe_allow_html=True)
    st.write(filed.corr())

    st.info(' ')
    st.markdown("<h1 style='text-align: center; color: white;'>Skewness Table</h1>", unsafe_allow_html=True)
    st.table(filed.skew())

# Power-BI 
def show_pbi():
    st.warning("Select Full-Screen and set Zoom to 60% if browser does not show the Dashboard Fully")
    iframe_code = """
    <div style="width: 100%; height: 0; padding-bottom: 72.67%; position: relative;">
        <iframe src="https://app.powerbi.com/view?r=eyJrIjoiYTVhZThhOWYtY2U0NC00YTY5LTk3ZWUtNTRjNGJlZDFhNGM2IiwidCI6IjkzNjIwZTExLTliYzQtNDRiOC05YTVjLWJjMDY2M2I3NDM3NCIsImMiOjEwfQ%3D%3D" 
                style="position: absolute; width: 100%; height: 100%; border: 0;" allowfullscreen></iframe>
    </div>
    """
    st.markdown(iframe_code, unsafe_allow_html=True)

# Docs 
def show_docs():
    st.title("NIFTY 2000-2021 Financial Data Analysis")
    st.markdown("""
    The Streamlit app is designed to provide a user-friendly interface for in-depth analysis of financial data, focusing on the NIFTY 2000-2021 dataset. This platform offers various sections and functionalities to explore and interpret the dataset efficiently.
    """)

    st.header("Features")

    st.subheader("Home Section:")
    st.markdown("""
    - **Overview:** Provides a detailed insight into the NIFTY 2000-2021 dataset, including available stocks, dataset basics (descriptive statistics), correlation matrix, and skewness table.
    """)

    st.subheader("Power BI Dashboard:")
    st.markdown("""
    - **Functionality:** Offers access to an interactive Power BI dashboard embedded within the app, showcasing visualizations and analytics derived from the financial dataset.
    - **Optimization:** Users are recommended to enable full-screen mode and adjust the zoom level for optimal visualization.
    """)

    st.subheader("Documentation:")
    st.markdown("""
    - **Purpose:** Contains extensive documentation about the Service.
    """)

    st.subheader("YDTP Report (YData Profiling Report):")
    st.markdown("""
    - **Functionality:** Generates and displays a comprehensive YData Profiling Report within the app interface, offering detailed insights into the dataset's structure, summary statistics, and data quality issues.
    - **Loading Source:** The YData Profiling Report is loaded from an HTML files named generated by YData Profiling, ensuring accurate and detailed profiling results.
    """)

# YDTP Report 
def show_ydtp_report():
    st.header('YData Profiling Report')
    st.info(' ')
    with open("profrep.html", "r") as file:
        html_content = file.read()
    st.components.v1.html(html_content, height=8800, width=800)

# Render 
if selected_page == "Home":
    show_home()
elif selected_page == "Power-Bi Dashboard":
    show_pbi()
elif selected_page == "Docs":
    show_docs()
elif selected_page == "YDTP Report":
    show_ydtp_report() 

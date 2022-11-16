# dashboard-streamlit

## This repo aims to:
- Create a basic streamlit dashboard using [Diabetes Dataset](https://www.kaggle.com/datasets/akshaydattatraykhare/diabetes-dataset/code)


# Dependencies for Chosen Dataset:
- Date/time stamp 
- Categorical data
- Continuous data 
- OPTIONAL: position/locational data 


# Streamlit Dashboard Includes The Following Components:
- [Streamlit Documentation](https://docs.streamlit.io/library/api-reference)
- Header
- Titles 
- Code-block 
- 2 dataframes
- 2 charts (e.g., line, bar)


# Setup Streamlit on Azure
- using my setup instructions detailed in **setup_Azure_streamlit.md**
- [Streamlit Documentation](https://docs.streamlit.io/library/api-reference)
- git clone [repo url]
- cd to dashboard-streamlit
- Install and Import Python File:
-       streamlit run app.py 
- Displays: [IP Address:8501] >> Error: port 8501 is not open (the default port for streamlit)
- Open port 8501 by Opening **Networking** Tab, 
- Add inbound security rule:
    - Destination port ranges: 8501
- Add inbound security rule:
    - Destination port ranges: 8502


# Images folder 
- Contains screenshots of my live streamlit dashboard
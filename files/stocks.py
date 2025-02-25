import pandas as pd
import streamlit as st
import plotly.express as px

kse_100 = pd.read_csv(r'files/filteredData/adam sugar mills stock 2002-2022.csv')
adam_sugar_mill = pd.read_csv(r'files/filteredData/adam sugar mills stock 2002-2022.csv')
allied_bank = pd.read_csv(r'files/filteredData/adam sugar mills stock 2002-2022.csv')
nbp_bank = pd.read_csv(r'files/filteredData/NBP stock 2001-2022.csv')
k_electric = pd.read_csv(r'files/filteredData/K Electric Stock.csv')
js_bank = pd.read_csv(r'files/filteredData/JS bank 2007-2022.csv')
hum_network = pd.read_csv(r'files/filteredData/Hum network stock 2007-2022.csv')
honda = pd.read_csv(r'files/filteredData/honda stock 2001-2022.csv')
habib_bank = pd.read_csv(r'files/filteredData/habib bank stock 2007-2022.csv')
faysal_bank= pd.read_csv(r'files/filteredData/Faysal Bank stock 2001-2022.csv')
fauji_fertilizer = pd.read_csv(r'files/filteredData/Fauji fertilizer stock 2001-2022.csv')
fatima_enterprise = pd.read_csv(r'files/filteredData/Fatima Enterprises Stock 2001-2022.csv')
engro_fertilizer = pd.read_csv(r'files/filteredData/Engro Fertilizers Stock 2014-2022.csv')
dg_khan = pd.read_csv(r'files/filteredData/DG Khan Cement 2001-2022.csv')
attock = pd.read_csv(r'files/filteredData/attock petroleum 2005-2022.csv')
askari = pd.read_csv(r'files/filteredData/askari bank stock 2001-2022.csv')

companies = sorted(['Adam Sugar Mill', 'Allied Bank', 'NBP Bank', ' K Electric', 'JS Bank', 'Hum Network',
             'Honda', 'Habib Bank', 'Faysal Bank', 'Fauji Fertilizer', 'Fatima Enterprise', 'Engro Fertilizer', 'DG Khan Cement',
             'Attock Petroleum', 'Askari Bank'])

def show():
    st.sidebar.header('Stocks')
    stock_selection = st.selectbox('Choose one:', options=['KSE 100 Index', 'Other Stocks'])
    chart_selection = st.sidebar.selectbox('Select a view: ', options=['Line plot', 'Bar chart', 'Both'])
    filter_selection = st.sidebar.selectbox('Select a filter: ', options=['Analyze by year', 'Analyze by name'])
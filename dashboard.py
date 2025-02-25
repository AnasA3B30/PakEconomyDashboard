import streamlit as st
import files.gdpfile as gd_page
import files.home as home
import  files.exchange_rates as exchange
import files.inflation as inflation
import files.imports_and_exports as ie
import files.stocks as stocks


#main page
st.set_page_config(
    page_title="Pakistan Economic Report",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded")


st.sidebar.title('Pakistan Economic Report')
st.sidebar.image(r'flag-symbolism-Pakistan-design-Islamic.webp')
st.sidebar.header('Menu')
page = st.sidebar.selectbox('Select indicator:',options=['Home','GDP', 'Exchange Rates', 'Inflation (2018 Onwards)','Stocks', 'Imports and Exports'])

#files handling
if page =='Home':
    home.show()
elif page =='GDP':
    gd_page.show()
elif page =='Exchange Rates':
    exchange.show()
elif page=='Stocks':
    stocks.show()
elif page=='Imports and Exports':
    ie.show()
elif page=='Inflation (2018 Onwards)':
    inflation.show()

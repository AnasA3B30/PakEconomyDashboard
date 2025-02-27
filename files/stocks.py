import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

kse_100 = pd.read_csv(r'files/filteredData/adam sugar mills stock 2002-2022.csv')
adam_sugar_mill = pd.read_csv(r'files/filteredData/adam sugar mills stock 2002-2022.csv')
allied_bank = pd.read_csv(r'files/filteredData/allied bank stock 2005-2022.csv')
nbp_bank = pd.read_csv(r'files/filteredData/NBP stock 2001-2022.csv')

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

companies = {'Adam Sugar Mill':adam_sugar_mill, 'Allied Bank':allied_bank, 'NBP Bank':nbp_bank, 'JS Bank':js_bank, 'Hum Network':hum_network,
             'Honda':honda, 'Habib Bank':habib_bank, 'Faysal Bank':faysal_bank, 'Fauji Fertilizer':fauji_fertilizer, 'Fatima Enterprise':fatima_enterprise, 'Engro Fertilizer':engro_fertilizer, 'DG Khan Cement':dg_khan,
             'Attock Petroleum':attock, 'Askari Bank':askari}
companies_names = sorted(list(companies.keys()))

def show():
    st.sidebar.header('Stocks')
    stock_selection = st.sidebar.selectbox('Choose one:', options=['KSE 100 Index', 'Other Stocks'])
    chart_selection = st.sidebar.radio('Select a view: ', options=['Line plot', 'Bar chart', 'Both'])
    if stock_selection=='KSE 100 Index':
        color_map = {'Open': '#A2C5E8', 'High': '#1B3B6F', 'Low': '#427AA1', 'Close': '#26547C', 'Volume': '#6497C8'}
        mode = st.selectbox('Choose trend view:', options=['General Trends','Yearly View'])
        if mode=='General Trends':
            bar_kse = go.Figure()
            line_kse = go.Figure()
            start, end = st.slider('Select a year range:', min_value=2000, max_value=2021, value=(2008, 2019))
            df = kse_100[(kse_100['Year']<=end)&(kse_100['Year']>=start)]
            data = df.groupby('Year',as_index=False)[['Open','High','Low','Close','Volume']].mean()
            metrics = st.sidebar.multiselect('Select a metric:', options=['Open', 'High', 'Low', 'Volume', 'Close'],default=['Open','Close'])
            for metric in metrics:
                bar_kse.add_trace(go.Bar(x=data['Year'],y=data[metric],name=metric,marker=dict(color=color_map.get(metric, 'gray'))))
                line_kse.add_trace(go.Scatter(x=data['Year'], y=data[metric], mode='lines+markers', name=metric, line=dict(color=color_map.get(metric, 'gray'), width=2)))
            bar_kse.update_layout(
                height=700,
                xaxis=dict(
                tickmode='array',
                tickvals=data['Year'],  # Ensures correct year labeling
                title='Year'
                )
            )
            line_kse.update_layout(
                height=700,
                xaxis=dict(
                    tickmode='array',
                    tickvals=data['Year'],  # Ensures correct year labeling
                    title='Year'
                )
            )
            if chart_selection == 'Line plot':

                st.plotly_chart(line_kse)
            elif chart_selection == 'Bar chart':

                st.plotly_chart(bar_kse)
            elif chart_selection=='Both':
                line_kse.update_layout(height=600)
                bar_kse.update_layout(height=600)
                col1, col2 = st.columns(2)
                with col1:
                    st.plotly_chart(line_kse)
                with col2:
                    st.plotly_chart(bar_kse)

        elif mode == 'Yearly View':
            year = st.number_input('Select a year"',min_value=2000, max_value=2021,value=2010)
            df = kse_100[kse_100['Year']==year]
            df = df.groupby('Month',as_index=False)[['Open','High','Low','Close','Volume']].mean()
            labels = {
                1:'January',
                2:'February',
                3:'March',
                4:'April',
                5:'May',
                6:'June',
                7:'July',
                8:'August',
                9:'September',
                10:'October',
                11:'November',
                12:'December'
            }
            df['MonthLabel'] = df['Month'].map(labels)
            metrics = st.sidebar.multiselect('Select a metric:', options=['Open', 'High', 'Low', 'Volume', 'Close'], default=['Open', 'Close'])

            bar_kse = go.Figure()
            line_kse = go.Figure()

            for metric in metrics:
                bar_kse.add_trace(go.Bar(x=df['Month'],y=df[metric],name=metric,marker=dict(color=color_map.get(metric, 'gray'))))
                line_kse.add_trace(go.Scatter(x=df['Month'], y=df[metric], mode='lines+markers', name=metric,line=dict(color=color_map.get(metric, 'gray'), width=2) ))

            bar_kse.update_layout(
                height=700,
                xaxis=dict(
                    title="Month",
                    tickmode="array",
                    tickvals=df['Month'],
                    ticktext=df['MonthLabel'],

                )
            )
            line_kse.update_layout(
                height=700,
                xaxis=dict(
                    title="Month",
                    tickmode="array",
                    tickvals=df['Month'],
                    ticktext=df['MonthLabel'],

                )
            )

            if chart_selection == 'Line plot':
                line_kse.update_layout(height=700)
                st.plotly_chart(line_kse)
            elif chart_selection == 'Bar chart':
                bar_kse.update_layout(height=700)
                st.plotly_chart(bar_kse)
            elif chart_selection == 'Both':
                line_kse.update_layout(height=600)
                bar_kse.update_layout(height=600)
                col1, col2 = st.columns(2)
                with col1:
                    st.plotly_chart(line_kse)
                with col2:
                    st.plotly_chart(bar_kse)

    elif stock_selection == 'Other Stocks':
        start, end = st.slider('Select a year range:', min_value=2000, max_value=2021, value=(2008, 2019))
        companies_selection = st.multiselect('Select the companies you want to analyze:', options=companies_names, default=['Allied Bank', 'NBP Bank', 'JS Bank',])
        line_companies = go.Figure()
        bar_companies = go.Figure()
        metrics = st.sidebar.multiselect('Select a metric:', options=['Open', 'High', 'Low', 'Volume', 'Close'],
                                         default=['Open', 'Close'])
        for name in companies_selection:
            df = companies[name]
            df = df[(df['Year']<=end)&(df['Year']>=start)]
            data = df.groupby('Year',as_index=False)[['Open','Close','High','Volume','Low']].mean()
            for metric in metrics:
                line_companies.add_trace(go.Scatter(x=data['Year'], y=data[metric], mode='lines', name=f'{name} {metric}'))
                bar_companies.add_trace(go.Bar(x=data['Year'], y=data[metric], name=f'{name} {metric}'))
            line_companies.update_layout(
                height=700
            )
            bar_companies.update_layout(
                height=700
            )
        if chart_selection=='Line plot':
            st.plotly_chart(line_companies)
        elif chart_selection == 'Bar chart':
            st.plotly_chart(bar_companies)
        elif chart_selection == 'Both':
            col1, col2 = st.columns(2)
            col1.plotly_chart(line_companies)
            col2.plotly_chart(bar_companies)



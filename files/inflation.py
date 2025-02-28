import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go


inflation_data = pd.read_csv(r'files/filteredData/inflation.csv')

def show():
    st.sidebar.header('Inflation Rates')

    mode = st.sidebar.radio('Choose a plot type', options=['Line plot', 'Bar plot'],)
    if mode == 'Line plot':
        st.header('Inflation Rates Trends')
        start, end = st.slider('Select a year range', min_value=2018, max_value=2024, value=(2018, 2021))
        filtered_data = inflation_data[(inflation_data['Year'] >= start) & (inflation_data['Year'] <= end)]
        countries = st.sidebar.multiselect('Select countries', options=inflation_data.RegionalMember.unique(),
                                   default='Pakistan')
        fig = go.Figure()
        for country in countries:
            country_data = filtered_data[filtered_data['RegionalMember'] == country]
            fig.add_trace(
                go.Scatter(
                    x=country_data['Year'],  # Keeping all data points
                    y=country_data['Inflation'],
                    mode='lines+markers',
                    name=country
                )

            )
        fig.update_layout(
            title="Inflation Trends by Country",
            legend_title="Countries",
            hovermode="x unified",
            xaxis=dict(
                title="Year",  # X-axis title font size
                tickfont=dict(size=18),
                tickmode='array',
                tickvals=list(range(start, end + 1))  # X-axis tick labels font size
            ),
            yaxis=dict(
                title="Inflation %",  # Y-axis title font size
                tickfont=dict(size=18)  # Y-axis tick labels font size
            ),
            font=dict(size=20)
        )
        st.plotly_chart(fig)

    elif mode == 'Bar plot':
        report_mode = st.sidebar.radio('Select mode', options=['By Country','By Year'])
        if report_mode == 'By Country':
            st.header('Inflation Rates by Country')
            country = st.sidebar.selectbox('Select a country',options=sorted(list(inflation_data['RegionalMember'].unique()),))
            report_data = inflation_data[inflation_data['RegionalMember']==country]
            st.plotly_chart(px.bar(report_data,x='Year',y='Inflation',labels={'Inflation':'Inflation %'},color='Year'))
        elif report_mode == 'By Year':
            st.header('Yearly Inflation Rates')
            year = st.sidebar.number_input(label='Select a year', min_value=2018,max_value=2024,value=2020)
            countries = st.sidebar.multiselect('Select a country', options=sorted(list(inflation_data['RegionalMember'].unique()),),default=['Pakistan','Afghanistan','India'] )
            filtered_data = inflation_data[(inflation_data['Year']==year)&(inflation_data['RegionalMember'].isin(countries))]
            st.plotly_chart(px.bar(filtered_data, x='RegionalMember',y='Inflation',labels={'Inflation': 'Inflation %'},color='Inflation'))
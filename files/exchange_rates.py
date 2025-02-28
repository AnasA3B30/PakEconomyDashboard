import pandas as pd
import streamlit as st
import plotly.graph_objects as go


exchange_file = pd.read_csv(r'files/filteredData/exchange_Rates.csv')
exchange_file = exchange_file.drop(columns='Unnamed: 0')

def show():
    st.header('Exchange Rates')
    start, end = st.slider('Select a year range', min_value=2000, max_value=2019, value=(2007, 2012))
    currencies = st.sidebar.multiselect('Select currencies for comparison', options=exchange_file.columns[1:-2],
                                default=['U.S. Dollar'])
    filtered = exchange_file[(exchange_file['Year'] >= start) & (exchange_file['Year'] <= end)]
    fig = go.Figure()
    for currency in currencies:
        fig.add_trace(
            go.Scatter(
                x=filtered['Year'],  # Keeping all data points
                y=filtered[currency],
                mode='lines+markers',
                name=currency
            )

        )
    fig.update_layout(

        legend_title="Currency",
        hovermode="x unified",
        xaxis=dict(
            title="Year",  # X-axis title font size
            tickfont=dict(size=18),
            tickmode = 'array',
            tickvals = list(range(start,end+1))# X-axis tick labels font size
        ),
        yaxis=dict(
            title="Amount (PKR)",  # Y-axis title font size
            tickfont=dict(size=18)  # Y-axis tick labels font size
        ),
        font=dict(size=20)
    )
    st.plotly_chart(fig)

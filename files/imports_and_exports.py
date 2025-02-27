import pandas as pd
import streamlit as st
import plotly.express as px

data_file = pd.read_csv(r'files/filteredData/imports and exports.csv')



def show():
    data_exports = data_file[['Year', 'Exports (% of GDP)', 'Exports']]
    data_imports = data_file[['Year', 'Imports (% of GDP)', 'Imports']]
    st.sidebar.header('Imports and Exports')
    start, end = st.slider('Select a year range',min_value=2000,max_value=2023,value=(2007,2015))
    data_imports = data_imports[(data_imports['Year']>=start)&(data_imports['Year']<=end)]
    data_exports = data_exports[(data_exports['Year'] >= start) & (data_exports['Year'] <= end)]
    indicator = st.sidebar.selectbox('Select an indicator: ', options=['Exports','Imports','Both'])


    if indicator == 'Exports':
        metric = st.sidebar.selectbox('Select an metric: ', options=['Value', '% of GDP', 'Both'])

        x = data_exports['Year']
        if metric == 'Value':
            view = st.sidebar.selectbox('Select a view: ', options=['Trends', 'Comparisons', 'Both'])
            y = data_exports['Exports']

            plot_line = px.line(x=x, y=y, labels={'y': 'Value USD', 'x': 'Year'}, height=700)
            plot_line.update_layout(
                xaxis=dict(
                    tickmode='array',
                    tickvals=list(range(start, end + 1))
                )
            )

            plot_bar = px.bar(data_exports,x=x, y=y, labels={'y': 'Value USD', 'x': 'Year'}, height=700,color_discrete_sequence=px.colors.sequential.Blues,color='Exports')
            plot_bar.update_layout(
                xaxis=dict(
                    tickmode='array',
                    tickvals=list(range(start, end + 1))
                )
            )

            if view == 'Trends':
                st.plotly_chart(plot_line)
            elif view == 'Comparisons':
                st.plotly_chart(plot_bar)
            else:
                col1, col2 = st.columns(2)
                col1.plotly_chart(plot_line)
                col2.plotly_chart(plot_bar)

        elif metric == '% of GDP':
            view = st.sidebar.selectbox('Select a view: ', options=['Trends', 'Comparisons', 'Both'])
            y = data_exports['Exports (% of GDP)']

            plot_line = px.line(x=x, y=y, labels={'y': 'Export as % of GDP', 'x': 'Year'}, height=700)
            plot_line.update_layout(
                xaxis=dict(
                    tickmode='array',
                    tickvals=list(range(start, end + 1))
                )
            )

            plot_bar = px.bar(data_exports,x=x, y=y, labels={'y': 'Export as % of GDP', 'x': 'Year'}, height=700,color_discrete_sequence=px.colors.sequential.Blues,color='Exports (% of GDP)')
            plot_bar.update_layout(
                xaxis=dict(
                    tickmode='array',
                    tickvals=list(range(start, end + 1))
                )
            )

            if view == 'Trends':
                st.plotly_chart(plot_line)
            elif view == 'Comparisons':
                st.plotly_chart(plot_bar)
            else:
                col1, col2 = st.columns(2)
                col1.plotly_chart(plot_line)
                col2.plotly_chart(plot_bar)
        elif metric == 'Both':
            y_val = data_exports['Exports']
            y_percent = data_exports['Exports (% of GDP)']
            view = st.sidebar.selectbox('Select a view: ', options=['Trends', 'Comparisons',])
            y_val_line = px.line(x=x,y=y_val,height=700,labels={'x':'Year', 'y':'Exports in USD'},color_discrete_sequence=px.colors.sequential.Blues_r)
            y_val_bar = px.bar(data_exports,x=x, y=y_val, height=700,labels={'x':'Year', 'y':'Exports in USD'},color_continuous_scale=px.colors.sequential.Blues,color='Exports')
            y_percent_line = px.line(x=x, y=y_percent, height=700,labels={'x':'Year', 'y':'Exports as % of GDP'})
            y_percent_bar = px.bar(data_exports,x=x, y=y_percent, height=700,labels={'x':'Year', 'y':'Exports as % of GDP'},color_discrete_sequence=px.colors.sequential.Blues,color='Exports (% of GDP)')
            col1, col2, = st.columns(2)

            if view == 'Trends':
                col1.plotly_chart(y_val_line)
                col2.plotly_chart(y_percent_line)
            elif view == 'Comparisons':
                col1.plotly_chart(y_val_bar)
                col2.plotly_chart(y_percent_bar)

    elif indicator == 'Imports':
        metric = st.sidebar.selectbox('Select an metric: ', options=['Value', '% of GDP', 'Both'])

        x = data_imports['Year']
        if metric == 'Value':
            view = st.sidebar.selectbox('Select a view: ', options=['Trends', 'Comparisons', 'Both'])
            y = data_imports['Imports']

            plot_line = px.line(x=x, y=y, labels={'y': 'Value USD', 'x': 'Year'}, height=700)
            plot_line.update_layout(
                xaxis=dict(
                    tickmode='array',
                    tickvals=list(range(start, end + 1))
                )
            )

            plot_bar = px.bar(x=x, y=y, labels={'y': 'Value USD', 'x': 'Year'}, height=700)
            plot_bar.update_layout(
                xaxis=dict(
                    tickmode='array',
                    tickvals=list(range(start, end + 1))
                )
            )

            if view == 'Trends':
                st.plotly_chart(plot_line)
            elif view == 'Comparisons':
                st.plotly_chart(plot_bar)
            else:
                col1, col2 = st.columns(2)
                col1.plotly_chart(plot_line)
                col2.plotly_chart(plot_bar)

        elif metric == '% of GDP':
            view = st.sidebar.selectbox('Select a view: ', options=['Trends', 'Comparisons', 'Both'])
            y = data_imports['Imports (% of GDP)']

            plot_line = px.line(x=x, y=y, labels={'y': 'Import as % of GDP', 'x': 'Year'}, height=700)
            plot_line.update_layout(
                xaxis=dict(
                    tickmode='array',
                    tickvals=list(range(start, end + 1))
                )
            )

            plot_bar = px.bar(x=x, y=y, labels={'y': 'Import as % of GDP', 'x': 'Year'}, height=700)
            plot_bar.update_layout(
                xaxis=dict(
                    tickmode='array',
                    tickvals=list(range(start, end + 1))
                )
            )

            if view == 'Trends':
                st.plotly_chart(plot_line)
            elif view == 'Comparisons':
                st.plotly_chart(plot_bar)
            elif view=='Both':
                col1, col2 = st.columns(2)
                col1.plotly_chart(plot_line)
                col2.plotly_chart(plot_bar)

        elif metric == 'Both':
            y_val = data_imports['Imports']
            y_percent = data_imports['Imports (% of GDP)']
            view = st.sidebar.selectbox('Select a view: ', options=['Trends', 'Comparisons',])
            y_val_line = px.line(x=x,y=y_val,height=700,labels={'x':'Year', 'y':'Imports in USD'})
            y_val_bar = px.bar(x=x, y=y_val, height=700,labels={'x':'Year', 'y':'Imports in USD'})
            y_percent_line = px.line(x=x, y=y_percent, height=700,labels={'x':'Year', 'y':'Imports as % of GDP'})
            y_percent_bar = px.bar(x=x, y=y_percent, height=700,labels={'x':'Year', 'y':'Imports as % of GDP'})
            col1, col2, = st.columns(2)

            if view == 'Trends':
                col1.plotly_chart(y_val_line)
                col2.plotly_chart(y_percent_line)
            elif view == 'Comparisons':
                col1.plotly_chart(y_val_bar)
                col2.plotly_chart(y_percent_bar)

    elif indicator == 'Both':
        x = data_exports['Year']
        metric = st.sidebar.selectbox('Select an metric: ', options=['Value', '% of GDP'])
        if metric == 'Value':
            y1 = data_imports['Imports']
            y2 = data_exports['Exports']
            line_1 = px.line(x=x, y=y1, height=700,labels={'x':'Year','y':'Imports'})
            line_2 = px.line(x=x, y=y2, height=700,labels={'x':'Year','y':'Exports'})
            bar_1 = px.bar(y1,x=x,y=y1,height=700,labels={'x':'Year','y':'Imports',},color='Imports')
            bar_2 = px.bar(y2,x=x,y=y2,height=700,labels={'x':'Year','y':'Exports'},color='Exports')
            view = st.sidebar.selectbox('Select a view: ', options=['Trends', 'Comparisons'])
            if view == 'Trends':
                col1, col2, = st.columns(2)
                col1.plotly_chart(line_1)
                col2.plotly_chart(line_2)
            elif view == 'Comparisons':
                col1, col2, = st.columns(2)
                col1.plotly_chart(bar_1)
                col2.plotly_chart(bar_2)
        elif metric == '% of GDP':
            view = st.sidebar.selectbox('Select a view: ', options=['Trends', 'Comparisons'])
            y1 = data_imports['Imports (% of GDP)']
            y2 = data_exports['Exports (% of GDP)']
            line_1 = px.line(x=x, y=y1, height=700, labels={'y': "Import as % of GDP"})
            line_2 = px.line(x=x, y=y2, height=700, labels={'y': "Export as % of GDP"})
            bar_1 = px.bar(y1,x=x, y=y1, height=700, labels={'y': "Import in USD"},color='Imports (% of GDP)')
            bar_2 = px.bar(y2,x=x, y=y2, height=700, labels={'y': "Export in USD"},color='Exports (% of GDP)')
            if view == 'Trends':
                col1, col2, = st.columns(2)
                col1.plotly_chart(line_1)
                col2.plotly_chart(line_2)
            elif view == 'Comparisons':
                col1, col2, = st.columns(2)
                col1.plotly_chart(bar_1)
                col2.plotly_chart(bar_2)


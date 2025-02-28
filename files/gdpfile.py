import streamlit as st
import pandas as pd
import  plotly.express as px
import plotly.graph_objects as go


gdp_data = pd.read_csv(r'files/filteredData/Pakistan GDP.csv')
gdp_years = list(gdp_data['Year'])
gdp_yearly = list(gdp_data['GDP'])
gdp_dict = dict(zip(gdp_years,gdp_yearly))

gdp_sector_wise =pd.read_csv(r'files/filteredData/gdpSector.csv')


def show():
    st.sidebar.header('National GDP Overview')

    #define filters for year and chart type selection
    select = st.sidebar.selectbox('Select your view:', options=['Cumulative Yearly GDP Report', 'Sector Wise GDP Report'])
    selection=None

    if select=='Cumulative Yearly GDP Report':
        st.subheader('Cumulative Yearly GDP Report')
        start, end = st.slider('Select a year range', min_value=2000, max_value=2023, value=(2005, 2019))
        selection = st.sidebar.radio('Select a chart type:', options=['Line plot', 'Bar chart', 'Both'])
        metric1 = int(gdp_dict[end] - gdp_dict[start])
        metric1 = format(metric1, '.2e')
        metric2 = round(gdp_dict[end] / gdp_dict[start], 2)
        metric2 = str(metric2) + 'x'
        metric3 = (gdp_dict[end] - gdp_dict[start]) * 100 / gdp_dict[start]
        metric3 = round(metric3, 2)
        metric4 = round(int(metric3) / (end - start), 2)
        metric4 = str(metric4) + '%'
        metric3 = str(metric3) + '%'

        # filter data
        relevant_data = gdp_data.loc[(gdp_data['Year'] <= end) & (gdp_data['Year'] >= start)]

        # creating charts
        # line plot
        line_plot = px.line(relevant_data, x='Year', y='GDP')
        line_plot.update_layout(
            xaxis=dict(
                tickmode='array',
                tickvals=list(range(start, end + 1))
            )
        )
        # bar plot
        bar_plot = px.bar(relevant_data, x='Year', y='GDP',color='GDP')
        bar_plot.update_traces(showlegend=False, )
        bar_plot.update_layout(
            showlegend=False,
            xaxis=dict(
                tickmode='array',
                tickvals=[str(i) for i in range(start,end+1)]
            )
        )

        # dealing with user selection
        if selection == 'Line plot':
            st.plotly_chart(line_plot)

        elif selection == 'Bar chart':
            st.plotly_chart(bar_plot)

        else:


            col1, col2 = st.columns(2)
            col1.plotly_chart(line_plot)
            col2.plotly_chart(bar_plot)

        col1, col2, col3, col4 = st.columns(4)
        col2.metric("GDP Growth in USD", metric1, f'from {start} to {end}')
        col1.metric("GDP Growth", metric2,f'from {start} to {end}')
        col3.metric("GDP Growth %", metric3, f'from {start} to {end}')
        col4.metric('Avg Yearly Growth', metric4, f'from {start} to {end}')

    elif select=='Sector Wise GDP Report':
        st.subheader('Reports by sector')
        selection = st.sidebar.radio('Select a chart type:', options=['Sector Wise Trends', 'Sector Wise Distribution','Product Wise Trends', 'Product Wise Distribution', 'Yearly Pie Chart'])
        if selection=='Sector Wise Distribution':
            year = st.selectbox('Select a year to analyze', options=list(range(2000, 2019)))
            sector_data = gdp_sector_wise[gdp_sector_wise['Year']==year]
            plot_data=sector_data.groupby('Sector', as_index=False)['Amount'].sum()
            bar_c=px.bar(plot_data,title='Value in PKR',x='Sector',y='Amount',color='Sector',color_discrete_sequence=['#E0F7FA', '#81D4FA', '#0277BD']
)
            st.plotly_chart(bar_c)
        elif selection=='Product Wise Distribution':
            year = st.selectbox('Select a year to analyze', options=list(range(2000, 2019)))
            sector_data = gdp_sector_wise[gdp_sector_wise['Year'] == year]
            plot_data = sector_data.groupby('Product', as_index=False)['Amount'].sum()

            # Bar chart with colors
            bar_c = px.bar(
                plot_data,
                x='Product',
                y='Amount',
                title='Value in PKR',

                color='Product',  # Different colors for products
                color_discrete_sequence=px.colors.sequential.Blues  # Distinct colors
            )
            st.plotly_chart(bar_c)
        elif selection == 'Sector Wise Trends': #did this last cause I needed time to figure this out
            products = st.sidebar.multiselect('Select Sector',options=sorted(gdp_sector_wise['Sector'].unique()),default='Agriculture')
            start,end = st.slider('Select a year range',min_value=2000,max_value=2018,value=(2007,2012))
            relevant_data = gdp_sector_wise[(gdp_sector_wise['Year']>=start)&(gdp_sector_wise['Year']<=end)]
            fig = px.line()
            for product in products:
                product_data = relevant_data[relevant_data['Sector']==product]
                product_data = dict(product_data.groupby('Year')['Amount'].sum().reset_index())
                fig.add_trace(
                    go.Scatter(
                        x=product_data['Year'],  # Keeping all data points
                        y=product_data['Amount'],
                        mode='lines+markers',
                        name=product
                    )

                )
            fig.update_layout(
                title="Sector Wise GDP Trends",
                legend_title="Sector",
                hovermode="x unified",
                xaxis=dict(
                    title="Year",  # X-axis title font size
                    tickfont=dict(size=18) # X-axis tick labels font size
                ),
                yaxis=dict(
                    title="Amount (PKR)",  # Y-axis title font size
                    tickfont=dict(size=18)  # Y-axis tick labels font size
                ),
                font = dict(size=20)
            )
            st.plotly_chart(fig)



        elif selection == 'Product Wise Trends':  # did this last cause i needed time to figure this out

            products = st.sidebar.multiselect('Select Product', options=sorted(gdp_sector_wise['Product'].unique()),
                                              default='Small Scale Manufacturing')

            start, end = st.slider('Select a year range', min_value=2000, max_value=2018, value=(2007, 2012))

            relevant_data = gdp_sector_wise[(gdp_sector_wise['Year'] >= start) & (gdp_sector_wise['Year'] <= end)]

            fig = px.line()

            for product in products:
                product_data = relevant_data[relevant_data['Product'] == product]

                product_data = dict(product_data.groupby('Year')['Amount'].sum().reset_index())

                fig.add_trace(

                    go.Scatter(

                        x=product_data['Year'],  # Keeping all data points

                        y=product_data['Amount'],

                        mode='lines+markers',

                        name=product,

                    )

                )

            fig.update_layout(

                title="Product Wise GDP Trends",

                legend_title="Product",

                hovermode="x unified",

                xaxis=dict(

                    title="Year",  # X-axis title font size

                    tickfont=dict(size=18)  # X-axis tick labels font size

                ),

                yaxis=dict(

                    title="Amount (PKR)",  # Y-axis title font size

                    tickfont=dict(size=18)  # Y-axis tick labels font size

                ),

                font=dict(size=20),

            )

            st.plotly_chart(fig)


        elif selection=='Yearly Pie Chart':
            year = st.number_input('Select a year (2000-2019)', min_value=2000,max_value=2019,value=2007)
            st.subheader(f'Now displaying pie charts for year {year}.')
            df = gdp_sector_wise[gdp_sector_wise['Year']==year]
            st.subheader('By Sectors')
            st.plotly_chart(px.pie(df,values='Amount',names='Sector',hole=0.5,color_discrete_sequence=['#E0F7FA', '#81D4FA', '#0277BD'],width=500,height=500))
            st.divider()
            st.subheader('By Products')
            st.plotly_chart(px.pie(df,values='Amount',names='Product',color_discrete_sequence=px.colors.sequential.Teal,width=500,height=500))




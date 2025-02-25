import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import  plotly.express as px

gdp_2023 =337460000000
gdp_2024 = 374600000000
covid_gdp = 300000000000
formatted_2024 = format(gdp_2024, ',')
formatted_2023 = format(gdp_2023,',')
formatted_covid = format(covid_gdp,',')


diff = gdp_2024-gdp_2023
formatted_diff = format(diff,',')
diff_from_covid = gdp_2024-covid_gdp
formatted_diff_covid = format(diff_from_covid,',')
diff_exp = format(gdp_2024-gdp_2023,'.2e')
diff_exp_covid = format(gdp_2024-covid_gdp,'.2e')

growth_with_reference = round(gdp_2024/gdp_2023,2)
growth_with_reference_covid = round(gdp_2024/covid_gdp,2)

gdp_growth_rate = (gdp_2024-gdp_2023)*100/gdp_2023
gdp_growth_rate = round(gdp_growth_rate,2)
gdp_growth_rate = str(gdp_growth_rate)+'%'
gdp_growth_rate_covid = (gdp_2024-covid_gdp)*100/gdp_2023
gdp_growth_rate_covid = round(gdp_growth_rate_covid,2)
gdp_growth_rate_covid = str(gdp_growth_rate_covid)+'%'

metric2_val = formatted_2024 + ' USD'
metric2_diff = formatted_diff + ' USD from 2023'
metric_val_covid = formatted_2024 + ' USD'
metric_diff_covid = str(formatted_diff_covid) + ' USD from 2020'


def show():

    st.header('Economy Report of Pakistan')
    st.markdown('<p style="font-size: 20px;">Here is a brief summary of current, pandemic and immediate post-pandemic economic situation of Pakistan.</p>', unsafe_allow_html=True)
    main1, main2, main3, main4 = st.columns(4)
    with main1:
        st.markdown("""
            <div style="padding:10px; border-radius:10px; background-color:#f8f9fa; 
                        box-shadow: 2px 2px 10px #ddd; text-align: center;">
                <h3 style="color:#333;">24th Largest Economy</h3>
                <p style="color:#333;">Based on PPP</p>
            </div>
            """, unsafe_allow_html=True)

    with main2:
        st.markdown("""
            <div style="padding:10px; border-radius:10px; background-color:#f8f9fa; 
                        box-shadow: 2px 2px 10px #ddd; text-align: center;">
                <h3 style="color:#333;">43rd Largest Economy</h3>
                <p style="color:#333;">Based on Nominal GDP</p>
            </div>
            """, unsafe_allow_html=True)

    with main3:
        st.markdown("""
            <div style="padding:10px; border-radius:10px; background-color:#f8f9fa; 
                        box-shadow: 2px 2px 10px #ddd; text-align: center;">
                <h3 style="color:#333;">161st Ranked Economy</h3>
                <p style="color:#333;">By Nominal GDP per Capita</p>
            </div>
            """, unsafe_allow_html=True)

    with main4:
        with st.container():
            st.markdown("""
                <div style="padding:10px; border-radius:10px; background-color:#f8f9fa; 
                            box-shadow: 2px 2px 10px #ddd; text-align: center;">
                    <h3 style="color:#333;">138th Ranked Economy</h3>
                    <p style="color:#333;">By GDP PPP</p>
                </div>
                """, unsafe_allow_html=True)

    st.divider()

    #WRT to 2023
    st.subheader('Post-COVID Overview')
    col1,col2,col3,col4 = st.columns(4)
    col2.metric('GDP 2024', metric2_val, metric2_diff)
    col1.metric('GDP 2023', formatted_2023+' USD')
    col3.metric('GDP Growth', str(growth_with_reference)+'x', 'From 2023')
    col4.metric('GDP Growth Rate Yearly',gdp_growth_rate, 'From 2023')
    st.divider()

    #WRT Covid Years
    st.subheader('During COVID Overview (2020 as reference)')
    col5, col6, col7, col8 = st.columns(4)
    col6.metric('GDP 2024', metric_val_covid, metric_diff_covid)
    col5.metric('GDP COVID', formatted_covid + ' USD')
    col7.metric('GDP Growth', str(growth_with_reference_covid) + 'x', 'From COVID')
    col8.metric('GDP Growth Rate Yearly', gdp_growth_rate_covid, 'From COVID')


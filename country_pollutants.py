import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.io as pio
pio.templates.default = "plotly_dark"

df = pd.read_csv('air-pollution.csv', encoding='latin-1')

def pie_plot(category='', catg_type='', catg_aqi='', aqi_label='', title='', color=px.colors.sequential.Plotly3):

    # Filter by pollutant_category_type like Good or Moderate
    top_catg = df[df[category]==catg_type]

    # Sort by pollutant_aqi_value
    top_catg = top_catg.sort_values(catg_aqi, ascending=False)

    # Create the pie chart
    fig = px.pie(top_catg, values=catg_aqi, names='country',
                 title=title,
                 hover_data=[catg_aqi], labels={catg_aqi:aqi_label},
                 color_discrete_sequence=color)

    # Update the traces
    fig.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig)


def observations():
    with st.expander("OBSERVASI"):
        st.write(":blue[*Carbon Monoxide*]")
        st.write('''
            - Tidak ada negara yang lokasinya tergolong dalam kategori berisiko.
            - Dengan kinerja :green[**Good**] di semua negara, hanya Amerika Serikat yang memiliki
              Sedikit persentase lebih besar dalam :orange[**Unhealthy for Sensitive Groups category.**]
            ''')
    
        st.divider()
        st.write(":blue[*Ozone*]")
        st.write('''
            - China menunjukkan kondisi terburuk dengan kurang dari 40 persen wilayah yang dikategorikan dari :orange[**Unhealthy for Sensitive Groups to Very Unhealthy**]. 
            - Di saat yang sama, lebih dari 60 persen wilayah digambarkan masih dalam batas normal
              :green[**(Good to Moderate)**], sehingga situasinya tidak terlalu dramatis dibandingkan dengan "Indian AQI".
            - Berbicara tentang India, dalam kategori ini, lebih dari 70 persen wilayah memiliki kondisi :green[**Good O3**].
            ''')
    
        st.divider()
        st.write(':blue[*Nitrogen Dioxide*]')
        st.write('''
            - Kondisi yang relatif lebih buruk dengan tingkat :green[**Good NO2 levels (between 47 - 49)**] dapat ditemukan di
              negara-negara seperti Indonesia, Tiongkok, Amerika Serikat, dan Brasil.
            - Persentase kecil tingkat :green[**Moderate NO2**] dapat ditemukan di beberapa wilayah Amerika Serikat.
            ''')
    
        st.divider()
        st.write(':blue[*Atmospheric Particulate Matter*]')
        st.write('''
            - Kondisi terburuk dapat ditemukan di India, Tiongkok, Indonesia, Meksiko, dan Pakistan,
              di mana sebagian besar wilayahnya dikategorikan dalam :orange[**Unhealthy for Sensitive Groups to Very Unhealthy**]
            - Persentase yang sangat kecil dari wilayah di negara-negara tersebut memiliki tingkat :green[**Moderate PM2.5**] yang telah disebutkan sebelumnya
            - Negara-negara seperti India, Afrika Selatan, Rusia, Pakistan, dan Korea
              Selatan tercatat memiliki tingkat PM2.5 yang tinggi dalam kategori :red[**Hazardous**]. TSelatan tercatat memiliki tingkat PM2.5 yang tinggi dalam kategori
            ''')

import streamlit as st
from country_pollutants import pie_plot, observations
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
pio.templates.default = "plotly_dark"

# PAGE CONFIG
st.set_page_config(
    page_title="Kualitas Udara",
    page_icon="🍃")

# =========================
# SIDEBAR



st.sidebar.title("*Implementasi Dashboard Visualisasi Berbasis Web Sederhana*")

st.sidebar.markdown("About 👀")
st.sidebar.markdown(""" Website ini menampilkan tingkat polusi udara di seluruh dunia dengan menggunakan peta dan grafik interaktif untuk memperlihatkan Indeks Kualitas Udara (AQI) serta berbagai polutan seperti NO₂, CO, dan lainnya. Temukan ancaman tak kasat mata terhadap lingkungan kita dan pahami lebih baik udara yang kita hirup. """)

st.sidebar.divider()

#### Polusi udara
st.sidebar.header("Polusi Udara")
st.sidebar.markdown("""
<a href="https://mr22rzwisledm85muisvjn-polusiudarademoweb.streamlit.app/" target="_blank">
    <button style="background-color:#4CAF50; color:white; padding:10px 24px; border:none; border-radius:8px; cursor:pointer;">
        Buka Polusi Udara
    </button>
</a>
""", unsafe_allow_html=True)

# Finishing up with info panels 
st.sidebar.header("Resources ✨")
st.sidebar.info(
    """raw data dari [Kaggle](https://www.kaggle.com/datasets/hasibalmuzdadid/global-air-pollution-dataset)!"""
    )

st.sidebar.info(
    """
    icon idari [sini](https://icons8.com/icon/BIlYIKuOI6sm/air-pollution)
    """
    )

# =========================
# APP TITLE
c1, c2 = st.columns([0.2, 3.5], gap="large")

with c1:
    st.image(
        'icon.png',
        width=80,
    )

with c2:
    st.title("Pengecekan Kualitas Udara")
    st.markdown("*Visualizing Global Air Pollution Levels*")

# =========================
# Load the data
df = pd.read_csv('air-pollution.csv', encoding='latin-1', index_col=0)


# ============== PLOTS ==============

with st.expander("Tentang Polusi Udara"):
    st.write("""Polusi udara adalah pencemaran lingkungan dalam ruangan maupun luar ruangan  
             oleh zat kimia, fisik, atau biologis apa pun yang mengubah karakteristik alami atmosfer.""")

# ---- AQI on World Map ----
st.subheader("Global Air Quality Index (AQI) ☁")
st.info("""Peta dunia di bawah ini menunjukkan seberapa tercemarnya udara saat ini atau
seberapa tercemar udara yang diperkirakan akan terjadi.
Seiring meningkatnya tingkat polusi udara,
Indeks Kualitas Udara (AQI) juga meningkat, begitu pula risiko kesehatan masyarakat yang terkait.""")

world_aqi = pd.DataFrame(df.groupby("country")["aqi_value"].max())

fig = go.Figure(data=go.Choropleth(
    locations = df['country_code'].values.tolist(),
    z = world_aqi['aqi_value'].values.tolist(),
    text = df.index,
    colorscale = 'matter',  #Color_options: magenta, Agsunset, Tealgrn
    autocolorscale=False,
    marker_line_color='darkgray',
    marker_line_width=1,
    colorbar_title = 'AQI<br>Value',
))

fig.update_layout(
    geo=dict(
        showframe=True,
        showcoastlines=False,
        projection_type='natural earth'
    ),
    height=450,
    margin={"r":10,"t":0,"l":10,"b":50}
)

st.plotly_chart(fig)


# =========================
# ---- Exploring countries with diff. air pollutants' levels  ----

st.divider()
st.subheader("Negara-Negara dengan Tingkat Polutan Udara 🏭")
tab1, tab2, tab3, tab4 = st.tabs(["CO", "O3", "NO2", "PM2.5"])

with tab1:
    st.info("""Karbon Monoksida adalah gas yang tidak berwarna dan tidak berbau.  
            Di luar ruangan, gas ini terutama dilepaskan ke udara oleh mobil, truk,  
            dan kendaraan atau mesin lain yang membakar bahan bakar fosil.  
            Peralatan seperti pemanas ruang berbahan gas atau minyak tanah, serta kompor gas,  
            juga melepaskan CO yang memengaruhi kualitas udara dalam ruangan.""")
    
    st.markdown('#### Kualitas udara CO di berbagai negara!')
    choose_catg = st.selectbox('Select Kualitas Udara type 👇',
    ('Good', 'Moderate', 'Unhealthy for Sensitive Groups'))

    pie_plot(category='co_aqi_category', catg_type=choose_catg,
             catg_aqi='co_aqi_value', aqi_label='CO',
             title='CO Levels Globally')

with tab2:
    st.info("""Molekul Ozon berbahaya bagi kualitas udara luar ruangan (jika berada di luar lapisan ozon).  
            Ozon di permukaan tanah dapat menyebabkan berbagai masalah kesehatan seperti nyeri dada,  
            batuk, iritasi tenggorokan, dan peradangan saluran pernapasan.""")
    
    st.markdown('#### Kualitas udara O3 di berbagai negara!')
    choose_catg = st.selectbox('Select Kualiatas Udara type 👇',
    ('Good', 'Moderate', 'Unhealthy for Sensitive Groups', 'Unhealthy', 'Very Unhealthy'))

    pie_plot(category='ozone_aqi_category', catg_type=choose_catg,
             catg_aqi='ozone_aqi_value', aqi_label='O3',
             title='Ozone O3 Levels Globally', color=px.colors.sequential.haline)
    
with tab3:
    st.info("""Nitrogen Dioksida dapat masuk ke udara melalui fenomena alam  
            seperti masuknya gas dari stratosfer atau petir. Namun, di permukaan bumi,  
            NO2 terbentuk dari emisi mobil, truk, dan bus, pembangkit listrik,  
            serta peralatan luar ruangan. Paparan dalam waktu singkat dapat memperburuk  
            penyakit pernapasan seperti asma""")
    
    st.markdown('#### Kualitas udara NO2 di berbagai negara!')
    choose_catg = st.selectbox('Select Kualitas Udara type 👇',
    ('Good', 'Moderate'))

    pie_plot(category='no2_aqi_category', catg_type=choose_catg,
             catg_aqi='no2_aqi_value', aqi_label='NO2',
             title='NO2 Levels Globally', color=px.colors.sequential.haline)

with tab4:
    st.info("""Partikulat atmosfer, atau juga dikenal sebagai partikel aerosol atmosfer,  
            adalah campuran kompleks dari zat padat dan cair kecil yang terbawa ke udara.  
            Jika terhirup, partikel ini dapat menyebabkan masalah serius pada jantung dan paru-paru.""")
    
    st.markdown('#### kualitas udara PM2.5 di berbagai negara!')
    choose_catg = st.selectbox('Select Kualitas Udara type 👇',
    ('Good', 'Moderate', 'Unhealthy for Sensitive Groups', 'Unhealthy', 'Very Unhealthy', 'Hazardous'))

    pie_plot(category='pm2_5_aqi_category', catg_type=choose_catg,
             catg_aqi='pm2_5_aqi_value', aqi_label='PM2.5',
             title='PM2.5 Levels Globally')

# Insights for above pie plots
observations()

# =========================
# ---- 8 Countries whose top 15 cities shows diff. air pollutants' levels  ----

def plot_bar(coc='', aqi=''):
    """Plots a Seaborn barplot for ."""

    # Filter data for specific country
    df_coc = df[df['country_code'] == coc]

    # Filter data for pollutant values
    cont_plot = pd.DataFrame(df_coc.groupby("city")[aqi].max())

    sns.set_theme(style='dark')
    plt.style.use('dark_background')
    sns_fig = plt.figure(figsize=(40, 20))
    
    sns.barplot(x=cont_plot.index,
                y=cont_plot[aqi].values,
                order=cont_plot.sort_values(aqi,ascending=False).index[:15],
                palette=("cool"))
    st.pyplot(sns_fig)

st.divider()
st.subheader('Maximum Values from 8 Countries📊')

choose_coc = st.selectbox('Select a Country Code 👇',
    ('USA', 'IND', 'CHN', 'MYS', 'IDN', 'ZAF', 'RUS', 'BRA'))

st.success("""📌 USA: United States, IND: India, CHN: China,
           MYS: Malaysia, IDN: Indonesia, ZAF: South Africa,
           RUS: Russia, BRA: Brazil""")

col1, col2 = st.columns(2, gap='medium')

with col1:
    st.markdown(':blue[Top 15 Cities with max values of **CO**]')
    plot_bar(coc=choose_coc, aqi='co_aqi_value')

with col2:
    st.markdown('Top 15 Cities with max values of **O3**')
    plot_bar(coc=choose_coc, aqi='ozone_aqi_value')


col3, col4 = st.columns(2, gap='medium')

with col3:
    plot_bar(coc=choose_coc, aqi='no2_aqi_value')
    st.markdown('Top 15 Cities with max values of **NO2**')

with col4:
    plot_bar(coc=choose_coc, aqi='pm2_5_aqi_value')
    st.markdown(':blue[Top 15 Cities with max values of **PM2.5**]')

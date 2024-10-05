import streamlit as st 

st.set_page_config(layout="wide")

import pandas as pd

import numpy as np

import plotly.graph_objects as go

import plotly.express as px







st.write('''<br><br><br><center><font color = "#0000ff" size = 7>Daftar Artikel Mengenai Aplikasi Metode Partial Least Squares Structural Equation Modeling (PLS-SEM) di Berbagai Bidang Disiplin Ilmu</font></center>



             ''', unsafe_allow_html = True)

















st.write('''<style>
         a:hover {
         background-color: yellow;
         text-decoration: none;
         }
         </style>''', unsafe_allow_html=True)





pilih_topik = st.radio(
    "Pilih Bidang: ",
    [":rainbow[Accounting, Finance, Econometrics, Business (Financial Data)]",":rainbow[Business, Management, Education, Sociology and Political Science]" , ":rainbow[Psychology]", ":rainbow[Agriculture]", ":rainbow[Health]",      ])


if pilih_topik == ":rainbow[Accounting, Finance, Econometrics, Business (Financial Data)]":
    st.write('''<br><br><br><center><font color = "red" size = 7>2020</font></center> ''', unsafe_allow_html = True)

    st.write('''[1] <font color = "#0000ff">Judul: Disclosure of corporate social responsibility (CSR) and its implications on company value as a result of the impact of corporate governance and profitability</font><br><font color = "#ff00ff">Jurnal: International Journal of Law and Management</font><br><font color = "#f4c430">Tahun Terbit Artikel: 2020</font><br><font color = "#32cd32">Publisher: Emerald</font><br><a href = "https://www.emerald.com/insight/content/doi/10.1108/IJLMA-08-2017-0197/full/html" target = "_blank" style = "text-decoration:none">Link Artikel</a>



             ''', unsafe_allow_html = True)
    

    st.markdown(
    """<a href="https://www.emerald.com/insight/content/doi/10.1108/IJLMA-08-2017-0197/full/html">
    <img src="https://statkomat.com/aplikasi-plssem/Accounting, Finance, Econometrics, Business (Financial Data)/1/1.png" width="1000">
    </a>""",
    unsafe_allow_html=True)





































































if pilih_topik == ":rainbow[Business, Management, Education, Sociology and Political Science]":

    st.write('''<br><br><br><center><font color = "red" size = 7>2020</font></center> ''', unsafe_allow_html = True)

    st.write('''[1] <font color = "#0000ff">Judul: Business and project strategy alignment: ICT project success in Iran</font><br><font color = "#ff00ff">Jurnal: Technology in Society</font><br><font color = "#f4c430">Tahun Terbit Artikel: 2020</font><br><font color = "#32cd32">Publisher: Elsevier</font><br><a href = "https://www.sciencedirect.com/science/article/pii/S0160791X19307298?via%3Dihub" target = "_blank" style = "text-decoration:none">Link Artikel</a>



             ''', unsafe_allow_html = True)
    

    st.markdown(
    """<a href="https://www.sciencedirect.com/science/article/pii/S0160791X19307298?via%3Dihub">
    <img src="https://statkomat.com/aplikasi-plssem/Business, Management, Education, Sociology and Political Science/1/1.png" width="600"><br>
    <img src="https://statkomat.com/aplikasi-plssem/Business, Management, Education, Sociology and Political Science/1/2.png" width="600"><br>
    </a>""",
    unsafe_allow_html=True)


































































if pilih_topik == ":rainbow[Psychology]":

    st.write('''<br><br><br><center><font color = "red" size = 7>2024</font></center> ''', unsafe_allow_html = True)

    st.write('''[1] <font color = "#0000ff">Judul: The mediating role of employee commitment in the relationship between compensation system and turnover intentions</font><br><font color = "#ff00ff">Jurnal: Employee Relations</font><br><font color = "#f4c430">Tahun Terbit Artikel: 2024</font><br><font color = "#32cd32">Publisher: Emerald</font><br><a href = "https://www.emerald.com/insight/content/doi/10.1108/ER-05-2023-0270/full/html" target = "_blank" style = "text-decoration:none">Link Artikel</a>



             ''', unsafe_allow_html = True)
    

    st.markdown(
    """<a href="https://www.emerald.com/insight/content/doi/10.1108/ER-05-2023-0270/full/html">
    <img src="https://statkomat.com/aplikasi-plssem/Psychology/1/1.png" width="1000">
    </a>""",
    unsafe_allow_html=True)

















































































































































st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")




st.markdown(
    """<center><img src="https://statkomat.com/gambar/ugi.png" width="500"></center>
    <h2 style='text-align: justify; color: blue;'><center>Prana Ugiana Gio, Founder of <a href = 'https://statcal.com/' target = '_blank' style = 'text-decoration:none'><font color = 'orange'>STATCAL</a></center></h2>""",
    unsafe_allow_html=True)




col1, col2, col3, col4, col5, col6 = st.columns([2, 2, 2, 2, 2, 2])
with col1:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/logo_figshare2.png" width="50"><br><a href = 'https://figshare.com/authors/prana_ugiana_gio/17826386' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>FIGSHARE</b></font></center></a>""",unsafe_allow_html=True)
with col2:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/statkomat.gif" width="50"><br><a href = 'https://statkomat.com/download_tulisan.php' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>STATKOMAT</b></font></center></a>""",unsafe_allow_html=True)
with col3:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/youtube.png" width="50"><br><a href = 'https://www.youtube.com/@STATKOMAT/videos' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>YOUTUBE</b></font></center></a>""",unsafe_allow_html=True)
with col4:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/literature-review.gif" width="50"><br><a href = 'https://literaturereview.streamlit.app/' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>LITERATURE REVIEW</b></font></center></a>""",unsafe_allow_html=True)
with col5:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/list-papers.gif" width="50"><br><a href = 'https://daftar-paper.streamlit.app/' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>LIST OF JOURNALS</b></font></center></a>""",unsafe_allow_html=True)
with col6:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/my-papers.gif" width="50"><br><a href = 'https://ugi-publikasi.streamlit.app/' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>MY PAPERS</b></font></center></a>""",unsafe_allow_html=True)

st.markdown("")
st.markdown("")

col7, col8, col9, col10, col11, col12 = st.columns([2, 2, 2, 2, 2, 2])
with col7:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/pls-sem.gif" width="50"><br><a href = 'https://aplikasi-plssem.streamlit.app//' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>STRUCTURAL EQUATION MODELING (PLS-SEM)</b></font></center></a>""",unsafe_allow_html=True)
with col8:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/statcal.gif" width="50"><br><a href = 'https://statcal.com/' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>STATCAL</b></font></center></a>""",unsafe_allow_html=True)
with col9:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/shiny.gif" width="50"><br><a href = 'https://share-your-shiny-app.id/' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>SHINY</b></font></center></a>""",unsafe_allow_html=True)
with col10:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/ugi-gio.gif" width="50"><br><a href = 'https://ugi-gio.id/' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>UGI</b></font></center></a>""",unsafe_allow_html=True)
with col11:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/indcomp.gif" width="50"><br><a href = 'https://indcomp-stats.id/' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>INDCOMP</b></font></center></a>""",unsafe_allow_html=True)
with col12:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/github.png" width="50"><br><a href = 'https://github.com/gioprana89' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>GITHUB</b></font></center></a>""",unsafe_allow_html=True)







st.markdown("")
st.markdown("")

st.markdown("""<a href = 'https://saweria.co/statkomat' target = '_blank' style = 'text-decoration:none'><center><img src="https://statkomat.com/streamlit-ugi/kopi.gif" width="150"></center></a><br><center><b><a href = 'https://saweria.co/statkomat' target = '_blank' style = 'text-decoration:none'><font color = 'orange' size = 7>Buy Me a Cup of Coffee</font></a></b></font></center>""",unsafe_allow_html=True)
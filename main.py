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




col1, col2, col3 = st.columns(3)

st.image("https://statkomat.com/gambar/ugi.png", caption='', width = 350)

st.markdown("<a href = 'https://statkomat.com/download_tulisan.php' target = '_blank' style = 'text-decoration:none'><font color = 'orange'><b>STATKOMAT</b></font></a> | <a href = 'https://www.youtube.com/@STATKOMAT/videos' target = '_blank' style = 'text-decoration:none'><font color = 'orange'><b>YOUTUBE</b></font></a> | <a href = 'https://literaturereview.streamlit.app/' target = '_blank' style = 'text-decoration:none'><font color = 'orange'><b>LITERATURE REVIEW</b></font></a> | <a href = 'https://daftar-paper.streamlit.app/' target = '_blank' style = 'text-decoration:none'><font color = 'orange'><b>LIST OF PAPERS</b></font></a> | <a href = 'https://ugi-publikasi.streamlit.app/' target = '_blank' style = 'text-decoration:none'><font color = 'orange'><b>PUBLICATION</b></font></a> | <a href = 'https://aplikasi-plssem.streamlit.app//' target = '_blank' style = 'text-decoration:none'><font color = 'orange'><b>PLS-SEM</b></font></a> | <a href = 'https://statkomat.com/download_tulisan.php' target = '_blank' style = 'text-decoration:none'><font color = 'orange'><b>MY SOFTWARE</b></font></a> | <a href = 'https://statcal.com/' target = '_blank' style = 'text-decoration:none'><font color = 'orange'><b>MY BOOK</b></font></a> | <a href = 'https://ugi-gio.id/' target = '_blank' style = 'text-decoration:none'><font color = 'orange'><b>UGI</b></font></a> | <a href = 'https://share-your-shiny-app.id/' target = '_blank' style = 'text-decoration:none'><font color = 'orange'><b>SHINY</b></font></a> | <a href = 'https://indcomp-stats.id/' target = '_blank' style = 'text-decoration:none'><font color = 'orange'><b>INDCOMP</b></font></a> | <a href = 'https://figshare.com/authors/prana_ugiana_gio/17826386' target = '_blank' style = 'text-decoration:none'><font color = 'orange'><b>FIGSHARE</b></font></a> | <a href = 'https://github.com/gioprana89' target = '_blank' style = 'text-decoration:none'><font color = 'orange'><b>GITHUB</b></font></a>", unsafe_allow_html=True)


pilih_topik = st.radio(
    "Pilih Bidang: ",
    [":rainbow[Accounting, Finance, Econometrics, Business (Financial Data)]", ":rainbow[Psychology]", ":rainbow[Agriculture]",      ])


if pilih_topik == ":rainbow[Accounting, Finance, Econometrics, Business (Financial Data)]":
    st.write('''[1] <font color = "#0000ff">Judul: Disclosure of corporate social responsibility (CSR) and its implications on company value as a result of the impact of corporate governance and profitability</font><br><font color = "#ff00ff">Jurnal: International Journal of Law and Management</font><br><font color = "#f4c430">Tahun Terbit Artikel: 2020</font><br><font color = "#32cd32">Publisher: Emerald</font><br><a href = "https://www.emerald.com/insight/content/doi/10.1108/IJLMA-08-2017-0197/full/html" target = "_blank" style = "text-decoration:none">Link Artikel</a>



             ''', unsafe_allow_html = True)
    

    st.markdown(
    """<a href="https://www.emerald.com/insight/content/doi/10.1108/IJLMA-08-2017-0197/full/html">
    <img src="https://statkomat.com/aplikasi-plssem/Accounting, Finance, Econometrics, Business (Financial Data)/1/1.png" width="1000">
    </a>""",
    unsafe_allow_html=True)


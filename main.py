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

    st.write('''<br><br>[2] <font color = "#0000ff">Judul: Self-Efficacy and Social Support: Two Predictors of Teachers Resilience in Inclusive Elementary School</font><br><font color = "#ff00ff">Jurnal: Journal An-Nafs: Kajian Penelitian Psikologi</font><br><font color = "#f4c430">Tahun Terbit Artikel: 2024</font><br><font color = "#32cd32">Publisher: </font><br><a href = "https://ejournal.uit-lirboyo.ac.id/index.php/psikologi/article/view/5448" target = "_blank" style = "text-decoration:none">Link Artikel</a>



             ''', unsafe_allow_html = True)
    

    st.markdown(
    """<a href="https://ejournal.uit-lirboyo.ac.id/index.php/psikologi/article/view/5448">
    <img src="https://statkomat.com/aplikasi-plssem/Psychology/5/1.png" width="500">
    </a>""",
    unsafe_allow_html=True)























    st.write('''<br><br><br><center><font color = "red" size = 7>2022</font></center> ''', unsafe_allow_html = True)
    st.write('''[1] <font color = "#0000ff">Judul: Pengaruh Kepemimpinan Transformasional dan Keterlibatan Kerja terhadap Organizational Citizenship Behavior (OCB) melalui Mediator Kepuasan Kerja</font><br><font color = "#ff00ff">Jurnal: Psikologika: Jurnal Pemikiran dan Penelitian Psikologi</font><br><font color = "#f4c430">Tahun Terbit Artikel: 2022</font><br><font color = "#32cd32">Publisher: </font><br><a href = "https://journal.uii.ac.id/Psikologika/article/view/18706" target = "_blank" style = "text-decoration:none">Link Artikel</a>



             ''', unsafe_allow_html = True)
    

    st.markdown(
    """<a href="https://journal.uii.ac.id/Psikologika/article/view/18706">
    <img src="https://statkomat.com/aplikasi-plssem/Psychology/4/1.png" width="800"><br>
    </a>""",
    unsafe_allow_html=True)







    st.write('''<br><br><br><center><font color = "red" size = 7>2021</font></center> ''', unsafe_allow_html = True)
    st.write('''[1] <font color = "#0000ff">Judul: The influence of socioeconomic status on job and life satisfaction among low-income employees in Johor Local Authorities</font><br><font color = "#ff00ff">Jurnal: Psikohumaniora: Jurnal Penelitian Psikologi</font><br><font color = "#f4c430">Tahun Terbit Artikel: 2021</font><br><font color = "#32cd32">Publisher: </font><br><a href = "https://journal.walisongo.ac.id/index.php/Psikohumaniora/article/view/8304" target = "_blank" style = "text-decoration:none">Link Artikel</a>



             ''', unsafe_allow_html = True)
    

    st.markdown(
    """<a href="https://journal.walisongo.ac.id/index.php/Psikohumaniora/article/view/8304">
    <img src="https://statkomat.com/aplikasi-plssem/Psychology/2/1.png" width="500"><br>
    <img src="https://statkomat.com/aplikasi-plssem/Psychology/2/2.png" width="800">
    </a>""",
    unsafe_allow_html=True)








    st.write('''<br><br><br><center><font color = "red" size = 7>2020</font></center> ''', unsafe_allow_html = True)
    st.write('''[1] <font color = "#0000ff">Judul: The effect of self-esteem, attitude towards the body, and eating habit on cognitive reactivity</font><br><font color = "#ff00ff">Jurnal: Psikohumaniora: Jurnal Penelitian Psikologi</font><br><font color = "#f4c430">Tahun Terbit Artikel: 2020</font><br><font color = "#32cd32">Publisher: </font><br><a href = "https://journal.walisongo.ac.id/index.php/Psikohumaniora/article/view/4561" target = "_blank" style = "text-decoration:none">Link Artikel</a>



             ''', unsafe_allow_html = True)
    

    st.markdown(
    """<a href="https://journal.walisongo.ac.id/index.php/Psikohumaniora/article/view/4561">
    <img src="https://statkomat.com/aplikasi-plssem/Psychology/3/1.png" width="800"><br>
    </a>""",
    unsafe_allow_html=True)




































































































































if pilih_topik == ":rainbow[Agriculture]":





    st.write('''<br><br><br><center><font color = "red" size = 7>2024</font></center> ''', unsafe_allow_html = True)
    st.write('''[1] <font color = "#0000ff">Judul: Pengaruh Penyuluhan terhadap Dampak Sosial Ekonomi Petani Penerima Bantuan Sarana Prasarana Pertanian di Kota Palopo</font><br><font color = "#ff00ff">Jurnal: Jurnal Penyuluhan</font><br><font color = "#f4c430">Tahun Terbit Artikel: 2024</font><br><font color = "#32cd32">Publisher: </font><br><a href = "https://journal.ipb.ac.id/index.php/jupe/article/view/47989" target = "_blank" style = "text-decoration:none">Link Artikel</a>



             ''', unsafe_allow_html = True)
    
    st.markdown(
    """<a href="https://journal.ipb.ac.id/index.php/jupe/article/view/47989">
    <img src="https://statkomat.com/aplikasi-plssem/Agriculture/8/1.png" width="700"><br>
    <img src="https://statkomat.com/aplikasi-plssem/Agriculture/8/2.png" width="600"><br>
    <img src="https://statkomat.com/aplikasi-plssem/Agriculture/8/3.png" width="600"><br>
    <img src="https://statkomat.com/aplikasi-plssem/Agriculture/8/4.png" width="600"><br>
    <img src="https://statkomat.com/aplikasi-plssem/Agriculture/8/5.png" width="600"><br>
    </a>""",
    unsafe_allow_html=True)













    st.write('''<br><br><br><center><font color = "red" size = 7>2023</font></center> ''', unsafe_allow_html = True)
    st.write('''[1] <font color = "#0000ff">Judul: Faktor yang Mempengaruhi Penggunaan Smartphone oleh Petani Padi Sawah di Kota Padang Sidimpuan Provinsi Sumatera Utara</font><br><font color = "#ff00ff">Jurnal: Jurnal Agro Ekonomi</font><br><font color = "#f4c430">Tahun Terbit Artikel: 2023</font><br><font color = "#32cd32">Publisher: </font><br><a href = "https://epublikasi.pertanian.go.id/berkala/jae/article/view/3558" target = "_blank" style = "text-decoration:none">Link Artikel</a>



             ''', unsafe_allow_html = True)
    
    st.markdown(
    """<a href="https://epublikasi.pertanian.go.id/berkala/jae/article/view/3558">
    <img src="https://statkomat.com/aplikasi-plssem/Agriculture/1/1.png" width="700"><br>
    <img src="https://statkomat.com/aplikasi-plssem/Agriculture/1/2.png" width="600"><br>
    <img src="https://statkomat.com/aplikasi-plssem/Agriculture/1/3.png" width="600"><br>
    </a>""",
    unsafe_allow_html=True)





    st.write('''<br><br><br>[2] <font color = "#0000ff">Judul: THE EFFECTIVENESS OF THE ROLE OF FARMERS' GROUP ON THE PERFORMANCE OF RICE FARMING IN KEMUMU VILLAGE, ARMA JAYA DISTRICT, NORTH BENGKULU REGENCY</font><br><font color = "#ff00ff">Jurnal: Jurnal AGRISEP: Kajian Masalah Sosial Ekonomi Pertanian dan Agribisnis</font><br><font color = "#f4c430">Tahun Terbit Artikel: 2023</font><br><font color = "#32cd32">Publisher: </font><br><a href = "https://ejournal.unib.ac.id/agrisep/article/view/25958" target = "_blank" style = "text-decoration:none">Link Artikel</a>



             ''', unsafe_allow_html = True)
    
    st.markdown(
    """<a href="https://ejournal.unib.ac.id/agrisep/article/view/25958">
    <img src="https://statkomat.com/aplikasi-plssem/Agriculture/2/1.png" width="700"><br>
    <img src="https://statkomat.com/aplikasi-plssem/Agriculture/2/2.png" width="600"><br>
    <img src="https://statkomat.com/aplikasi-plssem/Agriculture/2/3.png" width="600"><br>
    </a>""",
    unsafe_allow_html=True)




    st.write('''<br><br><br>[3] <font color = "#0000ff">Judul: THE ROLE OF AGRICULTURAL EXTENSIONERS AND AGRICULTURAL FARMER CHARACTERISTICS ON THE BEHAVIOR OF RICE SEED FARMERS IN BUNGA RAYA DISTRICT, SIAK REGENCY</font><br><font color = "#ff00ff">Jurnal: AGRISOCIONOMICS: Jurnal Sosial Ekonomi dan Kebijakan Pertanian</font><br><font color = "#f4c430">Tahun Terbit Artikel: 2023</font><br><font color = "#32cd32">Publisher: </font><br><a href = "https://ejournal2.undip.ac.id/index.php/agrisocionomics/article/view/17302" target = "_blank" style = "text-decoration:none">Link Artikel</a>



             ''', unsafe_allow_html = True)
    
    st.markdown(
    """<a href="https://ejournal.unib.ac.id/agrisep/article/view/25958">
    <img src="https://statkomat.com/aplikasi-plssem/Agriculture/5/1.png" width="700"><br>
    <img src="https://statkomat.com/aplikasi-plssem/Agriculture/5/2.png" width="600"><br>
    </a>""",
    unsafe_allow_html=True)





    st.write('''<br><br><br>[4] <font color = "#0000ff">Judul: Analisis Pengaruh Motivasi dan Penyuluhan Petani terhadap Usahatani Porang di Madiun Jawa Timur</font><br><font color = "#ff00ff">Jurnal: Jurnal Penyuluhan</font><br><font color = "#f4c430">Tahun Terbit Artikel: 2023</font><br><font color = "#32cd32">Publisher: </font><br><a href = "https://journal.ipb.ac.id/index.php/jupe/article/view/46744" target = "_blank" style = "text-decoration:none">Link Artikel</a>



             ''', unsafe_allow_html = True)
    
    st.markdown(
    """<a href="https://journal.ipb.ac.id/index.php/jupe/article/view/46744">
    <img src="https://statkomat.com/aplikasi-plssem/Agriculture/6/1.png" width="700"><br>
    <img src="https://statkomat.com/aplikasi-plssem/Agriculture/6/2.png" width="600"><br>
    <img src="https://statkomat.com/aplikasi-plssem/Agriculture/6/3.png" width="600"><br>
    <img src="https://statkomat.com/aplikasi-plssem/Agriculture/6/4.png" width="600"><br>
    </a>""",
    unsafe_allow_html=True)




    st.write('''<br><br><br>[5] <font color = "#0000ff">Judul: Peningkatan Kinerja Digital Penyuluh Pertanian Dinas Pertanian dan Pangan Kabupaten Banyuwangi Jawa Timur</font><br><font color = "#ff00ff">Jurnal: Jurnal Penyuluhan</font><br><font color = "#f4c430">Tahun Terbit Artikel: 2023</font><br><font color = "#32cd32">Publisher: </font><br><a href = "https://journal.ipb.ac.id/index.php/jupe/article/view/46275" target = "_blank" style = "text-decoration:none">Link Artikel</a>



             ''', unsafe_allow_html = True)
    
    st.markdown(
    """<a href="https://journal.ipb.ac.id/index.php/jupe/article/view/46275">
    <img src="https://statkomat.com/aplikasi-plssem/Agriculture/7/1.png" width="700"><br>
    <img src="https://statkomat.com/aplikasi-plssem/Agriculture/7/2.png" width="600"><br>
    <img src="https://statkomat.com/aplikasi-plssem/Agriculture/7/3.png" width="600"><br>
    <img src="https://statkomat.com/aplikasi-plssem/Agriculture/7/4.png" width="600"><br>
    </a>""",
    unsafe_allow_html=True)









    st.write('''<br><br><br><center><font color = "red" size = 7>2022</font></center> ''', unsafe_allow_html = True)
    st.write('''[1] <font color = "#0000ff">Judul: Pengaruh Motivasi, Disiplin Kerja, dan Kepuasan Kerja terhadap Kinerja Pegawai Direktorat Perbenihan Tanaman Pangan, Kementerian Pertanian Jakarta</font><br><font color = "#ff00ff">Jurnal: Owner: Riset & Jurnal Akuntansi</font><br><font color = "#f4c430">Tahun Terbit Artikel: 2022</font><br><font color = "#32cd32">Publisher: </font><br><a href = "https://www.researchgate.net/publication/359987013_Pengaruh_Motivasi_Disiplin_Kerja_dan_Kepuasan_Kerja_terhadap_Kinerja_Pegawai_Direktorat_Perbenihan_Tanaman_Pangan_Kementerian_Pertanian_Jakarta#fullTextFileContent" target = "_blank" style = "text-decoration:none">Link Artikel</a>



             ''', unsafe_allow_html = True)
    
    st.markdown(
    """<a href="https://epublikasi.pertanian.go.id/berkala/jae/article/view/3558">
    <img src="https://statkomat.com/aplikasi-plssem/Agriculture/1/1.png" width="700"><br>
    <img src="https://statkomat.com/aplikasi-plssem/Agriculture/1/2.png" width="600"><br>
    <img src="https://statkomat.com/aplikasi-plssem/Agriculture/1/3.png" width="600"><br>
    </a>""",
    unsafe_allow_html=True)









    st.write('''<br><br><br><center><font color = "red" size = 7>2020</font></center> ''', unsafe_allow_html = True)
    st.write('''[1] <font color = "#0000ff">Judul: KARAKTERISTIK PENYULUH DALAM PEMANFAATAN MEDIA SOSIAL SEBAGAI MEDIA INFORMASI PERTANIAN</font><br><font color = "#ff00ff">Jurnal: AGRISOCIONOMICS: Jurnal Sosial Ekonomi dan Kebijakan Pertanian</font><br><font color = "#f4c430">Tahun Terbit Artikel: 2020</font><br><font color = "#32cd32">Publisher: </font><br><a href = "https://ejournal2.undip.ac.id/index.php/agrisocionomics/article/view/6113" target = "_blank" style = "text-decoration:none">Link Artikel</a>



             ''', unsafe_allow_html = True)
    
    st.markdown(
    """<a href="https://epublikasi.pertanian.go.id/berkala/jae/article/view/3558">
    <img src="https://statkomat.com/aplikasi-plssem/Agriculture/4/1.png" width="700"><br>
    <img src="https://statkomat.com/aplikasi-plssem/Agriculture/4/2.png" width="600"><br>
    <img src="https://statkomat.com/aplikasi-plssem/Agriculture/4/3.png" width="600"><br>
    </a>""",
    unsafe_allow_html=True)






















    st.write('''<br><br><br><center><font color = "red" size = 7>2019</font></center> ''', unsafe_allow_html = True)
    st.write('''[1] <font color = "#0000ff">Judul: PENGARUH DISIPLIN KERJA, KEPUASAN KERJA DAN LOYALITAS KARYAWAN TERHADAP KINERJA KARYAWAN AGROWISATA BAGUS AGRO PELAGA</font><br><font color = "#ff00ff">Jurnal: AGRISOCIONOMICS: Jurnal Sosial Ekonomi dan Kebijakan Pertanian</font><br><font color = "#f4c430">Tahun Terbit Artikel: 2019</font><br><font color = "#32cd32">Publisher: </font><br><a href = "https://ejournal2.undip.ac.id/index.php/agrisocionomics/article/view/4801" target = "_blank" style = "text-decoration:none">Link Artikel</a>



             ''', unsafe_allow_html = True)
    
    st.markdown(
    """<a href="https://epublikasi.pertanian.go.id/berkala/jae/article/view/3558">
    <img src="https://statkomat.com/aplikasi-plssem/Agriculture/3/1.png" width="700"><br>
    <img src="https://statkomat.com/aplikasi-plssem/Agriculture/3/2.png" width="600"><br>
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

col13, col14, col15, col16, col17, col18 = st.columns([2, 2, 2, 2, 2, 2])
with col13:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/cfa.gif" width="50"><br><a href = 'https://cfa-aplikasi.streamlit.app/' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>CONFIRMATORY FACTOR ANALYSIS (CFA)</b></font></center></a>""",unsafe_allow_html=True)





st.markdown("")
st.markdown("")

st.markdown("""<a href = 'https://saweria.co/statkomat' target = '_blank' style = 'text-decoration:none'><center><img src="https://statkomat.com/streamlit-ugi/kopi.gif" width="150"></center></a><br><center><b><a href = 'https://saweria.co/statkomat' target = '_blank' style = 'text-decoration:none'><font color = 'orange' size = 7>Buy Me a Cup of Coffee</font></a></b></font></center>""",unsafe_allow_html=True)

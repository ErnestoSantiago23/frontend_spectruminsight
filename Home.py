import streamlit as st

st.set_page_config(
    page_title="SpectrumInsight",
    page_icon="https://as1.ftcdn.net/v2/jpg/06/73/98/70/1000_F_673987016_XJuf04WTeSXl8zWRQgEsDEIs5lScsG5D.jpg",
)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Aplicar el CSS
local_css("style.css")



st.markdown('<style>h1{color: whith;}</style>', unsafe_allow_html=True)
st.markdown('<h1>Welcome to SpectrumInsight! 👋</h1>', unsafe_allow_html=True)

st.markdown(
    """
    We are delighted that you are joining us on this journey of discovery and understanding.
    SpectrumInsight is designed to be an ally on the road to a better understanding of the autism spectrum.
    Here, you will find carefully crafted tools to help you better assess and understand each child's unique characteristics.

    Our mission is to provide a safe, informative and easy-to-use environment to support you in this important process.

"""
)

st.image('https://www.impaqto.net/wp-content/uploads/2016/04/manos-ok.jpg',
         caption='Autism')

url = 'https://www.youtube.com/watch?v=jpk1_JK2WZM'
st.video(url)

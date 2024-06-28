import streamlit as st
import requests
import streamlit.components.v1 as components

# GITHUB_REPO = 'https://github.com/Saurav-Krishna/Portfolio-Projects/blob/main/main.html'
# def fetch_html(url):
#     response = requests.get(url)
#     response.raise_for_status()
#     return response.text

html_file = 'main.html'
def main():
    st.title("Restaurant success Analysis")

    try:
        with open(html_file,'r',encoding='utf-8') as file:
            html_content = file.read()
        components.html(html_content,height=800,scrolling=True)
        # st.markdown(html_content, unsafe_allow_html=True)
    except requests.exceptions.RequestException as e:
        st.error(f'Error fetching HTML file: {e}')


if __name__ == '__main__':
    main()
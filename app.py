import streamlit as st
import requests

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
        st.markdown(html_content, unsafe_allow_html=True)
    except requests.exceptions.RequestException as e:
        st.error(f'Error fetching HTML file: {e}')


if __name__ == '__main__':
    main()
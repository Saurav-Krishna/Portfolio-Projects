import streamlit as st
import requests

GITHUB_REPO = 'https://github.com/Saurav-Krishna/Portfolio-Projects/blob/main/main.html'
def fetch_html(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def main():
    st.title("Restaurant success Analysis")

    try:
        html_content = fetch_html(GITHUB_REPO)
        st.markdown(html_content, unsafe_allow_html=True)
    except requests.exceptions.RequestException as e:
        st.error(f'Error fetching HTML file: {e}')


if __name__ == '__main__':
    main()
import streamlit as st

st.title('06.Pages')
st.caption('text 참고사이트: https://docs.streamlit.io/get-started/tutorials/create-a-multipage-app')

# 페이지 선언
def main_page():
    st.title('Main page 🎈')
    st.sidebar.title('Side main 🎈')
def page2():
    st.title('Page 2 ❄️')
    st.sidebar.title('Side 2 ❄️')
def page3():
    st.title('Page 3 🎉')
    st.sidebar.title('Side 3 🎉')

# dictionary
page_name_to_funcs = {'Main page':main_page, 'Page2':page2, 'Page3':page3}

# sidebar w/ selection of pages
selected_page = st.sidebar.selectbox("select a page", page_name_to_funcs.keys())

# sidebar에서 선택한 페이지 불러오기
page_name_to_funcs[selected_page]()

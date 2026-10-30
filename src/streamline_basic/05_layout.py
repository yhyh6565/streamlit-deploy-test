import streamlit as st

st.title('Layouts')
st.caption('text 참고사이트: https://docs.streamlit.io/library/api-reference/layout')

# 1.sidebar
# st.title('1. sidebar')
with st.sidebar:
    st.header('1.Sidebar')

add_selectbox = st.sidebar.selectbox('how should i contact you?',['email','phone','text'])

if add_selectbox == 'email':
    st.sidebar.title('📧')
elif add_selectbox == 'mobile':
    st.sidebar.title('📱')
else:
    st.sidebar.title('☎')

# 2. columns
st.header('2. Column')
col1, col2, col3 = st.columns(3)

with col1:
    st.text('A cat')
    st.image('https://static.streamlit.io/examples/cat.jpg')
with col2:
    st.text('A dog')
    st.image('https://static.streamlit.io/examples/dog.jpg')
with col3:
    st.text('A owl')
    st.image('https://static.streamlit.io/examples/owl.jpg')

# 3. Tabs
st.header('3. Tabs')
tab1, tab2, tab3 = st.tabs(['cat','dog','owl'])
with tab1:
    st.caption('Cat')
    st.image('https://static.streamlit.io/examples/cat.jpg')
with tab2:
    st.caption('Dog')
    st.image('https://static.streamlit.io/examples/dog.jpg')
with tab3:
    st.caption('Owl')
    st.image('https://static.streamlit.io/examples/owl.jpg')


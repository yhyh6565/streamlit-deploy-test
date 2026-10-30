import streamlit as st
import time

st.title('Media elements')
st.caption('media url : https://docs.streamlit.io/library/api-reference/media')

# random image whenever user presses button
st.header('Media elements')
if st.button('random image'):
    random_url = f'https://picsum.photos/250/250?random={time.time()}'
    st.image(random_url)

# play local audio file
st.header('2.Audio')
st.audio('data/MusicSample.mp3')        # 어짜피 이미 streamlit_basic이라는 폴더 안에 있으니 그 이전의 경로는 넣을 필요가 없음

# play local mp4 file
st.header('3.Video')
st.video('data/VideoSample.mp4')

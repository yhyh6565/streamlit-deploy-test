import streamlit as st
import pandas as pd
from datetime import datetime

st.title('Input widgets')
st.caption('Input url : https://docs.streamlit.io/library/api-reference/widgets')

# 1. Button
st.header('1. Button')

if st.button('knock'):
    st.write('somebody in here')
    
if st.button('say hello'):
    st.write('hello')
else :
    st.write('goodbye')

# 2. Radio button
st.header('2. Radio button')
genre = st.radio('favorite movie genre?', ['action','sf', 'thriller'])

if genre == 'sf':
    st.write('Dune')
elif genre == 'action':
    st.write('Mission Impossible')
else :
    st.write('If')

# 3. Checkbox
st.header('3. checkbox')
agree = st.checkbox('I agree')

if agree:
    st.write('hi'*10)

# 4. select box
st.header('4. Select box')
option = st.selectbox('how can I reach you?', ['email', 'phone', 'text'])
st.write('ok', option, ' I will reach you through that')

# 5. multiselect
st.header('5.Multi select')
options = st.multiselect('좋아하는 색은?',
['Green', 'Yellow', 'Red', 'Blue'],     # 선택지
['Yellow', 'Red'])                      # 선택지 중 디폴트

st.write('당신의 선호 색상은 : ')
for i in options:
    st.write(i)
    
# 6. Input: Text / Number
st.header('6.Input: Text/Number')

# 텍스트 입력
st.subheader('**_text_input_**')
title = st.text_input('가장 좋아하는 영화는?', 'Sound of Music')
st.write('당신의 최애 영화는:', title)

# 숫자 입력
st.subheader('**_number_input_**')
number = st.number_input('Insert a number(1-10)', min_value=1, max_value=10, value=5, step=1)
st.write('The current number is', number)


# 7. Date input
st.header('7.Date input')
ymd = st.date_input('When is your birthday', datetime(2000,9,6))
st.write('Your Birthday', ymd)

# 8. Slider
st.header('8.Slider')

# 숫자 슬라이더 (단일 값)
st.subheader('**_Slider-이전 구간_**')
age = st.slider('나이가 어떻게 되세요?', 0, 130, 25)
st.write('I am ', age, 'years old')

# 숫자 구간 슬라이더 (최소~최대)
st.subheader('**_최소-최대값 내에서 숫자 사이 구간_**')
values = st.slider('값 구간을 선택하세요', 0.0, 100.0, (25.0,75.0))
st.write('values:', values)

# 날짜 구간 슬라이더
st.subheader('**_년 월 일 사이 구간_**')

slider_date = st.slider(
    '날짜 구간을 선택하세요.',
    min_value = datetime(2024,1,1),
    max_value = datetime(2024,12,31),
    value = (datetime(2024,6,1), datetime(2024,7,31)),
    format = 'YY/MM/DD'
)
st.write('slider date:', slider_date)
st.write('slider_date[0]:', slider_date[0], 'slider_date[1]:', slider_date[1])

# 날짜 구간으로 데이터 조회하기
st.header('날짜 구간으로 데이터 조회하기')

# CSV 데이터 불러오기
df = pd.read_csv('data/data_subway_in_seoul.csv', encoding='cp949')
st.write('날짜 필드 형식:', df['날짜'].dtypes)
st.write(df)

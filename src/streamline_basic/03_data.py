import streamlit as st
import pandas as pd
import numpy as np

st.title('Data Display Elements')
st.caption('data url : https://docs.streamlit.io/library/api-reference/data')

# 1. Metric
st.header('1.Metric')
st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

# 2. Multiple metrics
st.header('2.Multiple metrics')
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

# 3. delta color options
st.header('3. delta color')
st.metric(label="Gas price", value=4, delta=-0.5, delta_color="inverse")

st.metric(
    label="Active developers", value=123, delta=123, delta_color="off"
)

# 4. grid metrics card
st.header('4. grid metrics')
a, b = st.columns(2)
c, d = st.columns(2)

a.metric("Temperature", "30°F", "-9°F", border=True)
b.metric("Wind", "4 mph", "2 mph", border=True)

c.metric("Humidity", "77%", "5%", border=True)
d.metric("Pressure", "30.34 inHg", "-2 inHg", border=True)

# 5. dataframe
st.header('5. Show dataframe')
titanic = pd.read_csv('data/t2.csv')
st.dataframe(titanic.head(10))

# pandas styler example
# 난수 데이터프레임 생성
df = pd.DataFrame(np.random.randn(10, 20), columns=("col %d" % i for i in range(20)))
st.dataframe(df.style.highlight_max(axis=0))


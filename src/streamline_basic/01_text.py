import streamlit as st

# header, subheader, text, caption
st.title('Text elements')
st.caption('text url : https://docs.streamlit.io/library/api-reference/text')
st.header('Header practice')
st.subheader('Subheader practice')
st.text('text practice')

# markdown
st.markdown("# This is a Markdown title")
st.markdown("## This is a Markdown title")
st.markdown("This is **the Markdown 진하게**")
st.markdown("This is _the Markdown 기울임_")
st.markdown("This is *the Markdown 기울임*")
st.markdown("This is **_the Markdown 진하고 기울임_**")

st.markdown('- item')
st.markdown('1. item')

st.code('x=1234')

# latex
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

# write practice
st.write('this is a practice session for write \n')
st.write('\n')
st.write('\n')
st.write('Hello, _World!_ :sunglasses:')

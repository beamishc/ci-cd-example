import streamlit as st

from api.fast import root

st.write(root())

st.write('This is obviously very simple, in reality one would rather use this page to display API results more nicely! :)')

st.write('I am adding a change to show cd')

st.image('Screenshot_20221117-112100.png')

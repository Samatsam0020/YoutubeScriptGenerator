import streamlit as st
from src.generator import generate_script

st.title("Youtube Script generator")

if 'text_inputs' not in st.session_state:
    st.session_state.text_inputs = []


def add_text_input():
    st.session_state.text_inputs.append("")


if st.button("Add a link"):
    add_text_input()
first_input = st.text_input("link1", key="first_input")


for i, text in enumerate(st.session_state.text_inputs):
    st.session_state.text_inputs[i] = st.text_input(
        f"link {i+2}", value=text, key=f"text_input_{i}")


liste_link = [first_input] + st.session_state.text_inputs


if st.button('Generate'):
    st.write(generate_script(liste_link))

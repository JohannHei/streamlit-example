from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import requests

"""
# Welcome to Zapp Search Compare!
"""

def do_search(endpoint, query):

    req = requests.post(endpoint, json={'query': graph_query})

    print(req)

def on_input_change(input):
    return f"{input} RESULT"

search_input = st.text_input("Search Query")
search_result = on_input_change(search_input)

col1, col2 = st.columns(2)


st.write("You entered: ", search_result)

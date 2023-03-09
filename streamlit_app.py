from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import requests

"""
# Welcome to Zapp Search Compare!
"""

def do_search_old_backend(query):
    endpoint = "https://stg.gateway.quickcommerce.org/search/searchProducts/"
    graph_query = """
    query Search($search:String!) {
  search(filter:{search:$search,warehouseId:"V2FyZWhvdXNlOjNlY2EwNDRlLWUwMDQtNDEwNC04MmI3LTdiYWEyYWI5YzY5MA=="
    
  }){
    products{
      edges{
        node{
          id
        }
      }
    }
  }
}
    """

    req = requests.post(endpoint, json={'query': graph_query,"operationName":"Search","variables":{"search":query}})

    print(req)

    return req.data


search_input = st.text_input("Search Query")

col1, col2 = st.columns(2)


with col1:
    search_result = do_search_old_backend(search_input)
    st.write("You entered: ", search_result)

with col2:
    search_result = do_search_old_backend(search_input)
    st.write("You entered: ", search_result)

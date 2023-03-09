from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import requests
import json

"""
# Welcome to Zapp Search Compare!
"""

def do_search_old_backend(query, search_header=[]):
    endpoint = "https://gb.gateway.quickcommerce.org/search/searchProducts/"
    graph_query = """
    query Search($search:String!) {
  search(filter:{search:$search,warehouseId:"V2FyZWhvdXNlOjNlY2EwNDRlLWUwMDQtNDEwNC04MmI3LTdiYWEyYWI5YzY5MA=="
    
  }){
    products{
      edges{
        node{
          id
          name
          thumbnail{
            url
          }
        }
      }
    }
  }
}
    """

    res = requests.post(endpoint, json={'query': graph_query,"operationName":"Search","variables":{"search":query}}, headers={"x-active-search-features":",".join(search_header)})

    return json.loads(res.text)["data"]["search"]["products"]


search_input = st.text_input("Search Query")

col1, col2 = st.columns(2)

def write_result(products):
    for p in products:
        st.text(p["name"])
        st.image(p["thumbnail"]["url"])
        """
        ------------
        """

with col1:
    """
    Status quo
    """
    search_result = do_search_old_backend(search_input)
    write_result(search_result)

with col2:
    """
    is_search_boost_title
    """
    search_result = do_search_old_backend(search_input, ["is_search_boost_title"])
    write_result(search_result)

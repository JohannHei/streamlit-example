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

def do_search_old_backend(query, search_header=[], boosts={}):
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

    res = requests.post(endpoint, json={'query': graph_query,"operationName":"Search","variables":{"search":query}}, 
    headers={
        "x-active-search-features":",".join(search_header),
        "x-boosts":json.dumps(boosts)
        })

    return json.loads(res.text)["data"]["search"]["products"]["edges"]


search_input = st.text_input("Search Query")
boost_title = st.slider('Boost Title?', 0, 1000, 1)
boost_tags = st.slider('Boost Tags?', 0, 1000, 100)
boost_badges = st.slider('Boost Badges?', 0, 1000, 100)

boost_title_ayg = st.slider('Boost Title AYG?', 0, 1000, 5)
boost_tags_ayg = st.slider('Boost Tags AYG?', 0, 1000, 0)
boost_badges_ayg = st.slider('Boost Badges AYG?', 0, 1000, 0)

boosts = {
    "boost_title":boost_title,
    "boost_tags":boost_tags,
    "boost_badges":boost_badges,
    "boost_title_ayg":boost_title_ayg,
    "boost_tags_ayg":boost_tags_ayg,
    "boost_badges_ayg":boost_badges_ayg
}

experiments = ["is_search_title_boost"]

columns = st.columns(len(experiments)+2)

def write_result(products):
    for p in products:
        p = p["node"]
        st.text(p["name"])
        st.image(p["thumbnail"]["url"])
        """
        ------------
        """

with columns[0]:
    """
    Status quo
    """
    search_result = do_search_old_backend(search_input, boosts=boosts)
    write_result(search_result)

with columns[1]:
    """
    Status quo
    """
    search_result = do_search_old_backend(search_input)
    write_result(search_result)

for idx,experiment in enumerate(experiments):
    with columns[idx+2]:
        f"""
        {experiment}
        """
        search_result = do_search_old_backend(search_input, [experiment])
        write_result(search_result)

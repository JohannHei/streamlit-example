
import requests
import json

def do_search_gcp_backend(query, search_header=[], boosts={}):
    endpoint = "https://stg.gateway.quickcommerce.org/zmobile-gateway/graphql"
    graph_query = """
    query Search($search:String!) {
      gcpRetailSearch(warehouseId: "uk_london_old-brompton-road", query: $search) {
        items {
          name
          sku
          imageUrls
        }
      }
    }
    """

    res = requests.post(endpoint, json={'query': graph_query,"operationName":"Search","variables":{"search":query}}, 
    headers={
        "x-active-search-features":",".join(search_header),
        "x-boosts":json.dumps(boosts)
        })

    return json.loads(res.text)["data"]["gcpRetailSearch"]["items"]

def safe_list_get (l, idx, default):
  try:
    return l[idx]
  except IndexError:
    return default

search_input = ""
search_result = do_search_gcp_backend(search_input)
print("search_result", search_result)
default_image = "https://stg.static.quickcommerce.org/products/52379ef4-fdcf-4b2c-810d-dae8a7c16c15.png"
standard_result = [{ "id": p["sku"], "name": p["name"], "thumbnail": { "url": safe_list_get(p["imageUrls"], 0, default_image) } } for p in search_result if p is not None]


print("search_result", standard_result)

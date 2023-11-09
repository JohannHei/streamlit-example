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
        })

    results = json.loads(res.text)["data"]["gcpRetailSearch"]["items"]

    print("inital_result", results)
    
    return [product for product in results if product is not None] if results else []


print(do_search_gcp_backend("watter"))
import logging

import azure.functions as func
import json
import requests

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
  
    req_body = req.get_json()
    id = req_body["id"]
    userid = req_body["userId"]
    productid = req_body["productId"]
    
    res = requests.get(f"serverlessohproduct.trafficmanager.net/api/GetProduct?productid={productid}")
    #conn = http.client.HTTPSConnection("serverlessohproduct.trafficmanager.net")
    #resp = conn.request("GET", f"/api/GetProduct?productid={productid}")
    
    return func.HttpResponse(f"Hello, from {productid} got id: {res}")
    

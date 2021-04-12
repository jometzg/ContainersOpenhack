import logging

import azure.functions as func
import json
import requests
import uuid
import time

def main(req: func.HttpRequest, outputDocument: func.Out[str]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
  
    req_body = req.get_json()
    id = req_body["id"]
    userid = req_body["userId"]
    productid = req_body["productId"]
    rating = req_body["rating"]

    # check that the productid is valid
    headers = {'Content-type': 'application/json'}
    res_prod = requests.get(f"https://serverlessohproduct.trafficmanager.net/api/GetProduct?productid={productid}", headers=headers)
    if res_prod.status_code != 200:
        return func.HttpResponse(f"Invalid productid", status_code=400)
    
    # check that the userid is valid
    headers = {'Content-type': 'application/json'}
    res_user = requests.get(f"https://serverlessohuser.trafficmanager.net/api/GetUser?userId={userid}", headers=headers)
    if res_user.status_code != 200:
        return func.HttpResponse(f"Invalid userid", status_code=400)

    # check rating in range
    if rating < 0 or rating > 5: 
        return func.HttpResponse(f"Invalid rating", status_code=400)

    # build output object
    data = {
        "id": str(uuid.uuid4()),
        "userId" : userid,
        "ProductId" : productid,
        "timestamp": time.time(),
        "locationName": req_body["locationName"],  
        "Rating" : rating,
        "UserNotes" : req_body["userNotes"],
    }

    # save to Cosmos
    outputDocument.set(json.dumps(data))

    # return
    return func.HttpResponse(json.dumps(data))
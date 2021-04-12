import logging

import azure.functions as func
import json

def main(req: func.HttpRequest, rating:func.DocumentList) -> func.HttpResponse:
    
    logging.info('Python HTTP trigger function processed a request.')
 
    ratings_json = []

    for rate in rating:
        data = {
            "id": rate["id"],
            "userId" : rate["userId"],
            "ProductId" : rate["ProductId"],
            "timestamp": rate["timestamp"],
            "locationName": rate["locationName"],  
            "Rating" : rate["Rating"],
            "UserNotes" : rate["UserNotes"],
        }
        ratings_json.append(data)

    return func.HttpResponse(
            json.dumps(ratings_json),
            status_code=200,
            mimetype="application/json"            
    )
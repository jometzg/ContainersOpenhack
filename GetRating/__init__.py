import logging

import azure.functions as func
import json

def main(req: func.HttpRequest, rating: func.DocumentList) -> str:
    logging.info('Python HTTP trigger function processed a request.')
    logging.info(req.params["ratingId"])
    if not rating:
        logging.warning("rating item not found")
        return func.HttpResponse(f"Not foound", status_code=404)
    else:
        logging.info("Found rating item, Notes=%s",
                     rating[0]['UserNotes'])
        data = {
            "id": rating[0]["id"],
            "userId" : rating[0]["userId"],
            "ProductId" : rating[0]["ProductId"],
            "timestamp": rating[0]["timestamp"],
            "locationName": rating[0]["locationName"],  
            "Rating" : rating[0]["Rating"],
            "UserNotes" : rating[0]["UserNotes"],
        }
        return json.dumps(data)

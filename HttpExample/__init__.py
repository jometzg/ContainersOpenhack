import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    productid = req.params.get('ProductId')
    if not productid:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            productid = req_body.get('ProductId')

    if productid:
        return func.HttpResponse(f"The product name for your product id {productid} is Starfruit Explosion.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )

import logging
logger = logging.getLogger()
import os
import requests
# easikit imports
from easiutils import exceptions as er

# project specific imports
from handler.utils import utils
from easireqs import tokens

def retrieve(uri=None, req=None):
    token = tokens.azure_token(scope=os.environ['TARGET_CLIENT_ID'] + "/.default")
    headers = {"Authorization": "Bearer " + token["access_token"]}
    r = requests.post(os.environ["BACKEND_URI"] +"/song?limit-5&offset=0", headers=headers)
    if r.status_code != 200:
        msg=f"Something went wrong while connectiing to {os.environ['BACKEND_URI'] +'/song?limit-200&offset=0'}"
        raise er.BackendError(type=er.BACKEND_SERVICE_ERROR, message=msg)
    return r.json()


def process_response(data):
    rslt = []
    for record in data['DATA']['songs']:
        rslt.append(create_entity(record))
    return rslt


def create_entity(record):

    entity = {
          "identifier": record['sng_id'],
          "name": record['sng_name'],
          "artist": {
            "identifier": record['art_id'],
            "name":record['sng_name']
          }
        }
        
    return entity


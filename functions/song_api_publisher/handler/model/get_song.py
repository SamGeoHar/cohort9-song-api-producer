import logging
logger = logging.getLogger()

# easikit imports
from easiutils import exceptions as er

# project specific imports
from handler.utils import utils


# the model package should be a set of files, each of which is responsible
# for managing a different entity
# for small interfaces one file might manage multiple entities but generally
# the files would be split up
# if there is common code amongst entities, a model_utils type file would
# be created and imported by each individual entity

def retrieve(uri=None, req=None):
    '''gets values from the the API call via the service
    and converts them into the format needed by the backend,
    passes the converted values to the backend and converts the
    response into the something the service can use to pass back
    to the user
    '''
    mssg = utils.getmessage()
    rslt = process_response(mssg, uri, req)

    return rslt


def process_response(mssg, uri, req):
    '''units of functionality - such as processing backend responses -
    are often split out into their own functions to allow easier testing
    '''
    entity = create_entity([ mssg, uri, req ])
    return entity


def create_entity(record):
    '''so the final service calls are composed of known units of 
    reliable underlying functionality which also make up elements of the future
    regression testing
    '''
    entity = {
        "message": record[0],
        "incoming_uri": record[1],
        "easikit_request": record[2]
    }

    return entity



def create(uri=None, req=None):
    '''another CRUD operation for this entity - would generally take data, convert it
    and pass it to the back end, raising an error if anything failed along the way
    '''
    try:
        rslt = dict(payload)

    except Exception as ex:
        # exceptions outside the service layer should be raised, not handled
        # this allows the service layer to decide how to handle them
        # (though that will invariably be by passing them straight back
        # to the user)
        # all raised errors should be of er.UclError type or subtype
        raise er.UclError(ex)

    return rslt
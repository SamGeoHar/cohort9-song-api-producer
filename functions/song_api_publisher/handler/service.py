import logging
logger = logging.getLogger()

# easikit imports
from easiutils import service as sv, exceptions as er

# project specific imports
from handler.model import get_song


def retrieve_songs(req=None):

    with sv.handle_request() as h:

        data = get_song.retrieve()
        transformed_data = get_song.process_response(data)
        h.resp = { "body": {"song": transformed_data}, "status": 200, "entity": "song_collection"}

    return h.resp


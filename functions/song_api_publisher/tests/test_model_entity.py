import unittest, logging, os
import json, jsonschema

from testutils import test_setup
logger = logging.getLogger()
logger.setLevel(logging.getLevelName(os.environ.get("LOG_LEVEL", "DEBUG")))

# test specific imports
from handler.model import get_song

logging.disable(logging.CRITICAL)

class EntityTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_retrieve_song(self):
        if "SKIP_INTEGRATION_TESTS" in os.environ: print("skipped ..."); return

        r = get_song.retrieve()
        self.assertIn("DATA", r, "The response contains the DATA object")
        self.assertIn("songs", r['DATA'], "The response contains the 'song' field name in the DATA object")
        self.assertIsInstance(r['DATA']["songs"], list, "The song field in the response is of the type list")


    def test_create_entity(self):

        record={
        "sng_id": "1qn0PMzUT6Slh7Lb9yrIwC",
        "sng_name": "Gone Goes on and On",
        "art_id": "7tje8UB3cuR1ZfeJx2U38T",
        "art_name": "Logan Mize"
      }
        r=get_song.create_entity(record)
        self.assertIn("identifier", r, "Identifier in the response")
        self.assertEqual(r['identifier'], "1qn0PMzUT6Slh7Lb9yrIwC", "The value of the song id is 1qn0PMzUT6Slh7Lb9yrIwC")
        self.assertIn("name", r, "name in the response")
        self.assertIn("artist", r, "artist in the response")
        self.assertIn("identifier", r['artist'], "artist identifer in the artist object")
        self.assertIn("name", r['artist'], "artist name in the artist object")

    def test_process_response(self):

        data={
  "DATA": {
    "count": 106260,
    "songs": [
      {
        "sng_id": "6IqUm14MgoKbwt6jdGBikH",
        "sng_name": "Better Off Gone",
        "art_id": "7tje8UB3cuR1ZfeJx2U38T",
        "art_name": "Logan Mize"
      },
      {
        "sng_id": "1qn0PMzUT6Slh7Lb9yrIwC",
        "sng_name": "Gone Goes on and On",
        "art_id": "7tje8UB3cuR1ZfeJx2U38T",
        "art_name": "Logan Mize"
      },
      {
        "sng_id": "3mispPuVcaDKAFhx4unVOZ",
        "sng_name": "A Brief Introduction",
        "art_id": "7EVSr3oJoGDwOzIiE4WQx3",
        "art_name": "Logan Whitehurst & The Junior Science Club"
      },
      {
        "sng_id": "6TzwdWJGU9tXbrmmmLx2DH",
        "sng_name": "Please and Thank You",
        "art_id": "7EVSr3oJoGDwOzIiE4WQx3",
        "art_name": "Logan Whitehurst & The Junior Science Club"
      }
    ]
  }
}
        r=get_song.process_response(data)
        self.assertIsInstance(r, list, "The response is of the type list")

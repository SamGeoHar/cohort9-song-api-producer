import unittest, logging, os
from unittest.mock import patch
import json, jsonschema

from testutils import test_setup
logger = logging.getLogger()
logger.setLevel(logging.getLevelName(os.environ.get("LOG_LEVEL", "DEBUG")))

# easiutils imports
from easiutils import exceptions as er

# test specific imports
from handler import service

logging.disable(logging.CRITICAL)

class ServiceTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_get_song(self):
        # if "SKIP_INTEGRATION_TESTS" in os.environ: print("skipped ..."); return

        r = service.retrieve_songs()
        self.assertIn("body", r, "Response should have body field")
        self.assertIn("status", r, "Response should have status field")
        self.assertEqual(r["status"], 200, "Status should be 200")


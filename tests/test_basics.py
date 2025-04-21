import unittest
import tmsh


class Basics(unittest.TestCase):
    def test_initialize(self):
        tmsh.initialize()
        self.assertTrue(tmsh.isInitialized())
        tmsh.finalize()
        self.assertFalse(tmsh.isInitialized())

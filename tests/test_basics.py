from __future__ import annotations

import unittest

import tmsh


class Basics(unittest.TestCase):
    def test_initialize(self) -> None:
        tmsh.initialize()
        self.assertTrue(tmsh.isInitialized())
        tmsh.finalize()
        self.assertFalse(tmsh.isInitialized())

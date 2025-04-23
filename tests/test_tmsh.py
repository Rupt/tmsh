from __future__ import annotations

import unittest

import tests
import tmsh


class Tmsh(unittest.TestCase):
    def test_initialize(self) -> None:
        tmsh.initialize()
        self.assertTrue(tmsh.isInitialized())
        tmsh.finalize()
        self.assertFalse(tmsh.isInitialized())

    def test_bad_finalize(self) -> None:
        with self.assertRaises(RuntimeError):
            tmsh.finalize()

    @tests.initialized()
    def test_clear(self) -> None:
        tmsh.model.add("name")
        tmsh.option.setNumber("General.Verbosity", 3)
        tmsh.clear()
        self.assertEqual(tmsh.model.list(), [""])

from __future__ import annotations

import unittest

import tmsh


class Model(unittest.TestCase):
    def test_add(self) -> None:
        tmsh.initialize()
        name = "a"
        assert name not in tmsh.model.list()
        tmsh.model.add(name)
        self.assertIn(name, tmsh.model.list())
        tmsh.finalize()

    def test_remove(self) -> None:
        tmsh.initialize()
        name = "b"
        tmsh.model.add(name)
        assert tmsh.model.getCurrent() == name
        tmsh.model.remove()
        self.assertNotEqual(tmsh.model.getCurrent(), name)
        self.assertNotIn(name, tmsh.model.list())
        tmsh.finalize()

    def test_list(self) -> None:
        tmsh.initialize()
        self.assertEqual(tmsh.model.list(), [""])
        name = "1"
        tmsh.model.add(name)
        self.assertEqual(set(tmsh.model.list()), {"", name})
        tmsh.finalize()

    def test_current(self) -> None:
        tmsh.initialize()
        one = "I"
        two = "II"
        tmsh.model.add(one)
        tmsh.model.add(two)
        tmsh.model.setCurrent(one)
        self.assertEqual(tmsh.model.getCurrent(), one)
        tmsh.model.setCurrent(two)
        self.assertEqual(tmsh.model.getCurrent(), two)
        tmsh.finalize()

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

    def test_filename(self) -> None:
        tmsh.initialize()
        name = "abc"
        tmsh.model.setFileName(name)
        self.assertEqual(tmsh.model.getFileName(), name)
        tmsh.finalize()

    def test_entities(self) -> None:
        tmsh.initialize()
        self.assertEqual(tmsh.model.getEntities(), [])

        point_a = tmsh.model.geo.addPoint(0.0, 0.0, 0.0)
        point_b = tmsh.model.geo.addPoint(0.0, 0.0, 1.0)
        point_c = tmsh.model.geo.addPoint(0.0, 1.0, 1.0)
        line = tmsh.model.geo.addPolyline((point_a, point_b, point_c, point_a))
        loop = tmsh.model.geo.addCurveLoop((line,))
        print(line)
        surface = tmsh.model.geo.addPlaneSurface((loop,))
        print(surface)
        tmsh.model.geo.synchronize()
        volume = tmsh.model.geo.extrude(((surface, 2),), 1.0, 0.0, 0.0)
        tmsh.model.geo.synchronize()
        print(tmsh.model.getEntities())
        print(tmsh.model.getEntities(0))
        print(tmsh.model.getEntities(1))
        print(tmsh.model.getEntities(2))
        print(tmsh.model.getEntities(3))
        print(volume)
        tmsh.finalize()
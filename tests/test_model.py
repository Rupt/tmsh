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

        a = tmsh.model.geo.addPoint(0.0, 0.0, 0.0)
        b = tmsh.model.geo.addPoint(0.0, 0.0, 1.0)
        c = tmsh.model.geo.addPoint(0.0, 1.0, 1.0)
        d = tmsh.model.geo.addPoint(1.0, 0.0, 0.0)

        e0 = tmsh.model.getEntities(dim=0)
        self.assertEqual(len(e0), 4)
        self.assertTrue(all(dim == 0 for dim, _ in e0))
        self.assertEqual({tag for _, tag in e0}, {a, b, c, d})

        ab = tmsh.model.geo.addLine(a, b)
        ac = tmsh.model.geo.addLine(a, c)
        ad = tmsh.model.geo.addLine(a, d)
        bc = tmsh.model.geo.addLine(b, c)
        bd = tmsh.model.geo.addLine(b, d)
        cd = tmsh.model.geo.addLine(c, d)

        e1 = tmsh.model.getEntities(dim=1)
        self.assertEqual(len(e1), 6)
        self.assertTrue(all(dim == 1 for dim, _ in e1))
        self.assertEqual({tag for _, tag in e1}, {ab, ac, ad, bc, bd, cd})

        loop_abc = tmsh.model.geo.addCurveLoop((ab, ac, bc), reorient=True)
        loop_abd = tmsh.model.geo.addCurveLoop((ab, ad, bd), reorient=True)
        loop_acd = tmsh.model.geo.addCurveLoop((ac, ad, cd), reorient=True)
        loop_bcd = tmsh.model.geo.addCurveLoop((bc, bd, cd), reorient=True)
        abc = tmsh.model.geo.addPlaneSurface((loop_abc,))
        abd = tmsh.model.geo.addPlaneSurface((loop_abd,))
        acd = tmsh.model.geo.addPlaneSurface((loop_acd,))
        bcd = tmsh.model.geo.addPlaneSurface((loop_bcd,))

        e2 = tmsh.model.getEntities(dim=2)
        self.assertEqual(len(e2), 4)
        self.assertTrue(all(dim == 2 for dim, _ in e2))
        self.assertEqual({tag for _, tag in e2}, {abc, abd, acd, bcd})

        surface_loop_abcd = tmsh.model.geo.addSurfaceLoop((abc, abd, acd, bcd))
        abcd = tmsh.model.geo.addVolume((surface_loop_abcd,))
        tmsh.model.geo.synchronize()

        e3 = tmsh.model.getEntities(dim=3)
        self.assertEqual(len(e3), 1)
        self.assertTrue(all(dim == 3 for dim, _ in e3))
        self.assertEqual({tag for _, tag in e3}, {abcd})

        self.assertEqual(
            set(tmsh.model.getEntities(dim=-1)), {*e0, *e1, *e2, *e3}
        )

        tmsh.finalize()

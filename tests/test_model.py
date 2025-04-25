from __future__ import annotations

import typing
import unittest

import tests
import tmsh


class Model(unittest.TestCase):
    @tests.initialized
    def test_add(self) -> None:
        name = "a"
        assert name not in tmsh.model.list()
        tmsh.model.add(name)
        self.assertIn(name, tmsh.model.list())

    @tests.initialized
    def test_remove(self) -> None:
        name = "b"
        tmsh.model.add(name)
        assert tmsh.model.getCurrent() == name
        tmsh.model.remove()
        self.assertNotEqual(tmsh.model.getCurrent(), name)
        self.assertNotIn(name, tmsh.model.list())

    @tests.initialized
    def test_list(self) -> None:
        self.assertEqual(tmsh.model.list(), [""])
        name = "1"
        tmsh.model.add(name)
        self.assertEqual(set(tmsh.model.list()), {"", name})

    @tests.initialized
    def test_current(self) -> None:
        one = "I"
        two = "II"
        tmsh.model.add(one)
        tmsh.model.add(two)
        tmsh.model.setCurrent(one)
        self.assertEqual(tmsh.model.getCurrent(), one)
        tmsh.model.setCurrent(two)
        self.assertEqual(tmsh.model.getCurrent(), two)

    @tests.initialized
    def test_filename(self) -> None:
        name = "abc"
        tmsh.model.setFileName(name)
        self.assertEqual(tmsh.model.getFileName(), name)

    @tests.initialized
    def test_entities(self) -> None:
        self.assertEqual(tmsh.model.getEntities(), [])

        tet = _tetrahedron()

        e0 = tmsh.model.getEntities(dim=0)
        self.assertEqual(len(e0), 4)
        self.assertTrue(all(dim == 0 for dim, _ in e0))
        self.assertEqual({tag for _, tag in e0}, set(tet.points))

        e1 = tmsh.model.getEntities(dim=1)
        self.assertEqual(len(e1), 6)
        self.assertTrue(all(dim == 1 for dim, _ in e1))
        self.assertEqual({tag for _, tag in e1}, set(tet.lines))

        e2 = tmsh.model.getEntities(dim=2)
        self.assertEqual(len(e2), 4)
        self.assertTrue(all(dim == 2 for dim, _ in e2))
        self.assertEqual({tag for _, tag in e2}, set(tet.surfaces))

        e3 = tmsh.model.getEntities(dim=3)
        self.assertEqual(len(e3), 1)
        self.assertTrue(all(dim == 3 for dim, _ in e3))
        self.assertEqual({tag for _, tag in e3}, {tet.volume})

        self.assertEqual(
            set(tmsh.model.getEntities(dim=-1)), {*e0, *e1, *e2, *e3}
        )


class _Tetrahedron(typing.NamedTuple):
    points: tuple[int, int, int, int]
    lines: tuple[int, int, int, int, int, int]
    surfaces: tuple[int, int, int, int]
    volume: int


def _tetrahedron() -> _Tetrahedron:
    a = tmsh.model.geo.addPoint(0.0, 0.0, 0.0)
    b = tmsh.model.geo.addPoint(0.0, 0.0, 1.0)
    c = tmsh.model.geo.addPoint(0.0, 1.0, 1.0)
    d = tmsh.model.geo.addPoint(1.0, 0.0, 0.0)
    ab = tmsh.model.geo.addLine(a, b)
    ac = tmsh.model.geo.addLine(a, c)
    ad = tmsh.model.geo.addLine(a, d)
    bc = tmsh.model.geo.addLine(b, c)
    bd = tmsh.model.geo.addLine(b, d)
    cd = tmsh.model.geo.addLine(c, d)
    loop_abc = tmsh.model.geo.addCurveLoop((ab, ac, bc), reorient=True)
    loop_abd = tmsh.model.geo.addCurveLoop((ab, ad, bd), reorient=True)
    loop_acd = tmsh.model.geo.addCurveLoop((ac, ad, cd), reorient=True)
    loop_bcd = tmsh.model.geo.addCurveLoop((bc, bd, cd), reorient=True)
    abc = tmsh.model.geo.addPlaneSurface((loop_abc,))
    abd = tmsh.model.geo.addPlaneSurface((loop_abd,))
    acd = tmsh.model.geo.addPlaneSurface((loop_acd,))
    bcd = tmsh.model.geo.addPlaneSurface((loop_bcd,))
    surface_loop_abcd = tmsh.model.geo.addSurfaceLoop((abc, abd, acd, bcd))
    abcd = tmsh.model.geo.addVolume((surface_loop_abcd,))
    tmsh.model.geo.synchronize()
    return _Tetrahedron(
        points=(a, b, c, d),
        lines=(ab, ac, ad, bc, bd, cd),
        surfaces=(abc, abd, acd, bcd),
        volume=abcd,
    )

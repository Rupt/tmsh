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

    @tests.initialized
    def test_entity_name(self) -> None:
        tet = _tetrahedron()
        base = tmsh.model.getEntityName(dim=3, tag=tet.volume)
        self.assertEqual(base, "")
        name = "abc"
        assert name != base
        tmsh.model.setEntityName(dim=3, tag=tet.volume, name=name)
        self.assertEqual(tmsh.model.getEntityName(dim=3, tag=tet.volume), name)
        tmsh.model.removeEntityName(name=name)
        self.assertEqual(tmsh.model.getEntityName(dim=3, tag=tet.volume), base)

    @tests.initialized
    def test_physical_group(self) -> None:
        tet = _tetrahedron()
        base_tags = tet.points[:3]
        base_tag = 123
        base_name = "base"
        base = tmsh.model.addPhysicalGroup(
            dim=0, tags=base_tags, tag=base_tag, name=base_name
        )
        self.assertEqual(base, base_tag)
        mesh_tags = tet.lines
        mesh_tag = 234
        mesh_name = "mesh"
        mesh = tmsh.model.addPhysicalGroup(
            dim=1, tags=mesh_tags, tag=mesh_tag, name=mesh_name
        )
        self.assertEqual(mesh, mesh_tag)
        self.assertEqual(
            set(tmsh.model.getPhysicalGroups()), {(0, base), (1, mesh)}
        )
        self.assertEqual(tmsh.model.getPhysicalGroups(dim=0), [(0, base)])
        self.assertEqual(tmsh.model.getPhysicalGroups(dim=1), [(1, mesh)])
        self.assertEqual(tmsh.model.getPhysicalGroups(dim=2), [])
        self.assertEqual(tmsh.model.getPhysicalGroups(dim=3), [])
        self.assertEqual(
            set(tmsh.model.getEntitiesForPhysicalGroup(dim=0, tag=base)),
            set(base_tags),
        )
        self.assertEqual(
            set(tmsh.model.getEntitiesForPhysicalGroup(dim=1, tag=mesh)),
            set(mesh_tags),
        )
        self.assertEqual(
            set(tmsh.model.getEntitiesForPhysicalName(base_name)),
            {(0, tag) for tag in base_tags},
        )
        self.assertEqual(
            set(tmsh.model.getEntitiesForPhysicalName(mesh_name)),
            {(1, tag) for tag in mesh_tags},
        )
        self.assertEqual(
            tmsh.model.getPhysicalGroupsForEntity(dim=0, tag=base_tags[0]),
            [base],
        )
        self.assertEqual(
            tmsh.model.getPhysicalGroupsForEntity(dim=1, tag=mesh_tags[0]),
            [mesh],
        )
        self.assertEqual(
            tmsh.model.getPhysicalGroupsForEntity(dim=3, tag=tet.volume), []
        )

    @tests.initialized
    def test_remove_physical_groups(self) -> None:
        self.assertEqual(tmsh.model.getPhysicalGroups(), [])
        tmsh.model.removePhysicalGroups()
        self.assertEqual(tmsh.model.getPhysicalGroups(), [])
        points = tuple(tmsh.model.geo.addPoint(i, 0.0, 0.0) for i in range(5))
        tmsh.model.geo.synchronize()
        groups = tuple(
            tmsh.model.addPhysicalGroup(0, points[i : i + 2]) for i in range(3)
        )
        self.assertEqual(
            tmsh.model.getPhysicalGroups(), [(0, tag) for tag in groups]
        )
        tmsh.model.removePhysicalGroups()
        self.assertEqual(tmsh.model.getPhysicalGroups(), [])


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

from __future__ import annotations

import sys
import unittest

import tests
import tmsh


class Tmsh(unittest.TestCase):
    def test_initialize(self) -> None:
        tmsh.initialize()
        self.assertTrue(tmsh.isInitialized())
        tmsh.finalize()
        self.assertFalse(tmsh.isInitialized())

    @tests.initialized
    def test_clear(self) -> None:
        tmsh.model.add("name")
        tmsh.option.setNumber("General.Verbosity", 3)
        tmsh.clear()
        self.assertEqual(tmsh.model.list(), [""])


def line() -> str:
    frame = sys._getframe(1)  # noqa: SLF001
    return f"{frame.f_code.co_filename}:{frame.f_lineno}:"


def observed(line: str, message: str) -> None:
    print(line, "observed: ", message, sep="")


def expected(line: str, message: str) -> None:
    print(line, "expected: ", message, sep="")


def test_test() -> None:
    a = 97
    b = chr(a)
    print(b)

    if b != "A" and (c := line()):
        observed(c, f"{b = }")
        expected(c, 'b == "A"')

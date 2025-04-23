from __future__ import annotations

import unittest

import tests
import tmsh


class Option(unittest.TestCase):
    @tests.initialized()
    def test_number(self) -> None:
        name = "General.TranslationX"
        value = 1.5
        tmsh.option.setNumber(name, value)
        self.assertEqual(tmsh.option.getNumber(name), value)

    @tests.initialized()
    def test_string(self) -> None:
        name = "General.AxesLabelX"
        value = "x"
        tmsh.option.setString(name, value)
        self.assertEqual(tmsh.option.getString(name), value)

    @tests.initialized()
    def test_color(self) -> None:
        name = "General.Color.Background"
        value = (255, 51, 204, 123)
        tmsh.option.setColor(name, *value)
        self.assertEqual(tmsh.option.getColor(name), value)

    @tests.initialized()
    def test_restore_defaults(self) -> None:
        name = "General.AxesLabelX"
        default = tmsh.option.getString(name)
        tmsh.option.setString(name, f"not {default}")
        assert tmsh.option.getString(name) != default
        tmsh.option.restoreDefaults()
        self.assertEqual(tmsh.option.getString(name), default)

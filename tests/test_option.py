from __future__ import annotations

import unittest

import tmsh


class Option(unittest.TestCase):
    def test_number(self) -> None:
        tmsh.initialize()
        name = "General.TranslationX"
        value = 1.5
        tmsh.option.setNumber(name, value)
        self.assertEqual(tmsh.option.getNumber(name), value)
        tmsh.finalize()

    def test_string(self) -> None:
        tmsh.initialize()
        name = "General.AxesLabelX"
        value = "x"
        tmsh.option.setString(name, value)
        self.assertEqual(tmsh.option.getString(name), value)
        tmsh.finalize()

    def test_color(self) -> None:
        tmsh.initialize()
        name = "General.Color.Background"
        value = (255, 51, 204, 123)
        tmsh.option.setColor(name, *value)
        self.assertEqual(tmsh.option.getColor(name), value)
        tmsh.finalize()

    def test_restore_defaults(self) -> None:
        tmsh.initialize()
        name = "General.AxesLabelX"
        default = tmsh.option.getString(name)
        tmsh.option.setString(name, f"not {default}")
        assert tmsh.option.getString(name) != default
        tmsh.option.restoreDefaults()
        self.assertEqual(tmsh.option.getString(name), default)

from __future__ import annotations

import unittest

import tests
import tmsh


class ErrorCode(unittest.TestCase):
    def test_no_error(self) -> None:
        with tmsh._ErrorCode() as error_code:  # noqa: SLF001
            self.assertEqual(error_code.value, 0)

    @tests.initialized
    def test_error(self) -> None:
        msg = "abc"
        tmsh.option.setNumber("General.Verbosity", 3)
        tmsh.logger.write(msg)
        with self.assertRaises(RuntimeError), tmsh._ErrorCode() as error_code:  # noqa: SLF001
            error_code.value = 1

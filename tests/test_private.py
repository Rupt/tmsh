from __future__ import annotations

import ctypes
import unittest

import gmsh

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


class Output(unittest.TestCase):
    def test_ostring(self) -> None:
        text = b"asdf\0"
        ptr = ctypes.cast(
            gmsh.lib.gmshMalloc(len(text)), ctypes.POINTER(ctypes.c_char)
        )
        ctypes.memmove(ptr, text, len(text))
        assert ptr[: len(text)] == text
        self.assertEqual(
            tmsh._ostring(ctypes.cast(ptr, ctypes.c_char_p)),  # noqa: SLF001
            text[:-1].decode(),
        )

    def test_ostring_error(self) -> None:
        ptr = ctypes.c_char_p()
        with self.assertRaisesRegex(RuntimeError, "null pointer"):
            tmsh._ostring(ptr)  # noqa: SLF001

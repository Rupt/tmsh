from __future__ import annotations

import contextlib
from typing import TYPE_CHECKING

import tmsh

if TYPE_CHECKING:
    from collections.abc import Generator


@contextlib.contextmanager
def initialized() -> Generator[None]:
    tmsh.initialize(readConfigFiles=False, run=False, interruptible=False)
    try:
        yield
    finally:
        tmsh.finalize()

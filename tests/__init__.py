from __future__ import annotations

from typing import TYPE_CHECKING

import tmsh

if TYPE_CHECKING:
    from collections.abc import Callable


def initialized[**P, T](fn: Callable[P, T]) -> Callable[P, T]:
    def inner(*args: P.args, **kwargs: P.kwargs) -> T:
        tmsh.initialize(readConfigFiles=False, run=False, interruptible=False)
        try:
            return fn(*args, **kwargs)
        finally:
            tmsh.finalize()

    return inner

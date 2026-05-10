from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `devin_platform.resources` module.

    This is used so that we can lazily import `devin_platform.resources` only when
    needed *and* so that users can just import `devin_platform` and reference `devin_platform.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("devin_platform.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()

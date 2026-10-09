"""
k3dict

It provides with several dict operation functions.

#   Status

This library is considered production ready.

"""

# from .proc import CalledProcessError
# from .proc import ProcError

from .dictutil import (
    AttrDict,
    AttrDictCopy,
    NoSuchKey,
    add,
    addto,
    attrdict,
    attrdict_copy,
    breadth_iter,
    combine,
    combineto,
    contains,
    depth_iter,
    get,
    make_getter,
    make_getter_str,
    make_setter,
    subdict,
)
from .fixed_keys_dict import (
    FixedKeysDict,
)

__all__ = [
    "AttrDict",
    "AttrDictCopy",
    "FixedKeysDict",
    "NoSuchKey",
    "add",
    "addto",
    "attrdict",
    "attrdict_copy",
    "breadth_iter",
    "combine",
    "combineto",
    "contains",
    "depth_iter",
    "get",
    "make_getter",
    "make_getter_str",
    "make_setter",
    "subdict",
]


def __getattr__(name: str) -> str:
    # importlib.metadata takes about 20 ms to import, so it is loaded only
    # when __version__ is read
    if name != "__version__":
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

    from importlib.metadata import version

    return version("k3dict")

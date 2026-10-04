"""
k3dict

It provides with several dict operation functions.

#   Status

This library is considered production ready.

"""

# from .proc import CalledProcessError
# from .proc import ProcError

from importlib.metadata import version

__version__ = version("k3dict")

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

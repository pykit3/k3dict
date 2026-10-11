from typing import ClassVar


class FixedKeysDict(dict):
    """
    It provides the base class for dict with explicit keys.

    :param args: as builtin **dict**.
    :param argkv: as builtin **dict**.
    :return: An instance of dictutil.FixedKeysDict.
    """

    # {'key', value_constructor}
    keys_default: ClassVar[dict] = {}

    # ordered keys as ident
    ident_keys = ()

    def __init__(self, *args, **argkv):
        super().__init__(*args, **argkv)

        # Convert present keys
        for k in self:
            self[k] = self.keys_default[k](self[k])

        # Add default value to absent keys
        for k in self.keys_default:
            if k not in self:
                self[k] = self.keys_default[k]()

    def __setitem__(self, key, value):
        try:
            value = self.keys_default[key](value)
        except KeyError:
            raise KeyError(f"key: {key} is invalid")
        except (ValueError, TypeError) as e:
            raise ValueError(f"value: {value!r} is invalid. {e!r}")

        super().__setitem__(key, value)

    # dict's own update(), setdefault() and |= do not call __setitem__().
    def update(self, *args, **argkv):
        for k, v in dict(*args, **argkv).items():
            self[k] = v

    def setdefault(self, key, default=None):
        if key not in self:
            self[key] = default

        return self[key]

    def __ior__(self, other):
        self.update(other)
        return self

    def ident(self):
        return tuple([self[k] for k in self.ident_keys])

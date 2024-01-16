from typing import Self

from comtypes import GUID

from portable_device_api._api.portable_device_api import tagpropertykey


class PropertyKey:
    """Mostly just here for the __eq__"""

    def __init__(self, v: tagpropertykey):
        self._v = v

    @classmethod
    def create(cls, fmtid: GUID, pid: int) -> Self:
        v = tagpropertykey(fmtid=fmtid, pid=pid)
        return cls(v)

    @classmethod
    def null(cls) -> Self:
        return cls.create(GUID(), 0)

    @property
    def v(self) -> tagpropertykey:
        return self._v

    def __eq__(self, other):
        if isinstance(other, PropertyKey):
            return self.v.fmtid == other.v.fmtid and self.v.pid == other.v.pid
        else:
            return NotImplemented

    def __repr__(self):
        return f"{type(self)}(fmtid = {self.v.fmtid}, pid = {self.v.pid})"

    def __str__(self):
        return f"{self.v.fmtid}:{self.v.pid}"
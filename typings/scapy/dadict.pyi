"""
This type stub file was generated by pyright.
"""

import scapy.modules.six as six
from scapy.error import Scapy_Exception
from scapy.compat import Any, Dict, Generic, Iterator, List, Union, _Generic_metaclass

"""
Direct Access dictionary.
"""
def fixname(x: Union[bytes, str]) -> str:
    """
    Modifies a string to make sure it can be used as an attribute name.
    """
    ...

class DADict_Exception(Scapy_Exception):
    ...


_K = ...
_V = ...
@six.add_metaclass(_Generic_metaclass)
class DADict(Generic[_K, _V]):
    """
    Direct Access Dictionary

    This acts like a dict, but it provides a direct attribute access
    to its keys through its values. This is used to store protocols,
    manuf...

    For instance, scapy fields will use a DADict as an enum::

        ETHER_TYPES[2048] -> IPv4

    Whereas humans can access::

        ETHER_TYPES.IPv4 -> 2048
    """
    def __init__(self, _name: str = ..., **kargs: Any) -> None:
        ...
    
    def ident(self, v: _V) -> str:
        """
        Return value that is used as key for the direct access
        """
        ...
    
    def update(self, *args: Dict[str, _V], **kwargs: Dict[str, _V]) -> None:
        ...
    
    def iterkeys(self) -> Iterator[_K]:
        ...
    
    def keys(self) -> List[_K]:
        ...
    
    def __iter__(self) -> Iterator[_K]:
        ...
    
    def itervalues(self) -> Iterator[_V]:
        ...
    
    def values(self) -> List[_V]:
        ...
    
    def __repr__(self) -> str:
        ...
    
    def __getitem__(self, attr: _K) -> _V:
        ...
    
    def __setitem__(self, attr: _K, val: _V) -> None:
        ...
    
    def __len__(self) -> int:
        ...
    
    def __nonzero__(self) -> bool:
        ...
    
    __bool__ = ...
    def __getattr__(self, attr: str) -> _K:
        ...
    
    def __dir__(self) -> List[str]:
        ...
    


"""
This type stub file was generated by pyright.
"""

import sys
import scapy.modules.six as six
from typing import Any, AnyStr, Callable, DefaultDict, Dict, Generic, IO, Iterable, Iterator, List, NewType, NoReturn, Optional, Pattern, Sequence, Set, Tuple, Type, TypeVar, Union, overload
from scapy.packet import Packet

"""
Python 2 and 3 link classes.
"""
__all__ = ['Any', 'AnyStr', 'Callable', 'DefaultDict', 'Dict', 'Generic', 'IO', 'Iterable', 'Iterator', 'List', 'Literal', 'NamedTuple', 'NewType', 'NoReturn', 'Optional', 'Pattern', 'Sequence', 'Set', 'Sized', 'Tuple', 'Type', 'TypeVar', 'Union', 'cast', 'overload', 'FAKE_TYPING', 'TYPE_CHECKING', 'AddressFamily', 'base64_bytes', 'bytes_base64', 'bytes_encode', 'bytes_hex', 'chb', 'gzip_compress', 'gzip_decompress', 'hex_bytes', 'lambda_tuple_converter', 'orb', 'plain_str', 'raw']
if notFAKE_TYPING:
    ...
else:
    def cast(_type, obj):
        ...
    
    Any = ...
    AnyStr = ...
    Callable = ...
    DefaultDict = ...
    Dict = ...
    Generic = ...
    Iterable = ...
    Iterator = ...
    IO = ...
    List = ...
    NewType = ...
    NoReturn = ...
    Optional = ...
    Pattern = ...
    Sequence = ...
    Set = ...
    Sequence = ...
    Tuple = ...
    Type = ...
    TypeVar = ...
    Union = ...
    class Sized:
        ...
    
    
    overload = ...
if sys.version_info >= (3, 7):
    ...
else:
    ...
if sys.version_info >= (3, 8):
    ...
else:
    ...
if sys.version_info >= (3, 4):
    ...
else:
    ...
class _Generic_metaclass(type):
    if FAKE_TYPING:
        def __getitem__(self, typ: Any) -> Any:
            ...
        


DecoratorCallable = ...
def lambda_tuple_converter(func: DecoratorCallable) -> DecoratorCallable:
    """
    Converts a Python 2 function as
      lambda (x,y): x + y
    In the Python 3 format:
      lambda x,y : x + y
    """
    ...

if TYPE_CHECKING:
    ...
if six.PY2:
    bytes_encode: Callable[[Any], bytes] = ...
    orb: Callable[[bytes], int] = ...
    def chb(x: int) -> bytes:
        ...
    
    def raw(x: Union[Packet]) -> bytes:
        """
        Builds a packet and returns its bytes representation.
        This function is and will always be cross-version compatible
        """
        ...
    
else:
    def raw(x: Union[Packet]) -> bytes:
        """
        Builds a packet and returns its bytes representation.
        This function is and will always be cross-version compatible
        """
        ...
    
    def bytes_encode(x: Any) -> bytes:
        """Ensure that the given object is bytes.
        If the parameter is a packet, raw() should be preferred.
        """
        ...
    
    def chb(x: int) -> bytes:
        """Same than chr() but encode as bytes."""
        ...
    
    def orb(x: Union[int, str, bytes]) -> int:
        """Return ord(x) when not already an int."""
        ...
    
def bytes_hex(x: AnyStr) -> bytes:
    """Hexify a str or a bytes object"""
    ...

def hex_bytes(x: AnyStr) -> bytes:
    """De-hexify a str or a byte object"""
    ...

def base64_bytes(x: AnyStr) -> bytes:
    """Turn base64 into bytes"""
    ...

def bytes_base64(x: AnyStr) -> bytes:
    """Turn bytes into base64"""
    ...

if six.PY2:
    html_escape = ...
else:
    html_escape = ...
if six.PY2:
    def gzip_decompress(x: AnyStr) -> bytes:
        """Decompress using gzip"""
        ...
    
    def gzip_compress(x: AnyStr) -> bytes:
        """Compress using gzip"""
        ...
    
else:
    gzip_decompress = ...
    gzip_compress = ...

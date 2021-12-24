"""
This type stub file was generated by pyright.
"""

"""
Fields that hold random numbers.
"""
class RandomEnumeration:
    """iterate through a sequence in random order.
       When all the values have been drawn, if forever=1, the drawing is done again.  # noqa: E501
       If renewkeys=0, the draw will be in the same order, guaranteeing that the same  # noqa: E501
       number will be drawn in not less than the number of integers of the sequence"""
    def __init__(self, inf, sup, seed=..., forever=..., renewkeys=...) -> None:
        ...
    
    def __iter__(self): # -> Self@RandomEnumeration:
        ...
    
    def next(self):
        ...
    
    __next__ = ...


class VolatileValue:
    def __repr__(self): # -> str:
        ...
    
    def command(self): # -> str:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __ne__(self, other) -> bool:
        ...
    
    __hash__ = ...
    def __getattr__(self, attr): # -> Any:
        ...
    
    def __str__(self) -> str:
        ...
    
    def __bytes__(self): # -> bytes:
        ...
    
    def __len__(self): # -> int:
        ...
    
    def copy(self): # -> Self@VolatileValue:
        ...
    


class RandField(VolatileValue):
    ...


class _RandNumeral(RandField):
    """Implements integer management in RandField"""
    def __int__(self) -> int:
        ...
    
    def __index__(self): # -> int:
        ...
    
    def __nonzero__(self): # -> bool:
        ...
    
    __bool__ = ...
    def __add__(self, other):
        ...
    
    def __radd__(self, other):
        ...
    
    def __sub__(self, other):
        ...
    
    def __rsub__(self, other):
        ...
    
    def __mul__(self, other):
        ...
    
    def __rmul__(self, other):
        ...
    
    def __floordiv__(self, other):
        ...
    
    __div__ = ...
    def __lt__(self, other) -> bool:
        ...
    
    def __le__(self, other) -> bool:
        ...
    
    def __ge__(self, other) -> bool:
        ...
    
    def __gt__(self, other) -> bool:
        ...
    
    def __lshift__(self, other):
        ...
    
    def __rshift__(self, other):
        ...
    
    def __and__(self, other):
        ...
    
    def __rand__(self, other):
        ...
    
    def __or__(self, other):
        ...
    
    def __ror__(self, other): # -> NoneType:
        ...
    


class RandNum(_RandNumeral):
    """Instances evaluate to random integers in selected range"""
    min = ...
    max = ...
    def __init__(self, min, max) -> None:
        ...
    


class RandFloat(RandNum):
    ...


class RandBinFloat(RandNum):
    ...


class RandNumGamma(_RandNumeral):
    def __init__(self, alpha, beta) -> None:
        ...
    


class RandNumGauss(_RandNumeral):
    def __init__(self, mu, sigma) -> None:
        ...
    


class RandNumExpo(_RandNumeral):
    def __init__(self, lambd, base=...) -> None:
        ...
    


class RandEnum(RandNum):
    """Instances evaluate to integer sampling without replacement from the given interval"""
    def __init__(self, min, max, seed=...) -> None:
        ...
    


class RandByte(RandNum):
    def __init__(self) -> None:
        ...
    


class RandSByte(RandNum):
    def __init__(self) -> None:
        ...
    


class RandShort(RandNum):
    def __init__(self) -> None:
        ...
    


class RandSShort(RandNum):
    def __init__(self) -> None:
        ...
    


class RandInt(RandNum):
    def __init__(self) -> None:
        ...
    


class RandSInt(RandNum):
    def __init__(self) -> None:
        ...
    


class RandLong(RandNum):
    def __init__(self) -> None:
        ...
    


class RandSLong(RandNum):
    def __init__(self) -> None:
        ...
    


class RandEnumByte(RandEnum):
    def __init__(self) -> None:
        ...
    


class RandEnumSByte(RandEnum):
    def __init__(self) -> None:
        ...
    


class RandEnumShort(RandEnum):
    def __init__(self) -> None:
        ...
    


class RandEnumSShort(RandEnum):
    def __init__(self) -> None:
        ...
    


class RandEnumInt(RandEnum):
    def __init__(self) -> None:
        ...
    


class RandEnumSInt(RandEnum):
    def __init__(self) -> None:
        ...
    


class RandEnumLong(RandEnum):
    def __init__(self) -> None:
        ...
    


class RandEnumSLong(RandEnum):
    def __init__(self) -> None:
        ...
    


class RandEnumKeys(RandEnum):
    """Picks a random value from dict keys list. """
    def __init__(self, enum, seed=...) -> None:
        ...
    


class RandChoice(RandField):
    def __init__(self, *args) -> None:
        ...
    


class RandString(RandField):
    _DEFAULT_CHARS = ...
    def __init__(self, size=..., chars=...) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    
    def __bytes__(self): # -> bytes:
        ...
    
    def __mul__(self, n):
        ...
    


class RandBin(RandString):
    def __init__(self, size=...) -> None:
        ...
    


class RandTermString(RandBin):
    def __init__(self, size, term) -> None:
        ...
    


class RandIP(RandString):
    _DEFAULT_IPTEMPLATE = ...
    def __init__(self, iptemplate=...) -> None:
        ...
    


class RandMAC(RandString):
    def __init__(self, template=...) -> None:
        ...
    


class RandIP6(RandString):
    def __init__(self, ip6template=...) -> None:
        ...
    


class RandOID(RandString):
    def __init__(self, fmt=..., depth=..., idnum=...) -> None:
        ...
    
    def __repr__(self): # -> str:
        ...
    


class RandRegExp(RandField):
    def __init__(self, regexp, lambda_=...) -> None:
        ...
    
    special_sets = ...
    @staticmethod
    def choice_expand(s): # -> str:
        ...
    
    @staticmethod
    def stack_fix(lst, index):
        ...
    
    def __repr__(self): # -> str:
        ...
    


class RandSingularity(RandChoice):
    ...


class RandSingNum(RandSingularity):
    @staticmethod
    def make_power_of_two(end): # -> set[Unknown]:
        ...
    
    def __init__(self, mn, mx) -> None:
        ...
    


class RandSingByte(RandSingNum):
    def __init__(self) -> None:
        ...
    


class RandSingSByte(RandSingNum):
    def __init__(self) -> None:
        ...
    


class RandSingShort(RandSingNum):
    def __init__(self) -> None:
        ...
    


class RandSingSShort(RandSingNum):
    def __init__(self) -> None:
        ...
    


class RandSingInt(RandSingNum):
    def __init__(self) -> None:
        ...
    


class RandSingSInt(RandSingNum):
    def __init__(self) -> None:
        ...
    


class RandSingLong(RandSingNum):
    def __init__(self) -> None:
        ...
    


class RandSingSLong(RandSingNum):
    def __init__(self) -> None:
        ...
    


class RandSingString(RandSingularity):
    def __init__(self) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    
    def __bytes__(self): # -> bytes:
        ...
    


class RandPool(RandField):
    def __init__(self, *args) -> None:
        """Each parameter is a volatile object or a couple (volatile object, weight)"""
        ...
    


class RandUUID(RandField):
    """Generates a random UUID.

    By default, this generates a RFC 4122 version 4 UUID (totally random).

    See Python's ``uuid`` module documentation for more information.

    Args:
        template (optional): A template to build the UUID from. Not valid with
                             any other option.
        node (optional): A 48-bit Host ID. Only valid for version 1 (where it
                         is optional).
        clock_seq (optional): An integer of up to 14-bits for the sequence
                              number. Only valid for version 1 (where it is
                              optional).
        namespace: A namespace identifier, which is also a UUID. Required for
                   versions 3 and 5, must be omitted otherwise.
        name: string, required for versions 3 and 5, must be omitted otherwise.
        version: Version of UUID to use (1, 3, 4 or 5). If omitted, attempts to
                 guess which version to generate, defaulting to version 4
                 (totally random).

    Raises:
        ValueError: on invalid constructor arguments
    """
    _BASE = ...
    _REG = ...
    VERSIONS = ...
    def __init__(self, template=..., node=..., clock_seq=..., namespace=..., name=..., version=...) -> None:
        ...
    


class AutoTime(_RandNumeral):
    def __init__(self, base=..., diff=...) -> None:
        ...
    


class IntAutoTime(AutoTime):
    ...


class ZuluTime(AutoTime):
    def __init__(self, diff=...) -> None:
        ...
    


class GeneralizedTime(AutoTime):
    def __init__(self, diff=...) -> None:
        ...
    


class DelayedEval(VolatileValue):
    """ Example of usage: DelayedEval("time.time()") """
    def __init__(self, expr) -> None:
        ...
    


class IncrementalValue(VolatileValue):
    def __init__(self, start=..., step=..., restart=...) -> None:
        ...
    


class CorruptedBytes(VolatileValue):
    def __init__(self, s, p=..., n=...) -> None:
        ...
    


class CorruptedBits(CorruptedBytes):
    ...


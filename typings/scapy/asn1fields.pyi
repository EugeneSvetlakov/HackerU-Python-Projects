"""
This type stub file was generated by pyright.
"""

"""
Classes that implement ASN.1 data structures.
"""
class ASN1F_badsequence(Exception):
    ...


class ASN1F_element:
    ...


class ASN1F_field(ASN1F_element):
    holds_packets = ...
    islist = ...
    ASN1_tag = ...
    context = ...
    def __init__(self, name, default, context=..., implicit_tag=..., explicit_tag=..., flexible_tag=...) -> None:
        ...
    
    def i2repr(self, pkt, x): # -> str:
        ...
    
    def i2h(self, pkt, x):
        ...
    
    def any2i(self, pkt, x):
        ...
    
    def m2i(self, pkt, s):
        """
        The good thing about safedec is that it may still decode ASN1
        even if there is a mismatch between the expected tag (self.ASN1_tag)
        and the actual tag; the decoded ASN1 object will simply be put
        into an ASN1_BADTAG object. However, safedec prevents the raising of
        exceptions needed for ASN1F_optional processing.
        Thus we use 'flexible_tag', which should be False with ASN1F_optional.

        Regarding other fields, we might need to know whether encoding went
        as expected or not. Noticeably, input methods from cert.py expect
        certain exceptions to be raised. Hence default flexible_tag is False.
        """
        ...
    
    def i2m(self, pkt, x): # -> Literal[b'']:
        ...
    
    def extract_packet(self, cls, s): # -> tuple[Unknown | Raw, Unknown | Literal[b'']] | tuple[None, Unknown]:
        ...
    
    def build(self, pkt): # -> Literal[b'']:
        ...
    
    def dissect(self, pkt, s):
        ...
    
    def do_copy(self, x): # -> list[Unknown]:
        ...
    
    def set_val(self, pkt, val): # -> None:
        ...
    
    def is_empty(self, pkt): # -> bool:
        ...
    
    def get_fields_list(self): # -> list[Self@ASN1F_field]:
        ...
    
    def __str__(self) -> str:
        ...
    
    def randval(self): # -> RandInt:
        ...
    


class ASN1F_BOOLEAN(ASN1F_field):
    ASN1_tag = ...
    def randval(self): # -> RandChoice:
        ...
    


class ASN1F_INTEGER(ASN1F_field):
    ASN1_tag = ...
    def randval(self): # -> RandNum:
        ...
    


class ASN1F_enum_INTEGER(ASN1F_INTEGER):
    def __init__(self, name, default, enum, context=..., implicit_tag=..., explicit_tag=...) -> None:
        ...
    
    def i2m(self, pkt, s): # -> Literal[b'']:
        ...
    
    def i2repr(self, pkt, x): # -> str:
        ...
    


class ASN1F_BIT_STRING(ASN1F_field):
    ASN1_tag = ...
    def __init__(self, name, default, default_readable=..., context=..., implicit_tag=..., explicit_tag=...) -> None:
        ...
    
    def randval(self): # -> RandString:
        ...
    


class ASN1F_STRING(ASN1F_field):
    ASN1_tag = ...
    def randval(self): # -> RandString:
        ...
    


class ASN1F_NULL(ASN1F_INTEGER):
    ASN1_tag = ...


class ASN1F_OID(ASN1F_field):
    ASN1_tag = ...
    def randval(self): # -> RandOID:
        ...
    


class ASN1F_ENUMERATED(ASN1F_enum_INTEGER):
    ASN1_tag = ...


class ASN1F_UTF8_STRING(ASN1F_STRING):
    ASN1_tag = ...


class ASN1F_NUMERIC_STRING(ASN1F_STRING):
    ASN1_tag = ...


class ASN1F_PRINTABLE_STRING(ASN1F_STRING):
    ASN1_tag = ...


class ASN1F_T61_STRING(ASN1F_STRING):
    ASN1_tag = ...


class ASN1F_VIDEOTEX_STRING(ASN1F_STRING):
    ASN1_tag = ...


class ASN1F_IA5_STRING(ASN1F_STRING):
    ASN1_tag = ...


class ASN1F_UTC_TIME(ASN1F_STRING):
    ASN1_tag = ...
    def randval(self): # -> GeneralizedTime:
        ...
    


class ASN1F_GENERALIZED_TIME(ASN1F_STRING):
    ASN1_tag = ...
    def randval(self): # -> GeneralizedTime:
        ...
    


class ASN1F_ISO646_STRING(ASN1F_STRING):
    ASN1_tag = ...


class ASN1F_UNIVERSAL_STRING(ASN1F_STRING):
    ASN1_tag = ...


class ASN1F_BMP_STRING(ASN1F_STRING):
    ASN1_tag = ...


class ASN1F_SEQUENCE(ASN1F_field):
    ASN1_tag = ...
    holds_packets = ...
    def __init__(self, *seq, **kwargs) -> None:
        ...
    
    def __repr__(self): # -> str:
        ...
    
    def is_empty(self, pkt): # -> bool:
        ...
    
    def get_fields_list(self): # -> list[Unknown]:
        ...
    
    def m2i(self, pkt, s):
        """
        ASN1F_SEQUENCE behaves transparently, with nested ASN1_objects being
        dissected one by one. Because we use obj.dissect (see loop below)
        instead of obj.m2i (as we trust dissect to do the appropriate set_vals)
        we do not directly retrieve the list of nested objects.
        Thus m2i returns an empty list (along with the proper remainder).
        It is discarded by dissect() and should not be missed elsewhere.
        """
        ...
    
    def dissect(self, pkt, s):
        ...
    
    def build(self, pkt): # -> Literal[b'']:
        ...
    


class ASN1F_SET(ASN1F_SEQUENCE):
    ASN1_tag = ...


class ASN1F_SEQUENCE_OF(ASN1F_field):
    ASN1_tag = ...
    holds_packets = ...
    islist = ...
    def __init__(self, name, default, cls, context=..., implicit_tag=..., explicit_tag=...) -> None:
        ...
    
    def is_empty(self, pkt): # -> bool:
        ...
    
    def m2i(self, pkt, s): # -> tuple[list[Unknown], Unknown]:
        ...
    
    def build(self, pkt): # -> Literal[b'']:
        ...
    
    def randval(self): # -> Packet:
        ...
    
    def __repr__(self): # -> str:
        ...
    


class ASN1F_SET_OF(ASN1F_SEQUENCE_OF):
    ASN1_tag = ...


class ASN1F_IPADDRESS(ASN1F_STRING):
    ASN1_tag = ...


class ASN1F_TIME_TICKS(ASN1F_INTEGER):
    ASN1_tag = ...


class ASN1F_optional(ASN1F_element):
    def __init__(self, field) -> None:
        ...
    
    def __getattr__(self, attr): # -> Any:
        ...
    
    def m2i(self, pkt, s): # -> tuple[None, Unknown]:
        ...
    
    def dissect(self, pkt, s):
        ...
    
    def build(self, pkt): # -> Literal[b'']:
        ...
    
    def any2i(self, pkt, x):
        ...
    
    def i2repr(self, pkt, x):
        ...
    


class ASN1F_CHOICE(ASN1F_field):
    """
    Multiple types are allowed: ASN1_Packet, ASN1F_field and ASN1F_PACKET(),
    See layers/x509.py for examples.
    Other ASN1F_field instances than ASN1F_PACKET instances must not be used.
    """
    holds_packets = ...
    ASN1_tag = ...
    def __init__(self, name, default, *args, **kwargs) -> None:
        ...
    
    def m2i(self, pkt, s): # -> tuple[ASN1F_field | Unknown | Raw, Unknown | Literal[b'']] | tuple[None, Unknown]:
        """
        First we have to retrieve the appropriate choice.
        Then we extract the field/packet, according to this choice.
        """
        ...
    
    def i2m(self, pkt, x): # -> bytes:
        ...
    
    def randval(self): # -> RandChoice:
        ...
    


class ASN1F_PACKET(ASN1F_field):
    holds_packets = ...
    def __init__(self, name, default, cls, context=..., implicit_tag=..., explicit_tag=...) -> None:
        ...
    
    def m2i(self, pkt, s): # -> tuple[Unknown | Raw | None, Unknown | Literal[b'']]:
        ...
    
    def i2m(self, pkt, x): # -> bytes:
        ...
    
    def randval(self): # -> Packet:
        ...
    


class ASN1F_BIT_STRING_ENCAPS(ASN1F_BIT_STRING):
    """
    We may emulate simple string encapsulation with explicit_tag=0x04,
    but we need a specific class for bit strings because of unused bits, etc.
    """
    holds_packets = ...
    def __init__(self, name, default, cls, context=..., implicit_tag=..., explicit_tag=...) -> None:
        ...
    
    def m2i(self, pkt, s): # -> tuple[Unknown | Raw | None, Unknown]:
        ...
    
    def i2m(self, pkt, x): # -> Literal[b'']:
        ...
    


class ASN1F_FLAGS(ASN1F_BIT_STRING):
    def __init__(self, name, default, mapping, context=..., implicit_tag=..., explicit_tag=...) -> None:
        ...
    
    def get_flags(self, pkt): # -> list[Unknown]:
        ...
    
    def i2repr(self, pkt, x): # -> str:
        ...
    



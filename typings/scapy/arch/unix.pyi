"""
This type stub file was generated by pyright.
"""

from scapy.compat import List, Tuple

"""
Common customizations for all Unix-like operating systems other than Linux
"""
def read_routes() -> List[Tuple[int, int, str, str, str, int]]:
    """Return a list of IPv4 routes than can be used by Scapy.

    This function parses netstat.
    """
    ...

def in6_getifaddr() -> List[Tuple[str, int, str]]:
    """
    Returns a list of 3-tuples of the form (addr, scope, iface) where
    'addr' is the address of scope 'scope' associated to the interface
    'iface'.

    This is the list of all addresses of all interfaces available on
    the system.
    """
    ...

def read_routes6() -> List[Tuple[str, int, str, str, List[str], int]]:
    """Return a list of IPv6 routes than can be used by Scapy.

    This function parses netstat.
    """
    ...


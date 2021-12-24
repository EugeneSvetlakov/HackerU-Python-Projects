"""
This type stub file was generated by pyright.
"""

from ctypes import Structure
from scapy.interfaces import InterfaceProvider

"""
Scapy *BSD native support - core
"""
LIBC = ...
class if_nameindex(Structure):
    _fields_ = ...


_ptr_ifnameindex_table = ...
def get_if_raw_addr(ifname): # -> bytes:
    """Returns the IPv4 address configured on 'ifname', packed with inet_pton."""
    ...

def get_if_raw_hwaddr(ifname): # -> tuple[Literal[772], bytes] | tuple[Literal[1], str]:
    """Returns the packed MAC address configured on 'ifname'."""
    ...

def get_dev_bpf(): # -> tuple[int, Unknown]:
    """Returns an opened BPF file object"""
    ...

def attach_filter(fd, bpf_filter, iface): # -> None:
    """Attach a BPF filter to the BPF file descriptor"""
    ...

_IFNUM = ...
class BPFInterfaceProvider(InterfaceProvider):
    name = ...
    def load(self): # -> dict[Unknown, Unknown]:
        ...
    



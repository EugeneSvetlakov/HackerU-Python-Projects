"""
This type stub file was generated by pyright.
"""

from scapy.automaton import SelectableObject
from scapy.supersocket import SuperSocket

"""
Native Microsoft Windows sockets (L3 only)

## Notice: ICMP packets

DISCLAIMER: Please use Npcap/Winpcap to send/receive ICMP. It is going to work.
Below is some additional information, mainly implemented in a testing purpose.

When in native mode, everything goes through the Windows kernel.
This firstly requires that the Firewall is open. Be sure it allows ICMPv4/6
packets in and out.
Windows may drop packets that it finds wrong. for instance, answers to
ICMP packets with id=0 or seq=0 may be dropped. It means that sent packets
should (most of the time) be perfectly built.

A perfectly built ICMP req packet on Windows means that its id is 1, its
checksum (IP and ICMP) are correctly built, but also that its seq number is
in the "allowed range".
    In fact, every time an ICMP packet is sent on Windows, a global sequence
number is increased, which is only reset at boot time. The seq number of the
received ICMP packet must be in the range [current, current + 3] to be valid,
and received by the socket. The current number is quite hard to get, thus we
provide in this module the get_actual_icmp_seq() function.

Example:
    >>> conf.use_pcap = False
    >>> a = conf.L3socket()
    # This will (most likely) work:
    >>> current = get_current_icmp_seq()
    >>> a.sr(IP(dst="www.google.com", ttl=128)/ICMP(id=1, seq=current))
    # This won't:
    >>> a.sr(IP(dst="www.google.com", ttl=128)/ICMP())

PS: on computers where the firewall isn't open, Windows temporarily opens it
when using the `ping` util from cmd.exe. One can first call a ping on cmd,
then do custom calls through the socket using get_current_icmp_seq(). See
the tests (windows.uts) for an example.
"""
class L3WinSocket(SuperSocket, SelectableObject):
    desc = ...
    nonblocking_socket = ...
    __selectable_force_select__ = ...
    __slots__ = ...
    def __init__(self, iface=..., proto=..., ttl=..., ipv6=..., promisc=..., **kwargs) -> None:
        ...
    
    def send(self, x): # -> None:
        ...
    
    def nonblock_recv(self, x=...): # -> None:
        ...
    
    def recv_raw(self, x=...): # -> tuple[None, None, None] | tuple[Type[IPv6], bytes, float] | tuple[Unknown, bytes, float]:
        ...
    
    def close(self): # -> None:
        ...
    
    @staticmethod
    def select(sockets, remain=...):
        ...
    


class L3WinSocket6(L3WinSocket):
    desc = ...
    def __init__(self, **kwargs) -> None:
        ...
    


def open_icmp_firewall(host): # -> int:
    """Temporarily open the ICMP firewall. Tricks Windows into allowing
    ICMP packets for a short period of time (~ 1 minute)"""
    ...

def get_current_icmp_seq():
    """See help(scapy.arch.windows.native) for more information.
    Returns the current ICMP seq number."""
    ...


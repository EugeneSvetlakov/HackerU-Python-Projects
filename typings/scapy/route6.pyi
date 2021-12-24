"""
This type stub file was generated by pyright.
"""

from scapy.compat import Any, List, Optional, Tuple

"""
Routing and network interface handling for IPv6.
"""
class Route6:
    def __init__(self) -> None:
        ...
    
    def invalidate_cache(self) -> None:
        ...
    
    def flush(self) -> None:
        ...
    
    def resync(self) -> None:
        ...
    
    def __repr__(self) -> str:
        ...
    
    def make_route(self, dst: str, gw: Optional[str] = ..., dev: Optional[str] = ...) -> Tuple[str, int, str, str, List[str], int]:
        """Internal function : create a route for 'dst' via 'gw'.
        """
        ...
    
    def add(self, *args: Any, **kargs: Any) -> None:
        """Ex:
        add(dst="2001:db8:cafe:f000::/56")
        add(dst="2001:db8:cafe:f000::/56", gw="2001:db8:cafe::1")
        add(dst="2001:db8:cafe:f000::/64", gw="2001:db8:cafe::1", dev="eth0")
        """
        ...
    
    def remove_ipv6_iface(self, iface: str) -> None:
        """
        Remove the network interface 'iface' from the list of interfaces
        supporting IPv6.
        """
        ...
    
    def delt(self, dst: str, gw: Optional[str] = ...) -> None:
        """ Ex:
        delt(dst="::/0")
        delt(dst="2001:db8:cafe:f000::/56")
        delt(dst="2001:db8:cafe:f000::/56", gw="2001:db8:deca::1")
        """
        ...
    
    def ifchange(self, iff: str, addr: str) -> None:
        ...
    
    def ifdel(self, iff: str) -> None:
        """ removes all route entries that uses 'iff' interface. """
        ...
    
    def ifadd(self, iff: str, addr: str) -> None:
        """
        Add an interface 'iff' with provided address into routing table.

        Ex: ifadd('eth0', '2001:bd8:cafe:1::1/64') will add following entry into  # noqa: E501
            Scapy6 internal routing table:

            Destination           Next Hop  iface  Def src @           Metric
            2001:bd8:cafe:1::/64  ::        eth0   2001:bd8:cafe:1::1  1

            prefix length value can be omitted. In that case, a value of 128
            will be used.
        """
        ...
    
    def route(self, dst: str = ..., dev: Optional[Any] = ..., verbose: int = ...) -> Tuple[str, str, str]:
        """
        Provide best route to IPv6 destination address, based on Scapy
        internal routing table content.

        When a set of address is passed (e.g. ``2001:db8:cafe:*::1-5``) an
        address of the set is used. Be aware of that behavior when using
        wildcards in upper parts of addresses !

        If 'dst' parameter is a FQDN, name resolution is performed and result
        is used.

        if optional 'dev' parameter is provided a specific interface, filtering
        is performed to limit search to route associated to that interface.
        """
        ...
    



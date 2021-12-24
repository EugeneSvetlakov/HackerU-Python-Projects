"""
This type stub file was generated by pyright.
"""

from scapy.compat import Any, List, Optional, Tuple

"""
Routing and handling of network interfaces.
"""
class Route:
    def __init__(self) -> None:
        ...
    
    def invalidate_cache(self) -> None:
        ...
    
    def resync(self) -> None:
        ...
    
    def __repr__(self) -> str:
        ...
    
    def make_route(self, host: Optional[str] = ..., net: Optional[str] = ..., gw: Optional[str] = ..., dev: Optional[str] = ..., metric: int = ...) -> Tuple[int, int, str, str, str, int]:
        ...
    
    def add(self, *args: Any, **kargs: Any) -> None:
        """Ex:
        add(net="192.168.1.0/24",gw="1.2.3.4")
        """
        ...
    
    def delt(self, *args: Any, **kargs: Any) -> None:
        """delt(host|net, gw|dev)"""
        ...
    
    def ifchange(self, iff: str, addr: str) -> None:
        ...
    
    def ifdel(self, iff: str) -> None:
        ...
    
    def ifadd(self, iff: str, addr: str) -> None:
        ...
    
    def route(self, dst: Optional[str] = ..., verbose: int = ...) -> Tuple[str, str, str]:
        """Returns the IPv4 routes to a host.
        parameters:
         - dst: the IPv4 of the destination host

        returns: (iface, output_ip, gateway_ip)
         - iface: the interface used to connect to the host
         - output_ip: the outgoing IP that will be used
         - gateway_ip: the gateway IP that will be used
        """
        ...
    
    def get_if_bcast(self, iff: str) -> List[str]:
        ...
    



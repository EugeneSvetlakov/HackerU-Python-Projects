"""
This type stub file was generated by pyright.
"""

from scapy.compat import Any, Callable, Optional
from scapy.packet import Packet
from scapy.plist import PacketList

"""
Sessions: decode flow of packets when sniffing
"""
class DefaultSession:
    """Default session: no stream decoding"""
    def __init__(self, prn: Optional[Callable[[Packet], Any]] = ..., store: bool = ..., supersession: Optional[DefaultSession] = ..., *args: Any, **karg: Any) -> None:
        ...
    
    @property
    def store(self) -> bool:
        ...
    
    @store.setter
    def store(self, val: bool) -> None:
        ...
    
    @property
    def prn(self) -> Optional[Callable[[Packet], Any]]:
        ...
    
    @prn.setter
    def prn(self, f: Optional[Any]) -> None:
        ...
    
    @property
    def count(self) -> int:
        ...
    
    def toPacketList(self) -> PacketList:
        ...
    
    def on_packet_received(self, pkt: Optional[Packet]) -> None:
        """DEV: entry point. Will be called by sniff() for each
        received packet (that passes the filters).
        """
        ...
    


class IPSession(DefaultSession):
    """Defragment IP packets 'on-the-flow'.

    Usage:
    >>> sniff(session=IPSession)
    """
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        ...
    
    def on_packet_received(self, pkt: Optional[Packet]) -> None:
        ...
    


class StringBuffer:
    """StringBuffer is an object used to re-order data received during
    a TCP transmission.

    Each TCP fragment contains a sequence number, which marks
    (relatively to the first sequence number) the index of the data contained
    in the fragment.

    If a TCP fragment is missed, this class will fill the missing space with
    zeros.
    """
    def __init__(self) -> None:
        ...
    
    def append(self, data: bytes, seq: int) -> None:
        ...
    
    def full(self) -> bool:
        ...
    
    def clear(self) -> None:
        ...
    
    def __bool__(self) -> bool:
        ...
    
    __nonzero__ = ...
    def __len__(self) -> int:
        ...
    
    def __bytes__(self) -> bytes:
        ...
    
    def __str__(self) -> str:
        ...
    


class TCPSession(IPSession):
    """A Session that matches seq/ack packets together to dissect
    special protocols, such as HTTP.

    DEV: implement a class-function `tcp_reassemble` in your Packet class::

        @classmethod
        def tcp_reassemble(cls, data, metadata):
            # data = the reassembled data from the same request/flow
            # metadata = empty dictionary, that can be used to store data
            [...]
            # If the packet is available, return it. Otherwise don't.
            # Whenever you return a packet, the buffer will be discarded.
            return pkt
            # Otherwise, maybe store stuff in metadata, and return None,
            # as you need additional data.
            return None

    For more details and a real example, see:
    https://scapy.readthedocs.io/en/latest/usage.html#how-to-use-tcpsession-to-defragment-tcp-packets

    :param app: Whether the socket is on application layer = has no TCP
                layer. This is used for instance if you are using a native
                TCP socket. Default to False
    """
    fmt = ...
    def __init__(self, app: bool = ..., *args: Any, **kwargs: Any) -> None:
        ...
    
    def on_packet_received(self, pkt: Optional[Packet]) -> None:
        """Hook to the Sessions API: entry point of the dissection.
        This will defragment IP if necessary, then process to
        TCP reassembly.
        """
        ...
    



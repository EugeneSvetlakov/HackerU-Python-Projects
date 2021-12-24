"""
This type stub file was generated by pyright.
"""

import scapy.modules.six as six
from scapy.compat import Any, Callable, Dict, Generic, Iterator, List, Optional, Tuple, Type, Union
from scapy.base_classes import BasePacketList, PacketList_metaclass, SetGen, _CanvasDumpExtended
from scapy.extlib import Line2D
from scapy.packet import Packet

"""
PacketList: holds several packets and allows to do operations on them.
"""
QueryAnswer = ...
_Inner = ...
@six.add_metaclass(PacketList_metaclass)
class _PacketList(Generic[_Inner]):
    __slots__ = ...
    def __init__(self, res: Optional[Union[_PacketList[_Inner], List[_Inner]]] = ..., name: str = ..., stats: Optional[List[Type[Packet]]] = ...) -> None:
        """create a packet list from a list of packets
           res: the list of packets
           stats: a list of classes that will appear in the stats (defaults to [TCP,UDP,ICMP])"""
        ...
    
    def __len__(self) -> int:
        ...
    
    def __repr__(self) -> str:
        ...
    
    def __getstate__(self) -> Dict[str, Any]:
        """
        Creates a basic representation of the instance, used in
        conjunction with __setstate__() e.g. by pickle

        :returns: dict representing this instance
        """
        ...
    
    def __setstate__(self, state: Dict[str, Any]) -> None:
        """
        Sets instance attributes to values given by state, used in
        conjunction with __getstate__() e.g. by pickle

        :param state: dict representing this instance
        """
        ...
    
    def __iter__(self) -> Iterator[_Inner]:
        ...
    
    def __getattr__(self, attr: str) -> Any:
        ...
    
    def __getitem__(self, item: Any) -> Any:
        ...
    
    _T = ...
    def __add__(self: _PacketList._T, other: _PacketList._T) -> _PacketList._T:
        ...
    
    def summary(self, prn: Optional[Callable[..., Any]] = ..., lfilter: Optional[Callable[..., bool]] = ...) -> None:
        """prints a summary of each packet

        :param prn: function to apply to each packet instead of
                    lambda x:x.summary()
        :param lfilter: truth function to apply to each packet to decide
                        whether it will be displayed
        """
        ...
    
    def nsummary(self, prn: Optional[Callable[..., Any]] = ..., lfilter: Optional[Callable[..., bool]] = ...) -> None:
        """prints a summary of each packet with the packet's number

        :param prn: function to apply to each packet instead of
                    lambda x:x.summary()
        :param lfilter: truth function to apply to each packet to decide
                        whether it will be displayed
        """
        ...
    
    def show(self, *args: Any, **kargs: Any) -> None:
        """Best way to display the packet list. Defaults to nsummary() method"""
        ...
    
    def filter(self, func: Callable[..., bool]) -> _PacketList[_Inner]:
        """Returns a packet list filtered by a truth function. This truth
        function has to take a packet as the only argument and return
        a boolean value.
        """
        ...
    
    def make_table(self, *args: Any, **kargs: Any) -> Optional[str]:
        """Prints a table using a function that returns for each packet its head column value, head row value and displayed value  # noqa: E501
        ex: p.make_table(lambda x:(x[IP].dst, x[TCP].dport, x[TCP].sprintf("%flags%")) """
        ...
    
    def make_lined_table(self, *args: Any, **kargs: Any) -> Optional[str]:
        """Same as make_table, but print a table with lines"""
        ...
    
    def make_tex_table(self, *args: Any, **kargs: Any) -> Optional[str]:
        """Same as make_table, but print a table with LaTeX syntax"""
        ...
    
    def plot(self, f: Callable[..., Any], lfilter: Optional[Callable[..., bool]] = ..., plot_xy: bool = ..., **kargs: Any) -> Line2D:
        """Applies a function to each packet to get a value that will be plotted
        with matplotlib. A list of matplotlib.lines.Line2D is returned.

        lfilter: a truth function that decides whether a packet must be plotted
        """
        ...
    
    def diffplot(self, f: Callable[..., Any], delay: int = ..., lfilter: Optional[Callable[..., bool]] = ..., **kargs: Any) -> Line2D:
        """diffplot(f, delay=1, lfilter=None)
        Applies a function to couples (l[i],l[i+delay])

        A list of matplotlib.lines.Line2D is returned.
        """
        ...
    
    def multiplot(self, f: Callable[..., Any], lfilter: Optional[Callable[..., Any]] = ..., plot_xy: bool = ..., **kargs: Any) -> Line2D:
        """Uses a function that returns a label and a value for this label, then
        plots all the values label by label.

        A list of matplotlib.lines.Line2D is returned.
        """
        ...
    
    def rawhexdump(self) -> None:
        """Prints an hexadecimal dump of each packet in the list"""
        ...
    
    def hexraw(self, lfilter: Optional[Callable[..., bool]] = ...) -> None:
        """Same as nsummary(), except that if a packet has a Raw layer, it will be hexdumped  # noqa: E501
        lfilter: a truth function that decides whether a packet must be displayed"""
        ...
    
    def hexdump(self, lfilter: Optional[Callable[..., bool]] = ...) -> None:
        """Same as nsummary(), except that packets are also hexdumped
        lfilter: a truth function that decides whether a packet must be displayed"""
        ...
    
    def padding(self, lfilter: Optional[Callable[..., bool]] = ...) -> None:
        """Same as hexraw(), for Padding layer"""
        ...
    
    def nzpadding(self, lfilter: Optional[Callable[..., bool]] = ...) -> None:
        """Same as padding() but only non null padding"""
        ...
    
    def conversations(self, getsrcdst: Optional[Callable[[Packet], Tuple[Any, ...]]] = ..., **kargs: Any) -> Any:
        """Graphes a conversations between sources and destinations and display it
        (using graphviz and imagemagick)

        :param getsrcdst: a function that takes an element of the list and
            returns the source, the destination and optionally
            a label. By default, returns the IP source and
            destination from IP and ARP layers
        :param type: output type (svg, ps, gif, jpg, etc.), passed to dot's
            "-T" option
        :param target: filename or redirect. Defaults pipe to Imagemagick's
            display program
        :param prog: which graphviz program to use
        """
        ...
    
    def afterglow(self, src: Optional[Callable[[_Inner], Any]] = ..., event: Optional[Callable[[_Inner], Any]] = ..., dst: Optional[Callable[[_Inner], Any]] = ..., **kargs: Any) -> Any:
        """Experimental clone attempt of http://sourceforge.net/projects/afterglow
        each datum is reduced as src -> event -> dst and the data are graphed.
        by default we have IP.src -> IP.dport -> IP.dst"""
        ...
    
    def canvas_dump(self, **kargs: Any) -> Any:
        ...
    
    def sessions(self, session_extractor: Optional[Callable[[Packet], str]] = ...) -> Dict[str, _PacketList[_Inner]]:
        ...
    
    def replace(self, *args: Any, **kargs: Any) -> PacketList:
        """
        lst.replace(<field>,[<oldvalue>,]<newvalue>)
        lst.replace( (fld,[ov],nv),(fld,[ov,]nv),...)
          if ov is None, all values are replaced
        ex:
          lst.replace( IP.src, "192.168.1.1", "10.0.0.1" )
          lst.replace( IP.ttl, 64 )
          lst.replace( (IP.ttl, 64), (TCP.sport, 666, 777), )
        """
        ...
    
    def getlayer(self, cls: Packet, nb: Optional[int] = ..., flt: Optional[Dict[str, Any]] = ..., name: Optional[str] = ..., stats: Optional[List[Type[Packet]]] = ...) -> PacketList:
        """Returns the packet list from a given layer.

        See ``Packet.getlayer`` for more info.

        :param cls: search for a layer that is an instance of ``cls``
        :type cls: Type[scapy.packet.Packet]

        :param nb: return the nb^th layer that is an instance of ``cls``
        :type nb: Optional[int]

        :param flt: filter parameters for ``Packet.getlayer``
        :type flt: Optional[Dict[str, Any]]

        :param name: optional name for the new PacketList
        :type name: Optional[str]

        :param stats: optional list of protocols to give stats on; if not
                      specified, inherits from this PacketList.
        :type stats: Optional[List[Type[scapy.packet.Packet]]]
        :rtype: scapy.plist.PacketList
        """
        ...
    
    def convert_to(self, other_cls: Type[Packet], name: Optional[str] = ..., stats: Optional[List[Type[Packet]]] = ...) -> PacketList:
        """Converts all packets to another type.

        See ``Packet.convert_to`` for more info.

        :param other_cls: reference to a Packet class to convert to
        :type other_cls: Type[scapy.packet.Packet]

        :param name: optional name for the new PacketList
        :type name: Optional[str]

        :param stats: optional list of protocols to give stats on;
                      if not specified, inherits from this PacketList.
        :type stats: Optional[List[Type[scapy.packet.Packet]]]

        :rtype: scapy.plist.PacketList
        """
        ...
    


class PacketList(_PacketList[Packet], BasePacketList[Packet], _CanvasDumpExtended):
    def sr(self, multi: bool = ..., lookahead: Optional[int] = ...) -> Tuple[SndRcvList, PacketList]:
        """
        Matches packets in the list

        :param multi: True if a packet can have multiple answers
        :param lookahead: Maximum number of packets between packet and answer.
                          If 0 or None, full remaining list is
                          scanned for answers
        :return: ( (matched couples), (unmatched packets) )
        """
        ...
    


_PacketIterable = Union[List[Packet], Packet, SetGen[Packet], _PacketList[Packet]]
class SndRcvList(_PacketList[QueryAnswer], BasePacketList[QueryAnswer], _CanvasDumpExtended):
    __slots__: List[str] = ...
    def __init__(self, res: Optional[Union[_PacketList[QueryAnswer], List[QueryAnswer]]] = ..., name: str = ..., stats: Optional[List[Type[Packet]]] = ...) -> None:
        ...
    


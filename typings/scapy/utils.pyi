"""
This type stub file was generated by pyright.
"""

import gzip
import struct
import sys
import threading
import scapy.modules.six as six
from decimal import Decimal
from scapy.config import conf
from scapy.compat import Any, AnyStr, Callable, Dict, IO, Iterator, List, Literal, Optional, TYPE_CHECKING, Tuple, Type, Union, overload
from scapy.packet import Packet
from scapy.plist import PacketList, _PacketIterable
from scapy.supersocket import SuperSocket

"""
General utility functions.
"""
if TYPE_CHECKING:
    _SuperSocket = SuperSocket
else:
    ...
_ByteStream = Union[IO[bytes], gzip.GzipFile]
def issubtype(x: Any, t: Union[type, str]) -> bool:
    """issubtype(C, B) -> bool

    Return whether C is a class and if it is a subclass of class B.
    When using a tuple as the second argument issubtype(X, (A, B, ...)),
    is a shortcut for issubtype(X, A) or issubtype(X, B) or ... (etc.).
    """
    ...

_Decimal = Union[Decimal, int]
class EDecimal(Decimal):
    """Extended Decimal

    This implements arithmetic and comparison with float for
    backward compatibility
    """
    def __add__(self, other: _Decimal, context: Any = ...) -> EDecimal:
        ...
    
    def __radd__(self, other: _Decimal) -> EDecimal:
        ...
    
    def __sub__(self, other: _Decimal) -> EDecimal:
        ...
    
    def __rsub__(self, other: _Decimal) -> EDecimal:
        ...
    
    def __mul__(self, other: _Decimal) -> EDecimal:
        ...
    
    def __rmul__(self, other: _Decimal) -> EDecimal:
        ...
    
    def __truediv__(self, other: _Decimal) -> EDecimal:
        ...
    
    def __floordiv__(self, other: _Decimal) -> EDecimal:
        ...
    
    if sys.version_info >= (3, ):
        def __divmod__(self, other: _Decimal) -> Tuple[EDecimal, EDecimal]:
            ...
        
    else:
        ...
    def __mod__(self, other: _Decimal) -> EDecimal:
        ...
    
    def __rmod__(self, other: _Decimal) -> EDecimal:
        ...
    
    def __pow__(self, other: _Decimal, modulo: Optional[_Decimal] = ...) -> EDecimal:
        ...
    
    def __eq__(self, other: Any) -> bool:
        ...
    
    def normalize(self, precision: int) -> EDecimal:
        ...
    


@overload
def get_temp_file(keep: bool, autoext: str, fd: Literal[True]) -> IO[bytes]:
    ...

@overload
def get_temp_file(keep: bool = ..., autoext: str = ..., fd: Literal[False] = ...) -> str:
    ...

def get_temp_file(keep: bool = ..., autoext: str = ..., fd: bool = ...) -> Union[IO[bytes], str]:
    """Creates a temporary file.

    :param keep: If False, automatically delete the file when Scapy exits.
    :param autoext: Suffix to add to the generated file name.
    :param fd: If True, this returns a file-like object with the temporary
               file opened. If False (default), this returns a file path.
    """
    ...

def get_temp_dir(keep: bool = ...) -> str:
    """Creates a temporary file, and returns its name.

    :param keep: If False (default), the directory will be recursively
                 deleted when Scapy exits.
    :return: A full path to a temporary directory.
    """
    ...

def sane(x: AnyStr, color: bool = ...) -> str:
    ...

@conf.commands.register
def restart() -> None:
    """Restarts scapy"""
    ...

def lhex(x: Any) -> str:
    ...

@conf.commands.register
def hexdump(p: Union[Packet, AnyStr], dump: bool = ...) -> Optional[str]:
    """Build a tcpdump like hexadecimal view

    :param p: a Packet
    :param dump: define if the result must be printed or returned in a variable
    :return: a String only when dump=True
    """
    ...

@conf.commands.register
def linehexdump(p: Union[Packet, AnyStr], onlyasc: int = ..., onlyhex: int = ..., dump: bool = ...) -> Optional[str]:
    """Build an equivalent view of hexdump() on a single line

    Note that setting both onlyasc and onlyhex to 1 results in a empty output

    :param p: a Packet
    :param onlyasc: 1 to display only the ascii view
    :param onlyhex: 1 to display only the hexadecimal view
    :param dump: print the view if False
    :return: a String only when dump=True
    """
    ...

@conf.commands.register
def chexdump(p: Union[Packet, AnyStr], dump: bool = ...) -> Optional[str]:
    """Build a per byte hexadecimal representation

    Example:
        >>> chexdump(IP())
        0x45, 0x00, 0x00, 0x14, 0x00, 0x01, 0x00, 0x00, 0x40, 0x00, 0x7c, 0xe7, 0x7f, 0x00, 0x00, 0x01, 0x7f, 0x00, 0x00, 0x01  # noqa: E501

    :param p: a Packet
    :param dump: print the view if False
    :return: a String only if dump=True
    """
    ...

@conf.commands.register
def hexstr(p: Union[Packet, AnyStr], onlyasc: int = ..., onlyhex: int = ..., color: bool = ...) -> str:
    """Build a fancy tcpdump like hex from bytes."""
    ...

def repr_hex(s: bytes) -> str:
    """ Convert provided bitstring to a simple string of hex digits """
    ...

@conf.commands.register
def hexdiff(a: Union[Packet, AnyStr], b: Union[Packet, AnyStr], autojunk: bool = ...) -> None:
    """
    Show differences between 2 binary strings, Packets...

    For the autojunk parameter, see
    https://docs.python.org/3.8/library/difflib.html#difflib.SequenceMatcher

    :param a:
    :param b: The binary strings, packets... to compare
    :param autojunk: Setting it to True will likely increase the comparison
        speed a lot on big byte strings, but will reduce accuracy (will tend
        to miss insertion and see replacements instead for instance).
    """
    ...

if struct.pack("H", 1) == b"\x00\x01":
    checksum_endian_transform: Callable[[int], int] = ...
else:
    checksum_endian_transform = ...
def checksum(pkt: bytes) -> int:
    ...

@conf.commands.register
def fletcher16_checksum(binbuf: bytes) -> int:
    """Calculates Fletcher-16 checksum of the given buffer.

       Note:
       If the buffer contains the two checkbytes derived from the Fletcher-16 checksum  # noqa: E501
       the result of this function has to be 0. Otherwise the buffer has been corrupted.  # noqa: E501
    """
    ...

@conf.commands.register
def fletcher16_checkbytes(binbuf: bytes, offset: int) -> bytes:
    """Calculates the Fletcher-16 checkbytes returned as 2 byte binary-string.

       Including the bytes into the buffer (at the position marked by offset) the  # noqa: E501
       global Fletcher-16 checksum of the buffer will be 0. Thus it is easy to verify  # noqa: E501
       the integrity of the buffer on the receiver side.

       For details on the algorithm, see RFC 2328 chapter 12.1.7 and RFC 905 Annex B.  # noqa: E501
    """
    ...

def mac2str(mac: str) -> bytes:
    ...

def valid_mac(mac: str) -> bool:
    ...

def str2mac(s: bytes) -> str:
    ...

def randstring(length: int) -> bytes:
    """
    Returns a random string of length (length >= 0)
    """
    ...

def zerofree_randstring(length: int) -> bytes:
    """
    Returns a random string of length (length >= 0) without zero in it.
    """
    ...

def strxor(s1: bytes, s2: bytes) -> bytes:
    """
    Returns the binary XOR of the 2 provided strings s1 and s2. s1 and s2
    must be of same length.
    """
    ...

def strand(s1: bytes, s2: bytes) -> bytes:
    """
    Returns the binary AND of the 2 provided strings s1 and s2. s1 and s2
    must be of same length.
    """
    ...

inet_ntoa = ...
def atol(x: str) -> int:
    ...

def valid_ip(addr: str) -> bool:
    ...

def valid_net(addr: str) -> bool:
    ...

def valid_ip6(addr: str) -> bool:
    ...

def valid_net6(addr: str) -> bool:
    ...

def ltoa(x: int) -> str:
    ...

def itom(x: int) -> int:
    ...

class ContextManagerSubprocess:
    """
    Context manager that eases checking for unknown command, without
    crashing.

    Example:
    >>> with ContextManagerSubprocess("tcpdump"):
    >>>     subprocess.Popen(["tcpdump", "--version"])
    ERROR: Could not execute tcpdump, is it installed?

    """
    def __init__(self, prog: str, suppress: bool = ...) -> None:
        ...
    
    def __enter__(self) -> None:
        ...
    
    def __exit__(self, exc_type: Optional[type], exc_value: Optional[Exception], traceback: Optional[Any]) -> Optional[bool]:
        ...
    


class ContextManagerCaptureOutput:
    """
    Context manager that intercept the console's output.

    Example:
    >>> with ContextManagerCaptureOutput() as cmco:
    ...     print("hey")
    ...     assert cmco.get_output() == "hey"
    """
    def __init__(self) -> None:
        ...
    
    def __enter__(self) -> ContextManagerCaptureOutput:
        ...
    
    def __exit__(self, *exc: Any) -> Literal[False]:
        ...
    
    def get_output(self, eval_bytes: bool = ...) -> str:
        ...
    


def do_graph(graph: str, prog: Optional[str] = ..., format: Optional[str] = ..., target: Optional[Union[IO[bytes], str]] = ..., type: Optional[str] = ..., string: Optional[bool] = ..., options: Optional[List[str]] = ...) -> Optional[str]:
    """Processes graph description using an external software.
    This method is used to convert a graphviz format to an image.

    :param graph: GraphViz graph description
    :param prog: which graphviz program to use
    :param format: output type (svg, ps, gif, jpg, etc.), passed to dot's "-T"
        option
    :param string: if not None, simply return the graph string
    :param target: filename or redirect. Defaults pipe to Imagemagick's
        display program
    :param options: options to be passed to prog
    """
    ...

_TEX_TR = ...
def tex_escape(x: str) -> str:
    ...

def colgen(*lstcol: Any, **kargs: Any) -> Iterator[Any]:
    """Returns a generator that mixes provided quantities forever
    trans: a function to convert the three arguments into a color. lambda x,y,z:(x,y,z) by default"""
    ...

def incremental_label(label: str = ..., start: int = ...) -> Iterator[str]:
    ...

def binrepr(val: int) -> str:
    ...

def long_converter(s: str) -> int:
    ...

class EnumElement:
    def __init__(self, key: str, value: int) -> None:
        ...
    
    def __repr__(self) -> str:
        ...
    
    def __getattr__(self, attr: str) -> Any:
        ...
    
    def __str__(self) -> str:
        ...
    
    def __bytes__(self) -> bytes:
        ...
    
    def __hash__(self) -> int:
        ...
    
    def __int__(self) -> int:
        ...
    
    def __eq__(self, other: Any) -> bool:
        ...
    
    def __neq__(self, other: Any) -> bool:
        ...
    


class Enum_metaclass(type):
    element_class = EnumElement
    def __new__(cls: Any, name: str, bases: Any, dct: Dict[str, Any]) -> Any:
        ...
    
    def __getitem__(self, attr: int) -> Any:
        ...
    
    def __contains__(self, val: int) -> bool:
        ...
    
    def get(self, attr: str, val: Optional[Any] = ...) -> Any:
        ...
    
    def __repr__(self) -> str:
        ...
    


def export_object(obj: Any) -> None:
    ...

def import_object(obj: Optional[str] = ...) -> Any:
    ...

def save_object(fname: str, obj: Any) -> None:
    """Pickle a Python object"""
    ...

def load_object(fname: str) -> Any:
    """unpickle a Python object"""
    ...

@conf.commands.register
def corrupt_bytes(data: str, p: float = ..., n: Optional[int] = ...) -> bytes:
    """
    Corrupt a given percentage (at least one byte) or number of bytes
    from a string
    """
    ...

@conf.commands.register
def corrupt_bits(data: str, p: float = ..., n: Optional[int] = ...) -> bytes:
    """
    Flip a given percentage (at least one bit) or number of bits
    from a string
    """
    ...

@conf.commands.register
def wrpcap(filename: Union[IO[bytes], str], pkt: _PacketIterable, *args: Any, **kargs: Any) -> None:
    """Write a list of packets to a pcap file

    :param filename: the name of the file to write packets to, or an open,
        writable file-like object. The file descriptor will be
        closed at the end of the call, so do not use an object you
        do not want to close (e.g., running wrpcap(sys.stdout, [])
        in interactive mode will crash Scapy).
    :param gz: set to 1 to save a gzipped capture
    :param linktype: force linktype value
    :param endianness: "<" or ">", force endianness
    :param sync: do not bufferize writes to the capture file
    """
    ...

@conf.commands.register
def rdpcap(filename: Union[IO[bytes], str], count: int = ...) -> PacketList:
    """Read a pcap or pcapng file and return a packet list

    :param count: read only <count> packets
    """
    ...

class PcapReader_metaclass(type):
    """Metaclass for (Raw)Pcap(Ng)Readers"""
    def __new__(cls: Any, name: str, bases: Any, dct: Dict[str, Any]) -> Any:
        """The `alternative` class attribute is declared in the PcapNg
        variant, and set here to the Pcap variant.

        """
        ...
    
    def __call__(cls, filename: Union[IO[bytes], str]) -> Any:
        """Creates a cls instance, use the `alternative` if that
        fails.

        """
        ...
    
    @staticmethod
    def open(fname: Union[IO[bytes], str]) -> Tuple[str, _ByteStream, bytes]:
        """Open (if necessary) filename, and read the magic."""
        ...
    


@six.add_metaclass(PcapReader_metaclass)
class RawPcapReader:
    """A stateful pcap reader. Each packet is returned as a string"""
    nonblocking_socket = ...
    PacketMetadata = ...
    def __init__(self, filename: str, fdesc: _ByteStream = ..., magic: bytes = ...) -> None:
        ...
    
    def __iter__(self) -> RawPcapReader:
        ...
    
    def next(self) -> Packet:
        """
        implement the iterator protocol on a set of packets in a pcap file
        """
        ...
    
    __next__ = ...
    def read_packet(self, size: int = ...) -> Packet:
        ...
    
    def dispatch(self, callback: Callable[[Tuple[bytes, RawPcapReader.PacketMetadata]], Any]) -> None:
        """call the specified callback routine for each packet read

        This is just a convenience function for the main loop
        that allows for easy launching of packet processing in a
        thread.
        """
        ...
    
    def read_all(self, count: int = ...) -> PacketList:
        ...
    
    def recv(self, size: int = ...) -> bytes:
        """ Emulate a socket
        """
        ...
    
    def fileno(self) -> int:
        ...
    
    def close(self) -> Optional[Any]:
        ...
    
    def __exit__(self, exc_type: Optional[Any], exc_value: Optional[Any], tracback: Optional[Any]) -> None:
        ...
    
    @staticmethod
    def select(sockets: List[SuperSocket], remain: Optional[float] = ...) -> List[SuperSocket]:
        ...
    


class PcapReader(RawPcapReader, _SuperSocket):
    def __init__(self, filename: str, fdesc: IO[bytes] = ..., magic: bytes = ...) -> None:
        ...
    
    def __enter__(self) -> PcapReader:
        ...
    
    def read_packet(self, size: int = ...) -> Packet:
        ...
    
    def recv(self, size: int = ...) -> Packet:
        ...
    


class RawPcapNgReader(RawPcapReader):
    """A stateful pcapng reader. Each packet is returned as
    bytes.

    """
    alternative: Type[Any] = ...
    PacketMetadata = ...
    def __init__(self, filename: str, fdesc: IO[bytes] = ..., magic: bytes = ...) -> None:
        ...
    


class PcapNgReader(RawPcapNgReader, _SuperSocket):
    alternative = ...
    def __init__(self, filename: str, fdesc: IO[bytes] = ..., magic: bytes = ...) -> None:
        ...
    
    def __enter__(self) -> PcapNgReader:
        ...
    
    def read_packet(self, size: int = ...) -> Packet:
        ...
    
    def recv(self, size: int = ...) -> Packet:
        ...
    


class RawPcapWriter:
    """A stream PCAP writer with more control than wrpcap()"""
    def __init__(self, filename: Union[IO[bytes], str], linktype: Optional[int] = ..., gz: bool = ..., endianness: str = ..., append: bool = ..., sync: bool = ..., nano: bool = ..., snaplen: int = ...) -> None:
        """
        :param filename: the name of the file to write packets to, or an open,
            writable file-like object.
        :param linktype: force linktype to a given value. If None, linktype is
            taken from the first writer packet
        :param gz: compress the capture on the fly
        :param endianness: force an endianness (little:"<", big:">").
            Default is native
        :param append: append packets to the capture file instead of
            truncating it
        :param sync: do not bufferize writes to the capture file
        :param nano: use nanosecond-precision (requires libpcap >= 1.5.0)

        """
        ...
    
    def fileno(self) -> int:
        ...
    
    def write_header(self, pkt: Optional[Union[Packet, bytes]]) -> None:
        ...
    
    def write(self, pkt: Union[_PacketIterable, bytes]) -> None:
        """
        Writes a Packet, a SndRcvList object, or bytes to a pcap file.

        :param pkt: Packet(s) to write (one record for each Packet), or raw
                    bytes to write (as one record).
        :type pkt: iterable[scapy.packet.Packet], scapy.packet.Packet or bytes
        """
        ...
    
    def write_packet(self, packet: Union[bytes, Packet], sec: Optional[int] = ..., usec: Optional[int] = ..., caplen: Optional[int] = ..., wirelen: Optional[int] = ...) -> None:
        ...
    
    def flush(self) -> Optional[Any]:
        ...
    
    def close(self) -> Optional[Any]:
        ...
    
    def __enter__(self) -> RawPcapWriter:
        ...
    
    def __exit__(self, exc_type: Optional[Any], exc_value: Optional[Any], tracback: Optional[Any]) -> None:
        ...
    


class PcapWriter(RawPcapWriter):
    """A stream PCAP writer with more control than wrpcap()"""
    def write_header(self, pkt: Optional[Union[Packet, bytes]]) -> None:
        ...
    
    def write_packet(self, packet: Union[bytes, Packet], sec: Optional[int] = ..., usec: Optional[int] = ..., caplen: Optional[int] = ..., wirelen: Optional[int] = ...) -> None:
        """
        Writes a single packet to the pcap file.

        :param packet: Packet, or bytes for a single packet
        :type packet: scapy.packet.Packet or bytes
        :param sec: time the packet was captured, in seconds since epoch. If
                    not supplied, defaults to now.
        :type sec: int or long
        :param usec: If ``nano=True``, then number of nanoseconds after the
                     second that the packet was captured. If ``nano=False``,
                     then the number of microseconds after the second the
                     packet was captured. If ``sec`` is not specified,
                     this value is ignored.
        :type usec: int or long
        :param caplen: The length of the packet in the capture file. If not
                       specified, uses ``len(raw(packet))``.
        :type caplen: int
        :param wirelen: The length of the packet on the wire. If not
                        specified, tries ``packet.wirelen``, otherwise uses
                        ``caplen``.
        :type wirelen: int
        :return: None
        :rtype: None
        """
        ...
    


@conf.commands.register
def import_hexcap(input_string: Optional[str] = ...) -> bytes:
    """Imports a tcpdump like hexadecimal view

    e.g: exported via hexdump() or tcpdump or wireshark's "export as hex"

    :param input_string: String containing the hexdump input to parse. If None,
        read from standard input.
    """
    ...

@conf.commands.register
def wireshark(pktlist: List[Packet], wait: bool = ..., **kwargs: Any) -> Optional[Any]:
    """
    Runs Wireshark on a list of packets.

    See :func:`tcpdump` for more parameter description.

    Note: this defaults to wait=False, to run Wireshark in the background.
    """
    ...

@conf.commands.register
def tdecode(pktlist: Union[IO[bytes], None, str, _PacketIterable], args: Optional[List[str]] = ..., **kwargs: Any) -> Any:
    """
    Run tshark on a list of packets.

    :param args: If not specified, defaults to ``tshark -V``.

    See :func:`tcpdump` for more parameters.
    """
    ...

@conf.commands.register
def tcpdump(pktlist: Union[IO[bytes], None, str, _PacketIterable] = ..., dump: bool = ..., getfd: bool = ..., args: Optional[List[str]] = ..., flt: Optional[str] = ..., prog: Optional[Any] = ..., getproc: bool = ..., quiet: bool = ..., use_tempfile: Optional[Any] = ..., read_stdin_opts: Optional[Any] = ..., linktype: Optional[Any] = ..., wait: bool = ..., _suppress: bool = ...) -> Any:
    """Run tcpdump or tshark on a list of packets.

    When using ``tcpdump`` on OSX (``prog == conf.prog.tcpdump``), this uses a
    temporary file to store the packets. This works around a bug in Apple's
    version of ``tcpdump``: http://apple.stackexchange.com/questions/152682/

    Otherwise, the packets are passed in stdin.

    This function can be explicitly enabled or disabled with the
    ``use_tempfile`` parameter.

    When using ``wireshark``, it will be called with ``-ki -`` to start
    immediately capturing packets from stdin.

    Otherwise, the command will be run with ``-r -`` (which is correct for
    ``tcpdump`` and ``tshark``).

    This can be overridden with ``read_stdin_opts``. This has no effect when
    ``use_tempfile=True``, or otherwise reading packets from a regular file.

    :param pktlist: a Packet instance, a PacketList instance or a list of
        Packet instances. Can also be a filename (as a string), an open
        file-like object that must be a file format readable by
        tshark (Pcap, PcapNg, etc.) or None (to sniff)
    :param flt: a filter to use with tcpdump
    :param dump:    when set to True, returns a string instead of displaying it.
    :param getfd:   when set to True, returns a file-like object to read data
        from tcpdump or tshark from.
    :param getproc: when set to True, the subprocess.Popen object is returned
    :param args:    arguments (as a list) to pass to tshark (example for tshark:
        args=["-T", "json"]).
    :param prog:    program to use (defaults to tcpdump, will work with tshark)
    :param quiet:   when set to True, the process stderr is discarded
    :param use_tempfile: When set to True, always use a temporary file to store
        packets.
        When set to False, pipe packets through stdin.
        When set to None (default), only use a temporary file with
        ``tcpdump`` on OSX.
    :param read_stdin_opts: When set, a list of arguments needed to capture
        from stdin. Otherwise, attempts to guess.
    :param linktype: A custom DLT value or name, to overwrite the default
        values.
    :param wait: If True (default), waits for the process to terminate before
        returning to Scapy. If False, the process will be detached to the
        background. If dump, getproc or getfd is True, these have the same
        effect as ``wait=False``.

    Examples::

        >>> tcpdump([IP()/TCP(), IP()/UDP()])
        reading from file -, link-type RAW (Raw IP)
        16:46:00.474515 IP 127.0.0.1.20 > 127.0.0.1.80: Flags [S], seq 0, win 8192, length 0  # noqa: E501
        16:46:00.475019 IP 127.0.0.1.53 > 127.0.0.1.53: [|domain]

        >>> tcpdump([IP()/TCP(), IP()/UDP()], prog=conf.prog.tshark)
          1   0.000000    127.0.0.1 -> 127.0.0.1    TCP 40 20->80 [SYN] Seq=0 Win=8192 Len=0  # noqa: E501
          2   0.000459    127.0.0.1 -> 127.0.0.1    UDP 28 53->53 Len=0

    To get a JSON representation of a tshark-parsed PacketList(), one can::

        >>> import json, pprint
        >>> json_data = json.load(tcpdump(IP(src="217.25.178.5",
        ...                                  dst="45.33.32.156"),
        ...                               prog=conf.prog.tshark,
        ...                               args=["-T", "json"],
        ...                               getfd=True))
        >>> pprint.pprint(json_data)
        [{u'_index': u'packets-2016-12-23',
          u'_score': None,
          u'_source': {u'layers': {u'frame': {u'frame.cap_len': u'20',
                                              u'frame.encap_type': u'7',
        [...]
                                              },
                                   u'ip': {u'ip.addr': u'45.33.32.156',
                                           u'ip.checksum': u'0x0000a20d',
        [...]
                                           u'ip.ttl': u'64',
                                           u'ip.version': u'4'},
                                   u'raw': u'Raw packet data'}},
          u'_type': u'pcap_file'}]
        >>> json_data[0]['_source']['layers']['ip']['ip.ttl']
        u'64'
    """
    ...

@conf.commands.register
def hexedit(pktlist: _PacketIterable) -> PacketList:
    """Run hexedit on a list of packets, then return the edited packets."""
    ...

def get_terminal_width() -> Optional[int]:
    """Get terminal width (number of characters) if in a window.

    Notice: this will try several methods in order to
    support as many terminals and OS as possible.
    """
    ...

def pretty_list(rtlst: List[Tuple[Union[str, List[str]], ...]], header: List[Tuple[str, ...]], sortBy: int = ..., borders: bool = ...) -> str:
    """
    Pretty list to fit the terminal, and add header.

    :param rtlst: a list of tuples. each tuple contains a value which can
        be either a string or a list of string.
    :param sortBy: the column id (starting with 0) which whill be used for
        ordering
    :param borders: whether to put borders on the table or not
    """
    ...

def make_table(*args: Any, **kargs: Any) -> Optional[Any]:
    ...

def make_lined_table(*args: Any, **kargs: Any) -> Optional[str]:
    ...

def make_tex_table(*args: Any, **kargs: Any) -> Optional[str]:
    ...

def whois(ip_address: str) -> bytes:
    """Whois client for Python"""
    ...

class PeriodicSenderThread(threading.Thread):
    def __init__(self, sock: Any, pkt: _PacketIterable, interval: float = ...) -> None:
        """ Thread to send packets periodically

        Args:
            sock: socket where packet is sent periodically
            pkt: packet or list of packets to send
            interval: interval between two packets
        """
        ...
    
    def run(self) -> None:
        ...
    
    def stop(self) -> None:
        ...
    


class SingleConversationSocket:
    def __init__(self, o: Any) -> None:
        ...
    
    @property
    def __dict__(self):
        ...
    
    def __getattr__(self, name: str) -> Any:
        ...
    
    def sr1(self, *args: Any, **kargs: Any) -> Any:
        ...
    
    def sr(self, *args: Any, **kargs: Any) -> Any:
        ...
    
    def send(self, x: Packet) -> Any:
        ...
    



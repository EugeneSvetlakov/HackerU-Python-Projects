"""
This type stub file was generated by pyright.
"""

import logging
import scapy.modules.six as six
from scapy.consts import WINDOWS
from logging import LogRecord
from scapy.compat import Any

"""
Logging subsystem and basic exception class.
"""
class Scapy_Exception(Exception):
    ...


class ScapyInvalidPlatformException(Scapy_Exception):
    ...


class ScapyNoDstMacException(Scapy_Exception):
    ...


class ScapyFreqFilter(logging.Filter):
    def __init__(self) -> None:
        ...
    
    def filter(self, record: LogRecord) -> bool:
        ...
    


class ScapyColoredFormatter(logging.Formatter):
    """A subclass of logging.Formatter that handles colors."""
    levels_colored = ...
    def format(self, record: LogRecord) -> str:
        ...
    


if WINDOWS:
    ...
log_scapy = ...
if log_scapy.level == logging.NOTSET:
    ...
_handler = ...
log_runtime = ...
log_interactive = ...
log_loading = ...
if six.PY2:
    ...
def warning(x: str, *args: Any, **kargs: Any) -> None:
    """
    Prints a warning during runtime.
    """
    ...


"""
This type stub file was generated by pyright.
"""

from scapy.compat import Any, Dict, List, Optional, Tuple, Union

"""
Main module for interactive startup.
"""
IGNORED = ...
LAYER_ALIASES = ...
QUOTES = ...
DEFAULT_PRESTART_FILE = ...
DEFAULT_STARTUP_FILE = ...
def load_module(name: str, globals_dict: Optional[Dict[str, Any]] = ..., symb_list: Optional[List[str]] = ...) -> None:
    """Loads a Scapy module to make variables, objects and functions
    available globally.

    """
    ...

def load_layer(name: str, globals_dict: Optional[Dict[str, Any]] = ..., symb_list: Optional[List[str]] = ...) -> None:
    """Loads a Scapy layer module to make variables, objects and functions
    available globally.

    """
    ...

def load_contrib(name: str, globals_dict: Optional[Dict[str, Any]] = ..., symb_list: Optional[List[str]] = ...) -> None:
    """Loads a Scapy contrib module to make variables, objects and
    functions available globally.

    If no contrib module can be found with the given name, try to find
    a layer module, since a contrib module may become a layer module.

    """
    ...

def list_contrib(name: Optional[str] = ..., ret: bool = ..., _debug: bool = ...) -> Optional[List[Dict[str, str]]]:
    """Show the list of all existing contribs.

    :param name: filter to search the contribs
    :param ret: whether the function should return a dict instead of
        printing it
    :returns: None or a dictionary containing the results if ret=True
    """
    ...

def update_ipython_session(session: Dict[str, Any]) -> None:
    """Updates IPython session with a custom one"""
    ...

def save_session(fname: str = ..., session: Optional[Dict[str, Any]] = ..., pickleProto: int = ...) -> None:
    """Save current Scapy session to the file specified in the fname arg.

    params:
     - fname: file to save the scapy session in
     - session: scapy session to use. If None, the console one will be used
     - pickleProto: pickle proto version (default: -1 = latest)"""
    ...

def load_session(fname: Optional[Union[str, None]] = ...) -> None:
    """Load current Scapy session from the file specified in the fname arg.
    This will erase any existing session.

    params:
     - fname: file to load the scapy session from"""
    ...

def update_session(fname: Optional[Union[str, None]] = ...) -> None:
    """Update current Scapy session from the file specified in the fname arg.

    params:
     - fname: file to load the scapy session from"""
    ...

def init_session(session_name: Optional[Union[str, None]], mydict: Optional[Union[Dict[str, Any], None]] = ...) -> Tuple[Dict[str, Any], List[str]]:
    ...

def interact(mydict: Optional[Any] = ..., argv: Optional[Any] = ..., mybanner: Optional[Any] = ..., loglevel: int = ...) -> None:
    """
    Starts Scapy's console.
    """
    ...

if __name__ == "__main__":
    ...
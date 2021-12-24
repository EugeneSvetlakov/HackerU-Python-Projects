"""
This type stub file was generated by pyright.
"""

import scapy.modules.six as six
from scapy.supersocket import SuperSocket
from scapy.consts import WINDOWS

"""
Automata with states, transitions and actions.

TODO:
    - add documentation for ioevent, as_supersocket...
"""
class SelectableObject:
    if WINDOWS:
        def __init__(self) -> None:
            ...
        
        def call_release(self): # -> None:
            ...
        
        def __del__(self): # -> None:
            ...
        
    else:
        def call_release(self): # -> None:
            ...
        
        def close(self): # -> None:
            ...
        
    def check_recv(self): # -> Literal[False]:
        ...
    


def select_objects(inputs, remain):
    """
    Select SelectableObject objects. Same than:
    ``select.select(inputs, [], [], remain)``
    But also works on Windows, only on SelectableObject.

    :param inputs: objects to process
    :param remain: timeout. If 0, return [].
    """
    ...

class ObjectPipe(SelectableObject):
    def __init__(self) -> None:
        ...
    
    def fileno(self): # -> int | None:
        ...
    
    def send(self, obj): # -> None:
        ...
    
    def write(self, obj): # -> None:
        ...
    
    def flush(self): # -> None:
        ...
    
    def check_recv(self): # -> bool:
        ...
    
    def recv(self, n=...): # -> None:
        ...
    
    def read(self, n=...): # -> None:
        ...
    
    def close(self): # -> None:
        ...
    
    def __del__(self): # -> None:
        ...
    
    @staticmethod
    def select(sockets, remain=...): # -> tuple[list[Unknown], None]:
        ...
    


class Message:
    def __init__(self, **args) -> None:
        ...
    
    def __repr__(self): # -> str:
        ...
    


class _instance_state:
    def __init__(self, instance) -> None:
        ...
    
    def __getattr__(self, attr): # -> Any:
        ...
    
    def __call__(self, *args, **kargs):
        ...
    
    def breaks(self):
        ...
    
    def intercepts(self):
        ...
    
    def unbreaks(self):
        ...
    
    def unintercepts(self):
        ...
    


class ATMT:
    STATE = ...
    ACTION = ...
    CONDITION = ...
    RECV = ...
    TIMEOUT = ...
    IOEVENT = ...
    class NewStateRequested(Exception):
        def __init__(self, state_func, automaton, *args, **kargs) -> None:
            ...
        
        def action_parameters(self, *args, **kargs): # -> Self@NewStateRequested:
            ...
        
        def run(self):
            ...
        
        def __repr__(self):
            ...
        
    
    
    @staticmethod
    def state(initial=..., final=..., stop=..., error=...): # -> (f: Unknown, initial: Unknown = initial, final: Unknown = final) -> (self: Unknown, *args: Unknown, **kargs: Unknown) -> NewStateRequested:
        ...
    
    @staticmethod
    def action(cond, prio=...): # -> (f: Unknown, cond: Unknown = cond) -> Unknown:
        ...
    
    @staticmethod
    def condition(state, prio=...): # -> (f: Unknown, state: Unknown = state) -> Unknown:
        ...
    
    @staticmethod
    def receive_condition(state, prio=...): # -> (f: Unknown, state: Unknown = state) -> Unknown:
        ...
    
    @staticmethod
    def ioevent(state, name, prio=..., as_supersocket=...): # -> (f: Unknown, state: Unknown = state) -> Unknown:
        ...
    
    @staticmethod
    def timeout(state, timeout): # -> (f: Unknown, state: Unknown = state, timeout: Unknown = timeout) -> Unknown:
        ...
    


class _ATMT_Command:
    RUN = ...
    NEXT = ...
    FREEZE = ...
    STOP = ...
    FORCESTOP = ...
    END = ...
    EXCEPTION = ...
    SINGLESTEP = ...
    BREAKPOINT = ...
    INTERCEPT = ...
    ACCEPT = ...
    REPLACE = ...
    REJECT = ...


class _ATMT_supersocket(SuperSocket, SelectableObject):
    def __init__(self, name, ioevent, automaton, proto, *args, **kargs) -> None:
        ...
    
    def send(self, s): # -> None:
        ...
    
    def check_recv(self): # -> bool:
        ...
    
    def fileno(self): # -> int | None:
        ...
    
    def recv(self, n=...): # -> None:
        ...
    
    def close(self): # -> None:
        ...
    
    @staticmethod
    def select(sockets, remain=...):
        ...
    


class _ATMT_to_supersocket:
    def __init__(self, name, ioevent, automaton) -> None:
        ...
    
    def __call__(self, proto, *args, **kargs): # -> _ATMT_supersocket:
        ...
    


class Automaton_metaclass(type):
    def __new__(cls, name, bases, dct):
        ...
    
    def build_graph(self): # -> str:
        ...
    
    def graph(self, **kargs):
        ...
    


class Automaton(six.with_metaclass(Automaton_metaclass)):
    def parse_args(self, debug=..., store=..., **kargs): # -> None:
        ...
    
    def master_filter(self, pkt): # -> Literal[True]:
        ...
    
    def my_send(self, pkt): # -> None:
        ...
    
    class _IO_fdwrapper(SelectableObject):
        def __init__(self, rd, wr) -> None:
            ...
        
        def fileno(self): # -> int | None:
            ...
        
        def check_recv(self): # -> bool:
            ...
        
        def read(self, n=...): # -> bytes | None:
            ...
        
        def write(self, msg): # -> int | None:
            ...
        
        def recv(self, n=...): # -> bytes | None:
            ...
        
        def send(self, msg): # -> int | None:
            ...
        
    
    
    class _IO_mixer(SelectableObject):
        def __init__(self, rd, wr) -> None:
            ...
        
        def fileno(self): # -> int:
            ...
        
        def check_recv(self):
            ...
        
        def recv(self, n=...):
            ...
        
        def read(self, n=...):
            ...
        
        def send(self, msg):
            ...
        
        def write(self, msg):
            ...
        
    
    
    class AutomatonException(Exception):
        def __init__(self, msg, state=..., result=...) -> None:
            ...
        
    
    
    class AutomatonError(AutomatonException):
        ...
    
    
    class ErrorState(AutomatonException):
        ...
    
    
    class Stuck(AutomatonException):
        ...
    
    
    class AutomatonStopped(AutomatonException):
        ...
    
    
    class Breakpoint(AutomatonStopped):
        ...
    
    
    class Singlestep(AutomatonStopped):
        ...
    
    
    class InterceptionPoint(AutomatonStopped):
        def __init__(self, msg, state=..., result=..., packet=...) -> None:
            ...
        
    
    
    class CommandMessage(AutomatonException):
        ...
    
    
    def debug(self, lvl, msg): # -> None:
        ...
    
    def send(self, pkt): # -> None:
        ...
    
    def __init__(self, *args, **kargs) -> None:
        ...
    
    def __iter__(self): # -> Self@Automaton:
        ...
    
    def __del__(self): # -> None:
        ...
    
    def __repr__(self): # -> str:
        ...
    
    def add_interception_points(self, *ipts): # -> None:
        ...
    
    def remove_interception_points(self, *ipts): # -> None:
        ...
    
    def add_breakpoints(self, *bps): # -> None:
        ...
    
    def remove_breakpoints(self, *bps): # -> None:
        ...
    
    def start(self, *args, **kargs): # -> None:
        ...
    
    def run(self, resume=..., wait=...):
        ...
    
    def runbg(self, resume=..., wait=...): # -> None:
        ...
    
    def next(self): # -> None:
        ...
    
    __next__ = ...
    def stop(self): # -> None:
        ...
    
    def forcestop(self): # -> None:
        ...
    
    def restart(self, *args, **kargs): # -> None:
        ...
    
    def accept_packet(self, pkt=..., wait=...): # -> None:
        ...
    
    def reject_packet(self, wait=...): # -> None:
        ...
    


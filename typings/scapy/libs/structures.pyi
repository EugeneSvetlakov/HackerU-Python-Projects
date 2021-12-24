"""
This type stub file was generated by pyright.
"""

import ctypes

"""
Commonly used structures shared across Scapy
"""
class bpf_insn(ctypes.Structure):
    """"The BPF instruction data structure"""
    _fields_ = ...


class bpf_program(ctypes.Structure):
    """"Structure for BIOCSETF"""
    _fields_ = ...


class sock_fprog(ctypes.Structure):
    """"Structure for SO_ATTACH_FILTER"""
    _fields_ = ...



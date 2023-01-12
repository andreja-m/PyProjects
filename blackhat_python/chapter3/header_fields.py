from ctypes import *
import socket
import struct

class IP(Structure):
    _fields_ = [
        ("ihl",         c_ubyte,    4),     # 4 bit unsinged char   - version
        ("version",     c_ubyte,    4),     # 4 bit unsinged char   - Header Length
        ("tos",         c_ubyte,    8),     # 1 byte char           - Type of Service
        ("len",         c_ushort,  16),     # 2 byte                - Total lenght
        ("id",          c_ushort,  16),     # 2 byte                - Identification
        ("offset",      c_ushort,  16),     # 2 byte                - Flags/Fragment Offset
        ("ttl",         c_ubyte,    8),     # 1 byte char           - Time to Live
        ("protocol_num",c_ubyte,    8),     # 1 byte char           - Protocol
        ("sum",         c_ushort,  16),     # 2 byte unsinged short - Header cheksum
        ("src",         c_unit32,  32),     # 4 byte unsinged int   - Source IP Address
        ("dst",         c_unit32,  32),     # 4 byte unsinged int   - Destination IP Address
    ]
    def __new__(cls, socket_buffer=None):
        return cls.from_buffer_copy(socket_buffer)
    def __init__(self, socket_buffer=None):
        # human readable IP addresses
        self.src_address = socket.inet_ntoa(struct.pack("<L", self.src))
        self.dst_address = socket.inet_ntoa(struct.pack("<L", self.dst))

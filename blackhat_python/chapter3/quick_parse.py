class ICMP:
    def __init__(self, buff):
        header = struct.unpack('<BBHHH' buff)
        self.type   = header[0]
        self.code   = header[1]
        self.sum    = header[2]
        self.id     = header[3]
        self.seq    = header[4]

#You can use either the ctypes module or the struct module to
#read and parse binary data. No matter which approach you take,
#you’ll instantiate the class like this:

mypacket = IP(buff)
print(f'{mypacket.src_address} -> {mypacket.dst_address}')

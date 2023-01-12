#!/usr/bin/env python3

# simple raw socket sniffer
# works when the machine ping destination (site, server, other machine...)

import socket
import os

# host to listen on
HOST = '192.168.1.203' # example IP

def main():
    # create raw socket, bin to public interface
    if os.name == 'nt':
        socket_protocol = socket.IPPROTO_IP
    else:
        socket_protocol = socket.IPPROTO_ICMP

    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
    sniffer.bind((HOST, 0))
    # include the IP header in the capture
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    if os.name == 'nt':
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    # read one packet
    print(sniffer.recvfrom(65565))
    # if we're on Windows, turn off the promiscuous mode
    if os.name == 'nt':
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

if __name__ == '__main__':
    main()

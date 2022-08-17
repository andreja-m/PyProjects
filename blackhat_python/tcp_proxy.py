import sys
import socket
import threading

HEX_FILTER = ''.join(
	[(len(repr(chr(i))) == 3) and chr(i) or '.' for i in range(256)])

def hexdump(src, lenght = 16, show = True):
	if isinstance(src, bytes):
		src = src.decode()

	results = list()
	for i in range(0, len(src), lenght):
		word = str(src[i:i+lenght])

		printable = word.translate(HEX_FILTER)
		hexa = ' '.join([f'{ord(c):02X}' for c in word])
		hexwidth = length*3
		results.append(f'{i:04x} {hexa:{hexwidth}} {printable}')
	if show:
		for line in results:
			print(line)
	else:
		return results

def receive_from(connection):
	buffer = b""

	# By default, we set a five-second timeout, which
	# might be aggressive if you’re proxying traffic 
	# to other countries or over lossy networks, 
	# so increase the timeout as necessary
	
	connection.settimeout(5)
	try:
		while True:
			data = connection.recv(4096)
			if not data:
				break
			buffer += data
		except Exception as e:
			pass
		return buffer

def request_handler(buffer):
	# perform packet modifications
	return buffer

def response_handler(buffer):
	# perform packet modifications]
	return buffer
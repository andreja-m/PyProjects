import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Welcome to basic Port Scanner.')
target = input('[+] Insert ip address: ')

def pscan(port):
    try:
        con = s.connect((target,port))
        return True
    except:
        return False

for x in range(65535):
    if pscan(x):
        print(f'[+] Port {x} is open')

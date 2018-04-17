PORT = 50000
MAGIC = "fna349fn"

from socket import socket, AF_INET, SOCK_DGRAM

s = socket(AF_INET, SOCK_DGRAM) #create UDP socket
s.bind(('', PORT))

while 1:
    data, addr = s.recvfrom(1024) #wait for a packet
    data = data.decode()
    if data.startswith(MAGIC):
        server_ip = data[len(MAGIC):]
        print("got service announcement from", server_ip)

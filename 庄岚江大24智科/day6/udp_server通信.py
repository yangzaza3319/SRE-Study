import socket
udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp_socket.bind(("127.0.0.1",8000))
msg,addr = udp_socket.recvfrom(1024)
print(addr,":",msg.decode('utf-8'))
udp_socket.sendto(msg.upper(),addr)
udp_socket.close()
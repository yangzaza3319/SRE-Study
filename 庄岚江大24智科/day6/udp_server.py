import socket
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(("0.0.0.0",8090))
#收发消息调用sendto(),recvfrom()
data,client_address= server.recvfrom(1024)
server.sendto(data.upper(),client_address)
server.close()
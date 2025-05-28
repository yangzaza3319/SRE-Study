import socket
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

client.sendto("hello world".encode("utf-8"),("127.0.0.1",8090))
#收发消息调用sendto(),recvfrom()
data,addr = client.recvfrom(1024)
print(data.decode("utf-8"))
client.close()

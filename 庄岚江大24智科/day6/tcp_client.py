#tcp_client客户端
import socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#连接服务端
client.connect(("127.0.0.1",8070))
while True:
    # 发送数据:一定要将数据编码->bytes
    smsg = input(">>>>>")
    if smsg == "exit":
        break
    client.send(smsg.encode("utf-8"))
    data = client.recv(1024)
    print(data.decode("utf-8"))

client.close()
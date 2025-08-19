import socket
ip_port = ('127.0.0.1', 8080)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    msg = input('请输入时间格式(默认%Y %m %d)>>: ').strip()
    s.sendto(msg.encode('utf-8'), ip_port)
    data, addr = s.recvfrom(1024)
    print("当前时间：", data.decode())
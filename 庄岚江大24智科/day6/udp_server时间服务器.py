import socket
import time
ip_port = ('127.0.0.1',8080)
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(ip_port)
while True:
    msg,addr = s.recvfrom(1024)
    stru_time = time.localtime()
    if not msg:
        time_fmt = '%Y-%m-%d '
    else:
        time_fmt = msg.decode('utf-8')
    back_msg = time.strftime(time_fmt,stru_time)
    s.sendto(back_msg.encode('utf-8'),addr)
s.close()
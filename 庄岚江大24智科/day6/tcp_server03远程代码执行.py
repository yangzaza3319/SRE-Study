import socket
import subprocess
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.bind(('127.0.0.1',8080))
phone.listen(5)
while True:
    conn,client_addr = phone.accept()
    print("客户端已连接")
    while True:
        try:
            cmd = conn.recv(1024)
            ret = subprocess.Popen(cmd.decode('utf-8'),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            correct_msg = ret.stdout.read()
            error_msg = ret.stderr.read()
            conn.send(correct_msg+error_msg)
        except ConnectionResetError:
            break
conn.close()
phone.close()
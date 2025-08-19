import socket
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.connect(('127.0.0.1',8080))
while True:
    client_data = input('>>>>')
    phone.send(client_data.encode('utf-8'))
    if client_data == 'exit':
        break
    from_server_data = phone.recv(1024)
    print(from_server_data.decode('gbk'))
phone.close()
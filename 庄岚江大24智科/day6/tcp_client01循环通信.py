import socket
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.connect(('127.0.0.1',9999))
while True:
    client_data = input('>>>>')
    phone.send(client_data.encode('utf-8'))
    from_server_data = phone.recv(1024)
    print(from_server_data.decode('utf-8'))
phone.close()
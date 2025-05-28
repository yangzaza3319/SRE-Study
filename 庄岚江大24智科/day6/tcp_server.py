import socket
#创建socket对象
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定地址和端口 0.0.0.0代表所有，8070代表监听本地
server.bind(("0.0.0.0",8070))
# 监听：最大连接数
server.listen(5)


try:
    while True:
        # 阻塞接受客户端请求，返回socket_object、address_info(客户端地址)

        conn, client_address = server.accept()
        print(conn, client_address)
        while True:
            data = conn.recv(1024)
            msg = data.decode("utf-8")
            print(msg)
            if  msg == "exit":
                print("已退出")
                break
            f_msg = msg + "EaglesLab"
            conn.send(f_msg.encode("utf-8"))
except ConnectionError  as e:
    print(f"{e}")
finally:
    #关闭连接
    conn.close()
    #关闭服务端
    server.close()
"""
SDK 的工作流程

TCP（传输控制协议）
可靠的、面向连接的协议（如：通话）、传输效率低的全双工通信（发送硬盘&接收硬盘）、
面向字节流。使用TCP的应用：Web浏览器；文件传输程序。
UDP（用户数据报协议）

不可靠、无连接的服务，传输效率高（发送前时延小），一对一、一对多、多对一、多对多、
面向报文（数据包），尽最大努力服务，无控制控制。使用UDP的应用：域名系统（DNS）；
视频流；IP语音（VoIP）。
"""
socket_family 可以是 AF_UNIX 或 AF_INET。
socket_type 可以是 SOCK_STREAM(TCP) 或 SOCK_DGRAM(UDP)。
#tcp_server服务端
"""
AdressFamily:
    AF_INET:ipv4
    AF_UNIX:unix socket
    AF_INET6:ipv6
SocketKind:
    SOCK_STREAM: TCP
    SOCK_DGRAM: UDP
    SOCK_RAW: xxx
"""

TCP协议
服务端：

服务器端先初始化socket对象
绑定监听的IP和端口
调用accept进行阻塞，等待客户端建立连接
如果有客户端连接上来，获取对方的信息，以及简历TCP连接对象
通过连接对象以及recv()、send()方法接收和回复客户端的信息
信息传输完成以后，通过close()终止TCP连接
客户：

同样先初始化socket对象
指定服务端的IP和端口号信息
通过connect来与服务端建立TCP连接
通过send()向服务端发送信息
通过recv()接收服务端发过来的信息
信息传输完成以后，通过close()终止TCP连接


UDP协议（不可靠）
服务端：

初始化Socket，并绑定端口和IP地址
直接通过recvfrom()来等待接收消息，消耗建立连接
通过send()回复消息
关闭套接字
客户：

相同的初始化Sket
指定服务端的端口和IP地址
通过sendto()给服务端发消息，由于没有建立连接，所以发消息的时候要带上对方的地址
通过recvfrom()来等待接收消息
关闭套接字










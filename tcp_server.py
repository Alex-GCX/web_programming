import socket


def client_server(client_socket):
    while True:
        # 接收数据
        recv_data = client_socket.recv(1024)
        if not recv_data:
            # 关闭服务套接字
            client_socket.close()
            break
        print('接收的数据为:', recv_data.decode('utf-8'))
        # 返回数据
        client_socket.send('已接收'.encode('utf-8'))


def main():
    # tcp创建套接字
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定端口
    local_addr = ('', 7890)
    tcp_server.bind(local_addr)
    # 使用listen将其变为被动
    tcp_server.listen(128)
    while True:
        print('准备接收连接.....')
        # 等待客户端连接，若有新客户端连接，返回一个新的套接字专门服务这个客户端
        client_socket, client_addr = tcp_server.accept()
        print('接收到连接,IP:%s PORT:%s' % (client_addr[0], client_addr[1]))
        client_server(client_socket)

    # 关闭监听的套接字
    tcp_server.close()
if __name__ == '__main__':
    main()

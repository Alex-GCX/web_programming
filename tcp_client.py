import socket


def main():
    # 创建套接字
    tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置服务器地址
    server_addr = ('47.114.184.141', 7890)
    # 创建连接
    tcp_client.connect(server_addr)
    while True:
        # 获取发送的数据
        send_data = input('请输入发送的数据(exit退出)：\n')
        if send_data == 'exit':
            break
        tcp_client.send(send_data.encode('utf-8'))
        # 接收服务端返回的数据
        recv_data = tcp_client.recv(1024)
        print('返回数据为:\n', recv_data.decode('utf-8'))
    tcp_client.close()


if __name__ == '__main__':
    main()

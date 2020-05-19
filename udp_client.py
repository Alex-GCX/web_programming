import socket


def main():
    # 创建套接字
    udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 设置服务器地址
    server_addr = ('localhost', 7788)
    while True:
        # 获取要发送的内容
        send_data = input('\n请输入要发送的内容(exit退出)：')
        if send_data == 'exit':
            break
        # 发送数据
        udp_client.sendto(send_data.encode('utf-8'), server_addr)
    # 关闭套接字
    udp_client.close()


if __name__ == '__main__':
    main()

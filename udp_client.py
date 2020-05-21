import socket


def main():
    # 创建套接字
    udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 设置服务器地址
    server_addr = ('172.16.193.86', 7788)
    while True:
        # 获取要发送的内容
        send_data = input('请输入要发送的内容(exit退出)：\n')
        if send_data == 'exit':
            break
        # 发送数据
        udp_client.sendto(send_data.encode('utf-8'), server_addr)
        print('准备接收数据。。。')
        # 接收数据
        recv_data = udp_client.recvfrom(1024)
        print('接收的数据为：\n', recv_data[0].decode('utf-8'))
    # 关闭套接字
    udp_client.close()


if __name__ == '__main__':
    main()

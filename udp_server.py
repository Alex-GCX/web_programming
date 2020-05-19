import socket

def main():
    '''udp服务器'''
    # 创建套接字
    udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定端口
    local_addr = ('', 7788) # ip地址不写表示本机IP
    udp_server.bind(local_addr)

    while True:
        # 接收数据
        print('准备接收数据。。。。')
        recv_data = udp_server.recvfrom(1024) # 1024表示本次接收的最大字节数
        if not recv_data:
            break
        # 打印数据
        print(recv_data[0].decode('utf-8'))
        # 客户端的ip和端口
        client_addr = recv_data[1]
        # 获取发送的数据
        send_data = input('请输入发送的数据\n')
        # 发送数据
        udp_server.sendto(send_data.encode('utf-8'), client_addr)


    # 关闭套接字
    udp_server.close()

if __name__ == '__main__':
    main()

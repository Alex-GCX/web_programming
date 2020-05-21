import socket

def downloader(client_socket):
    while True:
        # 接收客户端数据
        print('----等待需要下载的文件----')
        file_name = client_socket.recv(1024).decode('utf-8')
        print('客户端需要下载的文件名为：', file_name)
        if not file_name:
            client_socket.close()
            break
        # 打开文件
        try:
            file = open(file_name, 'rb')
            content = file.read()
            file.close()
        except Exception as e:
            content = '404'.encode('utf-8')
        print('---发送文件----')
        # 发送数据
        client_socket.send(content)

def main():
    # 创建套接字
    main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定ip和端口
    local_addr = ('', 7801)
    main_socket.bind(local_addr)
    # 设置监听状态
    main_socket.listen(128)
    while True:
        # 等待客户端连接
        print('----等待新客户端连接----')
        client_socket, client_addr = main_socket.accept()
        print('连接到客户端：', client_addr)
        downloader(client_socket)


if __name__ == '__main__':
    main()

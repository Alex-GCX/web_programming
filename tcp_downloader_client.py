import socket


def main():
    # 创建套接字
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置服务器地址
    server_addr = ('47.114.184.141', 7801)
    # 创建连接
    client_socket.connect(server_addr)
    while True:
        # 获取需要下载的文件名
        file_name = input('请输入想下载的文件名(exit退出)\n')
        if file_name == 'exit':
            break
        # 发送数据
        client_socket.send(file_name.encode('utf-8'))
        # 获取返回的文件
        content = client_socket.recv(1024)
        print('返回数据为：\n', content)
        if content.decode('utf-8') == '404':
            # 返回值为空
            print('文件在服务器中不存在！请重新输入')
            continue
        # 返回值不为空，则创建文件，将返回值写入文件中
        with open(file_name + '2', 'wb') as file:
            file.write(content)
        print('文件下载完成，请输入下一个文件名')
    # 关闭套接字
    client_socket.close()


if __name__ == '__main__':
    main()

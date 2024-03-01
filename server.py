import socket

imgcounter = 1
basename = "image%s.png"

Host = '0.0.0.0'
PORT = 12345


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((Host, PORT))
server_socket.listen(5)

client_socket, (client_ip, client_port) = server_socket.accept()

while True:
    myfile = open(basename % imgcounter, 'wb')

    data = server_socket.recv(40960000)
    if not data:
        myfile.close()
        break
    myfile.write(data)
    myfile.close()
    ''' command = input(">")
    client_socket.send(command)

    if command=="q":
        break
    data = client_socket.recv(1024)
    print(data) '''

client_socket.close()
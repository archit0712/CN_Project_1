import socket

if __name__ == "__main__":
    ip = "localhost"
    port = 5001
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(1)
    print('Server is ready for connections')
    while True:
        client, address = server.accept()
        print(f"Connection Established - {address[0]}:{address[1]}")
        try :
            data = client.recv(1024)
            command = data.decode('utf-8')
            cmd = command.split()
            if cmd[0] == 'get':
                file = open(cmd[1], 'rb')
                line = file.read(1024)
                while(line):
                    client.send(line)
                    line = file.read(1024)
                file.close()
                print("File Transfer Successful!") 
            elif cmd[0] == 'upload': 
                file = open('new'+cmd[1], 'wb')
                line = client.recv(1024)

                while(line):
                    file.write(line)
                    line = client.recv(1024)
                file.close()
                print("Uploaded file received!")
            elif cmd[0] == 'exit':
                print('Connection Close')
                client.close()
                break
            else : 
                print('Invalid Command')
                client.send('Invalid Command Please try again!'.encode("utf-8"))
                client.close()
                break
            client.close()
        except:
            client.close()
            print("Some Error Occured! Please Check Command!")
        else :
            continue

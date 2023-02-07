import socket

if __name__ == "__main__":
    connection_string = None
    while True:
        try:
            ip= "localhost"
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if connection_string is None :
                connection_string = input("Enter Command and port number to connect:")
            data = connection_string.split()
            port = int(data[1])
            server.connect((ip,port))
            print('to terminate the program enter "exit" ')
            print('to download enter get <filename>')
            print('for uploading enter upload <filename>')
        except :
            print("Please try again with correct port or command!")
        else : 
            data = input("Enter command:")
            command = data.split()

            if command[0] == 'get':
                print('requesting ' + command[1]+ ' from server...')
                server.send(data.encode('utf-8'))
                file = open('new'+command[1], 'wb')
                line = server.recv(1024)
                while(line):
                    file.write(line)
                    line = server.recv(1024)
                file.close()
                print("File received !")
            elif command[0] == 'upload' :
                print('sending '+ command[1]+' to server...')
                server.send(data.encode('utf-8'))
                file = open( command[1], 'rb')
                line = file.read(1024)
                while(line):
                    server.send(line)
                    line = file.read(1024)
                file.close()
                print('File Uploaded!')
            elif data == 'exit' :
                server.send(data.encode('utf-8'))
                print("Program Terminated!")
                server.close()
                break
            else :
                print("Invalid Command!")
                server.close()
            server.close()
    

        

        
    
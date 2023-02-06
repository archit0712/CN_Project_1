import socket

if __name__ == "__main__":
        
        try:
            ip= "localhost"
            port = 5001

            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   
            cmd = input("Enter Command and port number to connect:")
            data = cmd.split()
            print(data)
            port = int(data[1])
            server.connect((ip,port))
            print("Connection Successful!")
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
            else :
                print("Invalid Command!")
                server.close()
    

        

        
    
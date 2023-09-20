import sys
from socket import *


def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  
  #Prepare a server socket
  serverSocket.bind(("", port))
  #Fill in start
  serverSocket.listen()
  #Fill in end

  while True:
    print('Ready to serve...')
    #Fill in start -are you accepting connections? #Fill in end

    connectionSocket, addr = serverSocket.accept() #this is  client
    print(f"Connection established from {addr}"+"\n\n\n\n\n")     #Establish the connection
    
    try:
      message = connectionSocket.recv(1024).decode()# recieve the http get
      print("Client Mssg:\n", message)
      filename = message.split()[1] # pull the filename off of the http get
      print(filename, "found")

      # opens the client requested file.
      # Plenty of guidance online on how to open and read a file in python. How should you read it though if you plan on sending it through a socket?
      f = open(filename[1:], 'rb') #maybe 'rb'?
      print(f.read())


      # Fill in start using one send for header and contents of file as one variable
      # connectionSocket.sendall(HeaderMssgSend + message.encode())
      outputdataHeader = b"HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=UTF-8\r\nServer: <localhost:13331>\r\nConection: keep-alive\r\n\r\n"
      #connectionSocket.send(outputdataHeader)

      # for i in f:
      #   connectionSocket.send(i)

      
      SendPackage = f.read()
      outputdataHeader += SendPackage

      connectionSocket.send(outputdataHeader)
      connectionSocket.close()  # closing the connection socket
      print(filename, "Delivered \n\n\n")

    except Exception as e: # if file requested that we do not have, go here
    # Send response message for invalid request due to the file not being found (404) Remember the format you used in the try: block!
    # Fill in start
      print(e)
      print(filename + "\tNOT Found")
      error_mssg = b"HTTP/1.1 404 Not Found\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n"
      connectionSocket.send(error_mssg)
    # Fill in end
      connectionSocket.close()

    # Commenting out the below, as its technically not required and some students have moved it erroneously in the While loop. DO NOT DO THAT OR YOURE GONNA HAVE A BAD TIME.
    # serverSocket.close()
    #sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)
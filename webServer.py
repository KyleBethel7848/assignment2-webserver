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
    #Establish the connection
    
    print('Ready to serve...')      #makes it too here
    #Fill in start -are you accepting connections?     #Fill in end
    connectionSocket, addr = serverSocket.accept()
    
    try: # how are http get sent and recieved between client/server
      message = connectionSocket.recv(1024) # recieve the http get
      print("Client Mssg:\n", message)#Fill in start -a client is sending you a message   #Fill in end
      filename = message.split()[1] # pull the filename off of the http get

      # opens the client requested file.
      # Plenty of guidance online on how to open and read a file in python. How should you read it though if you plan on sending it through a socket?
      f = open(filename[1:], "r")
      # fill in end

      outputdata = b"Content-Type: text/html; charset=UTF-8\r\n"  #need to adjust this

      # Fill in start -This variable can store your headers you want to send for any valid or invalid request.
      # Content-Type above is an example on how to send a header as bytes. There are more!
      # Fill in end




      # Send an HTTP header line into socket for a valid request. What header should be sent for a response that is ok?
      # Note that a complete header must end with a blank line, creating the four-byte sequence "\r\n\r\n" Refer to https://w3.cs.jmu.edu/kirkpams/OpenCSF/Books/csf/html/TCPSockets.html
      # Fill in start
      mssgSend = "HTTP/1.1 200 OK\r\n\r\n"
      connectionSocket.send(mssgSend.encode('utf-8'))
      # Fill in end

      # Send the content of the requested file to the client
      for i in f:  # for line in file # Fill in start - send your html file contents
        contents = f.read(i)
      connectionSocket.send(contents)
      # #Fill in end
      connectionSocket.close()  # closing the connection socket

    except Exception as e: # if file requested that we do not have, go here
    # Send response message for invalid request due to the file not being found (404) Remember the format you used in the try: block!
    # Fill in start
      sendMssg = "404 Not Found KB"
      connectionSocket.sendall(sendMssg.encode('utf-8'))
      print("Sent 404")
    # Fill in end

    # Close client socket
    # Fill in start
    connectionSocket.close()
    print("Closing file")
    # Fill in end

    exit()
    print("Exiting Server")


    # Commenting out the below, as its technically not required and some students have moved it erroneously in the While loop. DO NOT DO THAT OR YOURE GONNA HAVE A BAD TIME.
    # serverSocket.close()
    # sys.exit()  # Terminate the program after sending the corresponding data
if __name__ == "__main__":
  webServer(13331)
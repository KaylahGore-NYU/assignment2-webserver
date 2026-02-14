# import socket module
from socket import *
# In order to terminate the program
import sys



def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  
  #Prepare a server socket
  serverSocket.bind(("", port)) #serverSocket.bind(("", port))
  serverSocket.listen(1)
  print(f"Server available on {port}.") 
  while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() #Fill in start -are you accepting connections?     #Fill in end
    
    try:
      message = connectionSocket.recv(1024).decode() #Fill in start -a client is sending you a message   #Fill in end 
      filename = message.split()[1]
      

      f = open(filename[1:], "rb")   #fill in start              #fill in end   )
      
      

      #This variable can store the headers you want to send for any valid or invalid request.   What header should be sent for a response that is ok?    
      #Fill in start 

      outputdata = b"HTTP/1.1 200 OK\r\n"
      outputdata += b"Content-Type: text/html; charset=UTF-8\r\n"
      outputdata += b"Server: SimpleHTTP/1.1\r\n"
      outputdata += b"Connection: close\r\n"
      outputdata += b"\r\n"


      #Note that a complete header must end with a blank line, creating the four-byte sequence "\r\n\r\n" Refer to https://w3.cs.jmu.edu/kirkpams/OpenCSF/Books/csf/html/TCPSockets.html
 
      #Fill in end
               
      for i in f: #for line in file
        output += i

      connectionSocket.send(outputdata)
      connectionSocket.close() #closing the connection socket
      
    except Exception as e:
      response = b"HTTP/1.1 404 Not Found\r\n"
      response += b"Content-Type: text/html; charset=UTF-8\r\n"
      response += b"\r\n"
      response += b"<html><body><h1> 404 not found</h1></body></html>"
      connectionSocket.send(response)
      connectionSocket.close()

if __name__ == "__main__":
  webServer(13331)









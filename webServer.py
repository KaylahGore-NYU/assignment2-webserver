# import socket module
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

  
  serverSocket.bind(("", port)) #serverSocket.bind(("", port))
  serverSocket.listen(1)
  print(f"Server available on {port}.") 
  while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() #Fill in start -are you accepting connections?     #Fill in end
    
    try:
      message = connectionSocket.recv(1024).decode() #Fill in start -a client is sending you a message   #Fill in end 
      filename = message.split()[1]
      f = open(filename[1:], "rb")
      
      outputdata = b"HTTP/1.1 200 OK\r\n"
      outputdata += b"Content-Type: text/html; charset=UTF-8\r\n"
      outputdata += b"Server: SimpleHTTP/1.1\r\n"
      outputdata += b"Connection: close\r\n"
      outputdata += b"\r\n"

               
      for i in f: 
        output += i

      connectionSocket.send(outputdata)
      connectionSocket.close() #closing the connection socket
      
    except Exception as e:
      response = b"HTTP/1.1 404 Not Found\r\n"
      response += b"Content-Type: text/html; charset=UTF-8\r\n"
      response += b"Server: SimpleHTTP/1.1\r\n"
      response += b"\r\n"
      response += b"<html><body><h1> 404 not found</h1></body></html>"
      connectionSocket.send(response)
      connectionSocket.close()

if __name__ == "__main__":
  webServer(13331)













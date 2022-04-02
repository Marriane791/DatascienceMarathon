import socket
#create a socket object with the parameters socket_domain,type,protocal 
s = socket.socket ()
#get local machine name
host = socket.gethostname()
#reserve a port for your service
port = 12345
# use the server method to bind host name and port to the server
s.connect((host,port))
print(s.recv(1024))
s.close()
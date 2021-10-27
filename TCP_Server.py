import socket
import threading

#================
# ip dan portnya
#================

host = '127.0.0.1'
port = 60300

# AF -> Adress Family
# AF_INET Buat IPv4
# AF_INET6 buat IPv6
# SOCK_STREAM buat TCP
# SOCK_DGRAM buat UDP
# kalo socket.socket() ga di isi defaultnya pake IPv4 dan TCP

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

client, address = server.accept()

#print (client, address)

msg =  "|     helo client!     |"

client.send(msg.encode("utf-8"))

def read(client: socket.socket):
    while True:
        message = client.recv(1024).decode("utf-8")
        
        if message == "exit":
            client.close()
            return            
        else:
            print ('client>>',message)
       
def write(client: socket.socket):
    while True:
        message = str(input(""))
        
        if message == "exit":      
            client.close()
            return
        else:
            client.send(message.encode("utf-8"))

print ()
print ("============================")
print ("|  Server is Listening...  |")
print ("============================")
print ()
           
readThread = threading.Thread(target=read, args=(client, ))
readThread.start()

writeThread = threading.Thread(target=write, args=(client, ))
writeThread.start()


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

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

print ("========================")
print (client.recv(1024).decode("utf-8"))
print ("========================")
print ()

def read(client: socket.socket):
    while True:
        message = client.recv(1024).decode("utf-8")
        
        if message == "exit":
            client.close()
            return            
        else:
            print ('server>>',message)
       
def write(client: socket.socket):
    while True:
        message = str(input(""))
        
        if message == "exit":      
            client.close()
            return
        else:
            client.send(message.encode("utf-8"))
            
readThread = threading.Thread(target=read, args=(client, ))
readThread.start()
#readThread.join()

writeThread = threading.Thread(target=write, args=(client, ))
writeThread.start()
#writeThread.join()
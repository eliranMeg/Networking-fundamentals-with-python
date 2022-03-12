import socket 

target_host ='0.0.0.0'
target_port = 9999

# AF_INET     -->  tell that we going to use IPv4 address.
# SOCK_STREAM -->  tell that this will be a TCP client.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("# Create a socket object.") 


client.connect((target_host, target_port))
print("# Connect the client")

client.sendall("Hiii I am the client")
print("# Send data")


response = client.recv(4096)
print("# Receive data")

print(response)


# for simplicity's sake:
# In this code I assume that the connection will always succeed
# and the server is always expecting us to send data first.
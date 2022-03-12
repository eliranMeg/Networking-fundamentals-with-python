import socket

target_host = '127.0.0.1'
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("# Create a socket object")

client.sendto("AAABBBCCC",(target_host, target_port))
print("# Send some data")

data, addr = client.recvfrom(4096)
print(data)


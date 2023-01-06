import socket, datetime, os

file_out = open('in_data.pkl','rb')
file_return = open('return_data.pkl','wb')

HOST = ''
PORT = 9092
s_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
s_.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s_.bind((HOST, PORT))
s_.listen(10)

s = socket.socket()
host = "192.168.2.99"  # FPGA IP
port = 9091  # Shared port
s.connect((host, port))

times = datetime.datetime.now()

bytes_ = file_out.read(2048)
while (bytes_):
    s.send(bytes_)
    bytes_ = file_out.read(2048)
    break
file_out.close()
s.shutdown(socket.SHUT_WR)

while True:
    c, addr = s_.accept()
    print ('Connected to ', addr)
    bytes_ = c.recv(2048)
    while (bytes_):
        file_return.write(bytes_)
        bytes_ = c.recv(2048)
    file_return.close()
    c.close()
    break
    
s_.close()
s.close()

timee = datetime.datetime.now()
time = timee - times
print(time.microseconds)
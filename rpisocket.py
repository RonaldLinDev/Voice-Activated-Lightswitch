import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind(("", 80))
except socket.error:
    print('failed to bind')
s.listen(5)# arbitrary buffer number


while True:
    port, ip = s.accept()
    data = port.recv(1000) # 1000 bits?
    print('light toggle')




port.close()
s.close()

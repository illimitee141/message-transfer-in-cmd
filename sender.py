import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #udp
target_ip = "127.0.0.1"
port_no = 2525
target_address = (target_ip,port_no)

condition = True
while condition:
  message = input("plz write your message here :")
  encrypt_message = message.encode('ascii') # go on google and check the ascii for change encode to code and vice versa
  s.sendto(encrypt_message,target_address)

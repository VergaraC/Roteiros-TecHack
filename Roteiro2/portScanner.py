import socket

ip = input("IP a ser eescaneado: ")

port1 = int(input("Primeiro Port: "))
port2 = int(input("Último Port (até 65535): "))
print("Começando Scan no IP ", ip)
print(" ")
print(" ")

for i in range(port1, port2):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		if s.connect_ex((ip, i)) == 0:
			print(f"Port {i} is open")
			servico = socket.getservbyport(i, "tcp")
			print(f"Serviço {servico} rodando na Porta {i}")
	except:
		pass
	s.close()
#print("other ports are closed")
	

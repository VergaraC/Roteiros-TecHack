import socket

ip = input("Enter the IP ADDRESS to be scanned: ")

start_port = int(input("Enter the start port: "))
end_port = int(input("Enter the end port: "))

def port_scanner():
	for i in range(start_port, end_port):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			if s.connect_ex((ip, i)) == 0:
				service = socket.getservbyport(i, "tcp")
				print(f"service {service} running on port {i}")
		except:
			pass
		s.close()
	print("other ports are closed")
		
port_scanner()
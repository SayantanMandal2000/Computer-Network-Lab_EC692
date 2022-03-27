#Accessing the IP address of the local machine or any other machine.
import socket
host_name=socket.gethostname()
ip1=socket.gethostbyname(host_name)
print(host_name)
print("IP Address is::",ip1)
remote_host='www.jaduniv.edu.in'
print(remote_host)
ip2=socket.gethostbyname(remote_host)
print("Remote IP Address::",ip2)

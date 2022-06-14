import socket
s=socket.socket()
s.bind(('localhost',4444))
s.listen(5)
conn,addr=s.accept()
print("Connection established with",addr)
ans=0.0
while True:
    op=conn.recv(1024)
    op=op.decode()
    if op.lower()=='exit':
        break
    op1=conn.recv(1024)
    op2=conn.recv(1024)
    op1=float(op1)
    op2=float(op2)
    print("Data received: ")
    print("Operator: ",op)
    print("Operand1: ",op1)
    print("Operand2: ",op2)
    if op.lower()=='+':
        ans=op1+op2
    elif op.lower()=='-':
        ans=op1-op2
    elif op.lower()=='*':
        ans=op1*op2
    elif op.lower()=='/':
        ans=op1/op2
    ans_string=str(ans)
    print("Answer is: ",ans)
    conn.send(ans_string.encode())
    
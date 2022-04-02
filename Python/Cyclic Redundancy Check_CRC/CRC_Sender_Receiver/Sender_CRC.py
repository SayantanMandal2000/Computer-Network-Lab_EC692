import socket

def xor(a, b):
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)
 
def mod2div(divident, divisor):
    pick = len(divisor)
    tmp = divident[0: pick]
    while pick < len(divident):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + divident[pick]
        else:  
            tmp = xor('0'*pick, tmp) + divident[pick]
        pick += 1
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*pick, tmp)
    checkword = tmp
    return checkword
 
def encodeData(data, key):
    l_key = len(key)
    appended_data = data + '0'*(l_key-1)
    remainder = mod2div(appended_data, key)
    codeword = data + remainder
    return codeword   
     
data = input("Enter data you want to send=")
print("Entered data in binary format :",data)
key = "1101"
ans = encodeData(data,key)
s = socket.socket()               
s.bind(('localhost',4444))
s.listen(5)
while True:
    conn,addr = s.accept()
    print('Connected with receiver',addr)
    print("Encoded data to be sent to server in binary format :",ans)
    conn.sendall(bytes(ans,'Utf-8'))
    
    

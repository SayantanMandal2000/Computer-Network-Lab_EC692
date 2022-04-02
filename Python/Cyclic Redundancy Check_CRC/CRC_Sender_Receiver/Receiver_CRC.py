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

def decodeData(data, key):
    l_key = len(key)
    appended_data = data.decode() + '0'*(l_key-1)
    remainder = mod2div(appended_data, key)
    return remainder

s=socket.socket()
s.connect(('localhost',4444))
data=s.recv(1024)
print("Received encoded data in binary format :",data.decode())
key = "1101"
ans = decodeData(data,key)
print("Remainder after decoding is->"+ans)
temp = "0" * (len(key) - 1)
"""
if ans == temp:
    s.sendto((data.decode()+" Received No error FOUND").encode(),('localhost',4444))
else:
    s.sendto(("Error in data").encode(),('localhost',4444))
s.close()
"""
if ans==temp:
     print("No Error")
else:
    print("Error")
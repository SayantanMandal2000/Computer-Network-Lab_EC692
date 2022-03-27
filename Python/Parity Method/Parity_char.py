char=input('Enter a character: ')
num=[format(ord(char),'07b')]
print(num)
count=0
for i in num:
    for j in i:
     print('num[0]= ',j)
     if(j=='1'):
        count=count+1
print(count)
if(count%2==0):
    parity=0
else:
    parity=1
num.append(parity)
print(num)

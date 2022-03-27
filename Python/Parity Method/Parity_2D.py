word=input('Enter a word: ')
mat=list()
length=len(word)
for i in word:
    ch=i
    num=[format(ord(ch),'07b')]
    count=0
    for l in num:
        for j in l:
         if(j=='1'):
            count=count+1
    if(count%2==0):
        parity='0'
    else:
        parity='1'
    num.append(parity)
    mat.append(num)
i=0
j=0
count=0
l=list()
l1=[]
total=list()
for i in mat:
    for j in i:
        for p in j:
            l.append(p)
for i in range(len(l)):
 l[i]=int(l[i])
l1=[l[i*8:(i+1)*8] for i in range((len(l)+7)//8)]
for i in l1:
    print(i)
count=[sum(i) for i in zip(*l1)]
for j in count:
     if(j%2==0):
      par=0
     else:
      par=1
     total.append(par)
print(total)


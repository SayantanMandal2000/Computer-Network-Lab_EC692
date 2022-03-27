ip_address=input("Enter the IP Address:")
ip_list=list(map(int,ip_address.split(".")))
flag=0
if len(ip_list)!=4:
    print("Invalid IP Address!!")
else:
    for i in ip_list:
        for i in ip_list:
            if i>255 or i<0:
                print("Invalid IP Address!!")
                flag=1
                break
    if flag!=1:
        if ip_list[0]>=0 and ip_list[0]<=127:
            print("Class A")
        elif ip_list[0]>=128 and ip_list[0]<=191:
            print("Class B")
        elif ip_list[0]>=192 and ip_list[0]<=223:
            print("Class C")
        elif ip_list[0]>=224 and ip_list[0]<=239:
            print("Class D")
        elif ip_list[0]>=240 and ip_list[0]<=255:
            print("Class E")

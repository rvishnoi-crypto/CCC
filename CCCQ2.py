L=int(input())

encodeList=[]
decodeList=[]

for i in range(0,L):
    a=input()
    encodeList.append(a)



for i in encodeList:
    if i[1]==" ":
        i= i[2] * int(i[0])
    else:
        i= i[3]* int(i[0:2])
    decodeList.append(i)



for i in decodeList:
    print(i)




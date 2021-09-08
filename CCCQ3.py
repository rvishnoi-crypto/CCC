N=int(input())
alist_of_pairs=[]
countList=[]
characterList=[]




for i in range(0, N):
    line= input()
    alist_of_pairs.append(line)
print(alist_of_pairs)

for j in alist_of_pairs:
    for i in j:
        print(j.count(i),i)











        

    

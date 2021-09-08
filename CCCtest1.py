import random

def howManyNum():
    k=int(input("How Many Integers Would You like to sum: "))
    print(k)
    return k
    
   
def numsToLine(k,randomList):
    for i  in range(0,k):
        line=int(input("Enter a number: "))
        
        randomList.append(line)
    print(line)
    








howManyNum()

def Sum(list_of_terms):

    length= len(list_of_terms)
    i=0
    while i < length:
        if i== 0 and list_of_terms[i]==0:
           list_of_terms.remove(list_of_terms[i])
           length-=1
           i-=1
        elif list_of_terms[i]==0:
              list_of_terms.remove(list_of_terms[i]) 
              list_of_terms.remove(list_of_terms[i-1])
              length-=2
              i-=2
        else:
           pass
        i+=1
    return list_of_terms



#Main 
##list_of_terms=[2,3,5,4,0,0]

randomList=[]

k=howManyNum()

numsToLine(k,randomList)

a=Sum(randomList)
print(a,sum(a))


    

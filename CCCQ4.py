character= input()

trueList=[1,2,3,4]

            
temp1=1
temp2=2
temp3=3
temp4=4

num1= 1
num2= 2
num3= 3
num4= 4



for i in character:
    if i=="H":
        num1=num3
        num3= temp1
        num2=num4
        num4=temp2
            # This makes sure the flipping is happening 


        temp1=num1
        temp2=num2
        temp3=num3
        temp4=num4
            # This updates the temps
            
        
    else:
        num1=num2
        num2=temp1
        num3=num4
        num4= temp3

        temp1=num1
        temp2=num2
        temp3=num3
        temp4=num4

            


print(num1, num2)
print(num3,num4)

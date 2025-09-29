import math
n=145
temp=n
total=0

while(temp>0):
    remainder=temp%10
    temp=temp//10
    print(remainder)
    a=math.factorial(remainder)
    print(a)
    total=total+a
print(total)      


    
      
    
  



    
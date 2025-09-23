reverse=int(input("Enter the number:"))

temp=reverse
reverseNumber=0

while(temp):
     
     remainder=temp%10
     reverseNumber=reverseNumber*10+remainder
     temp=temp/10




import math

total = 0
x = 2 
n = 0
term = 5
while( term):
    p = pow(x,n)
    f = math.factorial(n)
    # print(p/f)
    if(term%2!=0):
        total+=p/f
    else:
        total-=p/f
    n+=2
    term -=1
print(total)
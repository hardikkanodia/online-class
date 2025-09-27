n=25
temp=n
binary=0
multi=1

while(temp>0):
    remainder = temp%2
    temp=temp//2
    binary+=remainder*multi
    multi=multi*10
print(binary)    
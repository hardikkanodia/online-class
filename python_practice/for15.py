n=int(input("Enter the number of terms:"))
total=0
t=0

for i in range(0,n):
    t=t*10+9
    total+=t
    print(t,end=" ")
print()    
print("Sum of Number of series:",total,end=" ")    
n=int(input("enter no.of rows: "))
for i in range(1,n+1,1):
    for j in range(n,i,-1):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(i-1,end=" ")
    print()

n=int(input("Enter the number:"))
k=11
for i in range(n):
    for j in range(n-i-1):
        print("   ",end="")
    for j in range(i+1):
        print(k,end=" ")
        k=k+1
    print()
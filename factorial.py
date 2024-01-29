def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

n= int(input("Enter a Number: "))
facto=[str(fact(i)) for i in range(1,n+1)]
print(','.join(facto))
def fibo(n):
    if n<=1:
        return n
    else:
        return(fibo(n-1)+fibo(n-2))
trems = int(input("how many trems:"))
print("fibonacci sries: ")
for i in range (trems):
    print(fibo(i))    

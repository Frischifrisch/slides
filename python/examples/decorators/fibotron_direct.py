import decor

def fibo(n):
    return 1 if n in (1,2) else fibo(n-1) + fibo(n-2)

fibo = decor.tron(fibo)

print(fibo(5))

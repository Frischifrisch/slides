import decor

@decor.tron
def fibo(n):
    return 1 if n in (1,2) else fibo(n-1) + fibo(n-2)

print(fibo(5))

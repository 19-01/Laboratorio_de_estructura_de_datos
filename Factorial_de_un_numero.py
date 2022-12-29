import time 
def factor_recursivo(n):
    if n == 1:
        return 1
    return n*factor_recursivo(n-1)
tiempo1=time.perf_counter()
T=factor_recursivo(7)
tiempo2=time.perf_counter()
print(T,"tiempo del factor recursivo:",tiempo2-tiempo1)


def factorial_norecursivo(n):
    x=1
    for i in range(n,1,-1):
        x=x*1
    return x
tiempo1=time.perf_counter()
G=factorial_norecursivo(7)
tiempo2=time.perf_counter()
print(G,"tiempo del factor no recursivo:",tiempo2-tiempo1)
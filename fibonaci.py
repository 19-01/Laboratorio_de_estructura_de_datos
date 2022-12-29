import time
def fibonacci_recursivo(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return fibonacci_recursivo(numero -1)+fibonacci_recursivo(numero-2)
tiempo1=time.perf_counter()
fibonacci_recursivo(5)
tiempo2=time.perf_counter()
print("fibonacci_recursivo tiempo:",tiempo2-tiempo1)


def fibonacci_norecursivo(n):
    a = 0
    b = 1 
    for k in range(n+1):
        c= b+a
        a = b 
        b = c
    return a
tiempo1=time.perf_counter()
fibonacci_norecursivo(5)
tiempo2=time.perf_counter()
print("fibonacci_norecursivo tiempo:",tiempo2-tiempo1)
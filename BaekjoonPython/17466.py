N, P = map(int, input().split())

def calculate(n, p):
    factorial = 1
    for i in range(2, n+1):
        factorial = (factorial * i)%p
    print(factorial % p)

calculate(N, P)
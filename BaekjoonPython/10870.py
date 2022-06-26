def fibonaci(N):
    if N == 0:
        return 0
    if N == 1:
        return 1

    return fibonaci(N-1) + fibonaci(N-2)

n = int(input())
print(fibonaci(n))
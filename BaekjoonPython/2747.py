def fibonaci(N):
    result = [0 for i in range(N+1)]
    result[0] = 0
    result[1] = 1

    for i in range(2, N+1):
        result[i] = result[i-1] + result[i-2]
    print(result[N])
number = int(input())
fibonaci(number)
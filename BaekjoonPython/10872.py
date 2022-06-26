def factorial(N):
    answer = 1
    if N > 0:
        answer = N * factorial(N-1)
    return answer

number = int(input())
print(factorial(number))
A, B = input().split()
N, M = len(A), len(B)

crossWord = [["."] * N for _ in range(M)]
breakCondition = False
positionA = 0
positionB = 0
for i in range(N):
    for j in range(M):
        if A[i] == B[j]:
            positionA = i
            positionB = j
            breakCondition = True
            break
    if breakCondition:
        break

for i in range(N):
    crossWord[positionB][i] = A[i]
for j in range(M):
    crossWord[j][positionA] = B[j]

for i in range(M):
    for j in range(N):
        if j == N-1:
            print(crossWord[i][j])
        else:
            print(crossWord[i][j], end="")



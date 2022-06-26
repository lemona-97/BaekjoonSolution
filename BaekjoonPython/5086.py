def checkNumber(A, B):
    if B % A == 0:
        print("factor")
    elif A % B == 0:
        print("multiple")
    else:
        print("neither")

num1, num2 = map(int, input().split())
checkNumber(num1, num2)
while 1:
    num1, num2 = map(int, input().split())
    if num1 != 0 and num2 != 0:
        checkNumber(num1, num2)
    else:
        break

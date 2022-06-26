A = int(input())
B = int(input())
C = int(input())

if A == 60 and B == 60 and C == 60:
    print("Equilateral")
elif A + B + C == 180 :
    if A == B and A != C:
        print("Isosceles")
    elif A == C and A != B:
        print("Isosceles")
    elif B == C and B != A:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")
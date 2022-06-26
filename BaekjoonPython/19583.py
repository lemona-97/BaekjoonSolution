import sys
input = sys.stdin.readline
S, E, Q = input().split()
SH, SM = S.split(":")
S = int(SH+SM)
EH, EM = E.split(":")
E = int(EH+EM)
QH, QM = Q.split(":")
Q = int(QH+QM)

inAndOut = {}
count = 0
while True:
    try:
        time, name = input().split()
        TH, TM = time.split(":")
        T = int(TH+TM)
        if T <= S:
            inAndOut[name] = 1
        elif E <= T <= Q and name in inAndOut:
            inAndOut.pop(name)
            count += 1
    except:
        break
print(count)

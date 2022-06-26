Month, D, Y, T = input().split()
D = int(D[:-1])
Y = int(Y)
H, M = map(int, T.split(":"))
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
monthName = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
if Y % 400 == 0 or (Y % 4 == 0 and Y % 100 != 0):
    days[1] += 1
totalTime = sum(days) * 24 * 60

lastMonth = monthName.index(Month)
now = (sum(days[:lastMonth]) + D - 1) * 24 * 60 + H * 60 + M
print(now/totalTime * 100)
color1 = input()
color2 = input()
color3 = input()
colorSet = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

result = (colorSet.index(color1)*10 + colorSet.index(color2)) * (10**colorSet.index(color3))
print(result)
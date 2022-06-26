word = input()

count = 0
changeList = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in changeList:
    word = word.replace(i, 'a')
print(len(word))

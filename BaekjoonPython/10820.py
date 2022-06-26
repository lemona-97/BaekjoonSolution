def countString():
    while True:
        try:
            str1 = input()
            lowerCase = 0
            upperCase = 0
            numberCount = 0
            spaceCount = 0
            for i in range(len(str1)):
                if str1[i].islower():
                    lowerCase += 1
                elif str1[i].isupper():
                    upperCase += 1
                elif str1[i].isdigit():
                    numberCount += 1
                else:
                    spaceCount += 1
            print(lowerCase, upperCase, numberCount, spaceCount)
        except EOFError:
          break

countString()
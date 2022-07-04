Dic={}
flag = True
while True:
    userFunction = input("Please Choose your Function")
    if userFunction == "a":
        words = input("Type the word")
        definitions = input("Type the definition")
        Dic[words] = definitions
        print(Dic)
    elif userFunction == "l":
        lookupDic = input("Type the word")
        result = Dic.get(lookupDic)
        if result == None:
            print("That word isn't in the dictionary yet")
        else:
            print(result)
    elif userFunction == "q":
        print("Program ended")
        break
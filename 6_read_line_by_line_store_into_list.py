with open("sample3.txt","r") as f:
    list=f.readlines()
    print(list)
    for x in list:
        print(x.strip())

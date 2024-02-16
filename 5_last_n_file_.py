n=int(input("enter n lines : "))
f=open("sample3.txt","r")
for i in (f.readline() [-n:]):
    print(i)
f.close()
f1=open("sample2.txt","r")
f2=open("sample3.txt","w")
data=f1.readlines()
for lines in data:
    f2.write(lines)
f1.close()
f2.close()


"""
exception handling :- to handle such kind of exception using of try block and except in real word exception handling

"""

try:
    n1=int(input("enter num1 :"))
    n2=int(input("enter num2 :"))
    print(n1/n2)

except ZeroDivisionError:
    print("you can not be enter zero :")
except:
    print("invalid input:")
else:
    name=input("enter a name :")
    print("name, you perform all operation :")
finally:
    print("thank you for using this application :")    
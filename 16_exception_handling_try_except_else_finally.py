n1=int(input("enter a num1 :"))
n2=int(input("enter num2 :"))


try:
    div=n1/n2
    print(div)
except ZeroDivisionError:
    print("zero devision not allowed :")
except NameError:
    print("wrong name :")
else:
    print("exception didn't occure : ")
finally:
    print("always executed :")
    
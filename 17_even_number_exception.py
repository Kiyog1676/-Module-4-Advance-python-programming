class oddnumberexception(Exception):
    pass
try:
    num=int(input("enter a number :"))
    if num%2==0:
        print("even number :")
    else:
        raise oddnumberexception
except oddnumberexception:
    print("odd number not allowed :")


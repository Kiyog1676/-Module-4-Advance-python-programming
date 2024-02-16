"""
class :- class is a collection of datamember and member function, class is a datat types.

class always declare with class keyword

what is self ?

self :- it is ewpresent current class property

it is similar like keyword



"""

class Book:

    def __init__(self,bookname,bookprice):
        self.bname=bookname
        self.bprice=bookprice

    def display(self):
        print(f"{self.bookname}")
        print(f"{self.bookprice}")


obj=Book()

bookname=input("enter bookname")

bookprice=input("enter bookprice :")

obj.display()

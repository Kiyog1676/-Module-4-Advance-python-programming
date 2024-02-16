"""
inharitance :-  one class derived properties of another class 

==> using of inharitance we can reduce our code wich is provide reusability

==> using of inharitance we can save our time 

there are 5 types of inharitance :

1) single level inharitance
2) multi-level inharitance
3) multiple inharitance 
4) haierarchical inharitance
5) hybrid inharitance 

"""

class A:

    def displayA(self):
        print("A class is here :")

class B(A):
    def displayB(self):
        print("B class is here :")

obj=B()
obj.displayA()
obj.displayB()



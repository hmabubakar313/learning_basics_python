class MyComplexNumber():
    def __init__(self,real_no=0,image_no=0):
        print("inside my constructor")
        self.real_no=real_no
        self.image_no=image_no
    
    def display(self):
        print("{0}+{1}i".format(self.real_no,self.image_no))



complx1=MyComplexNumber(40,20)
print("first object")
complx1.display()
complx2=MyComplexNumber(10,20)
print("second object")
complx2.display()
complx2.new_attribute=30
print("printing second object")
print((complx2.real_no,complx2.image_no,complx2.new_attribute))
del complx2
print("deleting object")
print(complx2.real_no)
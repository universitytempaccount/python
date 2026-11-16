class A:
 def show1(self):
  print("Class A")
class B(A):
 def show2(self):
  print("Class B")
class C(B):
 def show3(self):
  print("Class C")
   
obj = C()
obj.show1()
obj.show2()
obj.show3()

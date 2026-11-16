class Father:
 def show1(self):
  print("Father")
class Mother:
 def show2(self):
  print("Mother")
class Child(Father, Mother):
 pass
  
c = Child()
c.show1()
c.show2()

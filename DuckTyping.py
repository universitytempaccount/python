class Car:
 def move(self):
  print("Car is moving")
class Boat:
 def move(self):
  print("Boat is sailing")
def start(obj):
 obj.move()
  
start(Car())
start(Boat())

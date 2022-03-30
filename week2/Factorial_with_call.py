class Factorial:
    def __init__(self):
      self.result = 1
      print("Instance initialized!")
      
    def __call__(self, n):
      if n == 0:
        return 1
      else:
        for x in range(n):
          self.result = self.result * (x+1) #x+1 is used because python starts counting at 0

def driver():
  x = int(input("Find the factorial of: "))
  Factorialof= Factorial()
  Factorialof(x)
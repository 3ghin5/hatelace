class Factorial:
    def __init__(self):
      result=1
      print("Instance initialized!")
      
    def __call__(self):
      if n == 0:
        return 1
      else:
        for x in range(n):
          result=result*(x+1) #x+1 is used because python starts counting at 0

def driver():
  x = int(input("Find the factorial of: "))
  Factorial(x)
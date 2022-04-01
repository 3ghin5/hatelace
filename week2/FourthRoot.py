class ForthrtCalculator:
  def __init__(self):
    self.sqrts = []
    
  def __call__(self, n):
    if n < 0:
      raise Exception("No negative numbers")
    
    if n >= len(self.sqrts):
      for x in range(len(self.sqrts), n + 1):
        self.sqrts.append(x ** 0.25)
        
    return self.sqrts[n]

def tester():
  fourthrt_calc = ForthrtCalculator()
  x = int(input("Enter a number: "))
  print(f"OOP says the fourth root of {x} is {fourthrt_calc(x)}")


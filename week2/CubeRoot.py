def CubeRoot(n):
  result=n**(1/3)
  return result

class cube_root_of:
  def __call__(self, x):
    y=x**(1/3)
    return y
f=cube_root_of() # Creates object; instance of class to use
def driver():
  a=int(input("Take the cube root of: "))
  print("Found the cube root through imperative form: ",end=str(CubeRoot(a)))
  print()
  print("Found the cube root through OOP form: ",end=str(f(a)))
  print()
  
def swap(a,b):
  ageList = [a, b]
  if(a>b):
    temp=ageList[0]
    ageList[0]=ageList[1]
    ageList[1]=temp
  return(ageList)

def driver():
  try:
    a=int(input("Value 1: "))
    b=int(input("Value 2: "))
  except:
    print("Invalid input; please input a number")
  swap(a,b)

# I BUILT THIS FROM SCRATCH R YALL PROUD OF MEEEEE
# LOOK AT ALL THIS LAZY PROGRAMMING *chefs kiss*
def christmasTree(size):
  try:
    if(size>20):
      print("This tree might be too big to display on here correctly, but it would if the screen was big enough. Here goes!")
    for x in range(size):
      print(' '*(size-x) + '* '*x + ' '*(size-x))
    
    print(' '*(size-2)+'***'+' '*(size))
    print(' '*(size-2)+'***'+' '*(size))
  except:
    print('OOPS! The christmas tree broke.')
def driver():
  try: 
    x = 2*int(input("How big do you want your christmas tree? ==["))
  except:
    print('Please input a positive integer.')
  christmasTree(x)
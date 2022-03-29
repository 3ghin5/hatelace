def numpad():
  matrix = array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
  m = reshape(matrix,(3,3))
  for row in m:
    for x in row:
      print(x, end=" ")
    print()
def driver():
  numpad()
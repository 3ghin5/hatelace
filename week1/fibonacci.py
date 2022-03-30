
# Hack 3: Fibonacci.  Write a recursive program to create a fibonacci sequence including error handling(with try/except) for invalid input
      
FibonacciSequence = []
def Fibonacci_Sequence(max, m):
  if m==1:
    FibonacciSequence.append(0)
  if m==2:
    FibonacciSequence.append(1)
  if m>2:
    FibonacciSequence.append(FibonacciSequence[m-3]+FibonacciSequence[m-2])
  if max>m:
    Fibonacci_Sequence(max, m+1)
  else:
    print(FibonacciSequence)
def driver():
  x=int(input("Iterations: "))
  Fibonacci_Sequence(x, 0)
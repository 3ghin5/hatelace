def fib_seq(n):
    if n == 0:
        print(0)
        return
        
    if n < 0:
        raise Exception("Can't use negative n")
    
    def helper(idx, curr, prev):
        print(curr)
        if idx == n:
            return
        helper(idx + 1, curr + prev, curr)
    
    print(0)
    helper(1, 1, 0)
    
def print_fibo(n):
    try:
        fib_seq(n)
    except:
        print("Invalid n")


def tester():
  f = input('Which Fibonacci number to go up to?: ')
  print_fibo(int(f)-1)


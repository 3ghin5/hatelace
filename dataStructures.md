{% include navbar.html %}

# Data Structures Documentation

Replit embed at [bottom of page](https://3ghin5.github.io/hatelace/dataStructures.html#Replit)

### Print function

 * The field in ` print()` can be left blank to use as a line break when writing into The Console

 * Additionally, the parameter `end` as in `print(x, end=" ")` can be used to have the print statement end with something, like a space. Not sure how this is used since I can just add a space at the end of a print command though. 
 * About the above, if `end=""` is used it can prevent line breaks and let different print commands print in one line.

### Exit

 * `exit()` can be used to exit `while` loops.

### Recursive Functions

 * Recursive functions can be used instead of loops. This can be easier in some cases.
 * A recursive function is one that calls itself. Here is an example of one:
```py
def recur_factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * recur_factorial(n-1)
```

### Classes

 * Classes are the main aspect of Object Oriented Programming. 
 * The methods `__call__` and `__init__` were the focus of this week.
 * `__init__` is a method that is called whenever an instance of the class has been initialized. Here is an example of a class used to find the factorial of a number the user inputs:
```py 
class Factorial:
    def __init__(self):
      self.result=1
      print("Instance initialized!")

```
 * `__call__ ` can be used so that an instance of the class can be called on like it was a function. Here it is used in the same class as before:
```py 
class Factorial:
    def __call__(self, n):
      if n == 0:
        return self.result
      else:
        for x in range(n):
          self.result=self.result*(x+1) #x+1 is used because python starts counting at 0
      print(result)

f = Factorial() #Creating an instance of the class
f(5) #Calling on the instance like it was a function. So here it would print 120.
```
 * Another thing I learned is that a variable to be used throughout a class has to be have a prefix of `self.` as in `self.result` or else it wouldn't work. The methods wouldn't be able to use the variable declared inside the class but outside the method and variables wouldnt otherwise be interchanged between methods. for example if I did `def __init__: x=1` and tried to use it in `def __call__: x = x+1` it wouldn't find `x`. I'd have to call it `self.x`. I had to figure this one out in order to make my OOP Fibonacci work- was confused for the longest time!

## Replit

<iframe frameborder="0" width="100%" height="1500px" src="https://replit.com/@3ghin5/MENU?lite=true"></iframe>

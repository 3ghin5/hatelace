"""
====================[ HACK 1 ]=============================
"""
# Hack 1: InfoDB lists.  Build your own/personalized InfoDb with a list length > 3,  create list within a list as illustrated with Owns_Cars

InfoDb = []
# List with dictionary records placed in a list  
InfoDb.append({  
               "Date": "5/19/2021",
               "Tc": 2459353.829300,  
               "Rp/Rs": 0.174,  
               "Duration": 0.100,  
               "Depth": "3.03%",  
               "Observatory": "BARO",  
               "Analysts":["Ayush", "William"]  
              }) 

InfoDb.append({  
               "Date": "6/2/2021",
               "Tc": 2459367.857660,  
               "Rp/Rs": 0.1535,  
               "Duration": 0.075,  
               "Depth": "2.36%",  
               "Observatory": "BARO",  
               "Analysts":["Pat", "William"]  
              })  


"""
====================[ HACK 2 ]=============================
"""
# given an index this will print InfoDb content
def print_data(n):
    print(InfoDb[n]["Date"], InfoDb[n]["Tc"])  # using comma puts space between values
    print("\t", "Analysts: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Analysts"]))  # join allows printing a string list with separator
    print()

# Hack 2: InfoDB loops. Print values from the lists using three different ways: for, while, recursion


## hack 2a: def for_loop()

def for_loop():
  for n in range(len(InfoDB)):
    print_data(n)
    
## hack 2b: def while_loop(0)

def while_loop(n):
  while True:
    print_data(n)
    n = n + 1
    if n > (len(InfoDB) - 1):
      exit()
## hack 2c : def recursive_loop(0)

def recursive_loop(n):
  print_data(n)
  recursive_loop(n+1)


def tester1():
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0)  # requires initial index to start while
    print("Recursive loop")
    recursive_loop(0)  # requires initial index to start recursion


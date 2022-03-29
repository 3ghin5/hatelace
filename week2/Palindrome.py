import re 
class Palindrome:
  def __init__(self):
    print("Palindrome initialized.")
  def __call__(self, string):
    string = string.lower() 
    string = re.sub(r"[^a-z]", "", string)
    return string==string[::-1] 

def driver():
  j=input("Test for palindromality: ")
  Palindrome(j)
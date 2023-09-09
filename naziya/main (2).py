# python program to find the Factorial of a number using Recursion
#fact_Recur.py
def fact(m):
  if m <= 1:
    return 1
  else:
    return m * fact(m - 1)


# Main program
n = int(input("ENter the value of n:"))
print("the factorial of", n, "is", fact(n))

#1.implement a recursive function to calculate facto1.implement a recursive function to calculate factorial of a given number
def fact_rec(n):
  if n == 0 or n == 1:

    return 1
  else:

    return n * fact_rec(n - 1)


number = int(input("Enter the value :"))
result = fact_rec(number)
print("The factorial of {} is {}.".format(number, result))
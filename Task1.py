# Task 1: Check if a Number is Even or Odd

def evenodd(a):
    if a%2==0:
        print(f"{a} is even number.")
    else:
        print(f'{a} is odd number.')

a = int(input("Enter a number:"))

evenodd(a)
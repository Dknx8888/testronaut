# example.py

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def factorial(n):
    """Return the factorial of n using recursion."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
def fibonacci_recursive(n):
  """
  Calculates the nth Fibonacci number using a naive recursive approach.
  """
  if n <= 1:
    return n
  else:
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
    


def main():
    print("Sum of 3 and 4 is:", add(3, 4))
    print("Factorial of 5 is:", factorial(5))
    print(fibonacci_recursive(10))

if __name__ == "__main__":
    main()

#PROBLEM START

#The Fibonacci number can be calculated as:

#F(n)=⎧⎩⎨0,1,F(n−1)+F(n−2),if n=0if n=1if n≥2
#Given a positive integer N (1≤N≤20), calculate the Nth Fibonacci number.

#Input Specification
#The first line of the input will contain one integer N.

#Output Specification
#Output an integer, representing the Nth Fibonacci number.

#PROBLEM END

def fib(n):
    if n <= 1:
      return n
     
    if n > 0:
     return fib(n-1) + fib(n-2)

n = int(input())

if __name__ == "__main__":
    print(fib(n))

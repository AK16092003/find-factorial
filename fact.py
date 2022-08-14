import sys
sys.setrecursionlimit(10**9)

memo = {1:1 , 0:1}
def factorial(n):
  if n in  memo:
    return memo[n]
  return n*factorial(n-1)

t = int(input("Enter number of testcases : "))
while(t):
  n = int(input("Enter number N : "))
  ans = factorial(n)
  print("Result = ", ans)
  t -= 1

                 #Fibnacci Series
def fib( n):
  a=0
  b=1

  if (n==0):
    return b;

  for _ in range(2, n):
    c=a+b
    a=b
    b=c

  return b

d=int(input("Enter The nth Term : "))
print ("fibbonacci series is : " , fib(d))


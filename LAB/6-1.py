def Addodd(n):
  sum=0
  for i in range (1,n+1):
    if i%2!=0:
      sum=sum+i
  print("Sum of all odd numbers upto n : ",sum)
n=int(input("Enter the value of n :"))
Addodd(n)
n=int(input("Enter the number :"))
n1=0;
for i in range(1,n+1):
  if i%7==0 and i%9 ==0:
    n1=i
    print(n1)
if n1==0: print("No number is divisible by both 7 and 9")
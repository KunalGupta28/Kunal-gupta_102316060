n=int(input("Enter the value :"))
for i in range(1,n+1):
  for j in range(2,i//2+1):
    if(i%j==0):
      print(i)
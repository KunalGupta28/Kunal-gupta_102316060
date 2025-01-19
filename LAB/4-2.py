n=int(input("Enter a no. :"))
print("The Table of" ,n, "is :",list(range(0,n*11,n)))
for i in range(1,11):
  print(n,"*",i,"=",n*i)
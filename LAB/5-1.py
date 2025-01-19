n1=int(input("Enter the first number :"))
n2=int(input("Enter the first number :"))
n3=int(input("Enter the first number :"))
if n1>n2 and n1>n3 :
  print(n1 ,"is the greatest number among the three numbers :")
elif n2>n1 and n2>n3 :
  print(n2 ,"is the greatest number among the three numbers :")
else:
  print(n3 ,"is the greatest number among the three numbers :")

#using max function 
print(max(n1,n2,n3),"is the greatest number amongst the three")
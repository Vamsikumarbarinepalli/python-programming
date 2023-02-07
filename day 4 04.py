n=int(input("Total users:"))
m=int(input("Staff users:"))
a=0
p=m/3
if(n<=0 or n<=m):
    print("Invalid input")
else:
    a=(n-(m+p))+a
    print("Non teaching staff are:",p)
    print("Student users:",a)

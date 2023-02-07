string=int(input("enter the number of words:"))
b=[]
for i in range(0,string):
    c=input("enter the word:")
    b.append(c)
print("list of words are:",b)
choice=input("enter your choice ascending or decending:")
if(choice=='ascending'):
    print("Ascending order:")
    b.sort()
    print(b)
elif(choice=='decending'):
    c=b
    print("decending order:")
    c.reverse()
    print(c)
else:
    print("pic from that both choice.")

a=[]
n=int(input("Enter size of list"))
for i in range(n):
    x=int(input("Enter value "))
    a.append(x)
b=max(a)
print("Max num is ",b)
a.remove(b)
c=max(a)
print("Second highest num",c)
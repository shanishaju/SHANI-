
list1=[]
list2=[]
a=[]
n=int(input("Enter the limit for list1:"))
for i in range(0,n):
    list1.append(str(input("enter the colors:")))
n2=int(input("Enter the limit for list2:"))
for i in range(0,n):
    list2.append(str(input("enter the colors:")))
for i in list1:
    if i not in list2:
        a.append(i)
print(a)

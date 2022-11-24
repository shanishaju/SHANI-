list=[]
n=int(input("enter the numbers:"))
for i in range(0,n):
    list.append(int(input()))
print("list:",list)
for i in range(0,n):
    if list[i]>100:
        list[i]='over'
        print("result list is:",list)

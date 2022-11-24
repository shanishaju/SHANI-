list=[]
n=int(input("Enter the number of colors:"))
for i in range(0,n):
    list.append(str(input()))
print(list)
print("The first colour is:",list[0])
print("The last colour is:",list[-1])

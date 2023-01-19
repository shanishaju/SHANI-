n=int(input("Enter the numbe of terms:"))
f1,f2=0,1
f3=f1+f2
print("Fibanocci series of first",n,"terms")
print(f1)
print(f2)
for i in range(3,n+1):
    print(f3)
    f1=f2
    f2=f3
    f3=f1+f2

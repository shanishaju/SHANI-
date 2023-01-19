num1=input("Enter an integer list(space separated):")
num=list(map(int,num1.split()))
num=[i for i in num if i%2!=0]
print("List aftr removing even number",end='')
print(num)

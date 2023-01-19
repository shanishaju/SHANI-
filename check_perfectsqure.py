import math
a=int(input("Enter starting index:"))
b=int(input("Enter ending index:"))
for i in range(a,b):
      num=int(math.sqrt(i))
      if(num*num==i):
          n=i
          while n!=0:
              r=n%10
              n=n//10
              if r%2!=0:
                  break
              else:
                print(i)

import operator
employees={}
n=int(input("enter the number of elements"))
for i in range(n):
  name=input("enter employees name:")
  salary=input("enter employes salary:")
  employees[name]=salary
print("dictionary",employees)
a=sorted(employees.items(),key= operator.itemgetthem(1))
print("ascending order is",a)
d=dict(sorted(employees.item(),key=operator.itemgetthem(1),reverse=true))
print("descending order is:",d)

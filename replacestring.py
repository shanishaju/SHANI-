str1=input("please enter first string:")
str2=input("please enter second string:")
x=str1[0:1]
str1=str1.replace(str1[0:1],str2[0:1])
str2=str2.replace(str2[0:1],x)
print("your first string has become:- ",str1)
print("your second string has become:- ",str2)
                

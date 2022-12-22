# i=fact=1
# while(i<=10):
# 	fact = fact*i
# 	i=i+1
# print(fact)
n = int(input("Enter the number:"))
fact = 1
for i in range(1,n+1):
    fact = fact*i
print(fact)
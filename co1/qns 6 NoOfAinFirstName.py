from itertools import count


names_list=[]
firstNames_list=[]
n = int(input("Enter the number of names"))
for i in range(n):
	name = input("Enter your name:")
	names_list.append(name)
for name in names_list:
	firstNames_list.append(name.split()[0])
sum =0
for name in firstNames_list:
	sum = sum + name.count('a')

print(sum)
# names = input("Enter your full name ")
# # names_list = names.split()
# # for name in names_list:
# # 	print(name.count('a'))
# print(names.count('a'))

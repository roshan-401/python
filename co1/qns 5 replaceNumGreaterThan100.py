num_list = []
num = int(input("enter the range: "))
for x in range(num):
  n = int(input("enter the number"))
  num_list.append(n)
for x in range(num):
    if num_list[x] > 100:
        num_list[x] = "over"
print(num_list)


	
        


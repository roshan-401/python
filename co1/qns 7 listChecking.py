list1 = [1,2,3,4,5]
list2 = [4,5,6,7]

print("whether the length of lists is same\n",len(list1)==len(list2))
print("whether the sum of lists is same\n",sum(list1)==sum(list2))
for num in list1:
    if(num in list2):
        print("list2 have an element in list1")
        break

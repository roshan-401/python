z = [-1,0,4,3,-4,-3]
print("1)list of positive integers")
print([num for num in z if num>0])
print("2)list of squares")
n = int(input("enter the range"))
print([x**2 for x in range(1,n+1)])
print("3)list of vowel in a word")
word = input("enter a word: ")
print(set([letter for letter in word if letter in ['a','e','i','o','u']]))
print("4)list of ordinal value")
print([ord(letter) for letter in word])
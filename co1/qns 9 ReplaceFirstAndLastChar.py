str1 = "greetings earthlings"
str1 = list(str1)
temp = str1[0]
str1[0] = str1[-1]
str1[-1] = temp
print(' '.join(str1))
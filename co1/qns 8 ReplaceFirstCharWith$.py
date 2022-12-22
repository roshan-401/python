str1 = "onion is orage in color"
word = '$'

result = str1[0] + str1[1:].replace(str1[0],word)
print(result) 
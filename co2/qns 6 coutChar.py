str = "red ribbon"
for char in set(str)-set(" "):
    print(char,str.count(char))
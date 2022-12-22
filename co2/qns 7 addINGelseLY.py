str_list = ["intresting","jump"]

for str in str_list:
    if(str[-3:] == "ing"):
        str = str+"ly"
    else:
        str += "ing"
    print(str)

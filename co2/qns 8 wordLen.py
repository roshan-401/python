word_list = ["alpenliebe", "mentos", "diary milk" ,"gems"]
result = word_list[0]
for word in word_list:
    # print(word)
    if(len(result)<len(word)):
        result = word
# print(max([len(word)for word in word_list]))
print(result,len(result))
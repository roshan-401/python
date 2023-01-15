readflie = open('greetings.txt','r')
writefile = open("temp.txt",'w')
lines = readflie.read().split('\n')
for i in range(1,len(lines),2):
    writefile.write(lines[i]+'\n')
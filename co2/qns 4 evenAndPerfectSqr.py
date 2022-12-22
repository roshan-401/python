import math
start = 1000
end = 10000

perfect_sqr = list()
for n in range(start,end):
    if((math.sqrt(n) % 1) == 0 and len([(d) for d in str(n) if int(d)%2 != 0]) == 0):
        perfect_sqr.append(n)
print(perfect_sqr)
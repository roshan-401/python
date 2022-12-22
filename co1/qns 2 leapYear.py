year = int(input("Enter a year"))

# for year in range(2022,year+1):
if(year%400==0 or year%100!=0 and year%4==0):
    print(year," is a leap year")
else:
    print(year," is not a leap year")

# fruits = {}
# for i in range(2):
#     fruits[i] = input("enter a fruit")
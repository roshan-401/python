class Time:
    def __init__(self,hour,minute,second):
        self.hour = hour
        self.minute = minute
        self.second = second
    def __add__(self,other):
        sec1 = self.hour*60*60 + self.minute*60 + self.second
        sec2 =  other.hour*60*60 + other.minute*60 + other.second
        totalSeconds = sec1 + sec2
        finalHour = int(totalSeconds/3600)
        finalMinutes = int((totalSeconds%3600)/60)
        finalSecs = int((totalSeconds%3600)%60)
        return (finalHour, finalMinutes, finalSecs)

t1 = Time(2,15,00)
t2 = Time(1,45,30)
print(t1+t2)


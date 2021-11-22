class Time:

    def __init__(self, hour=None, minute=None, second=None):
        self.hour = hour
        self.minute = minute
        self.second = second
        #self.func() mishe hatta tabe ezafe kard vali ba self 

    def sum(self, time):
        result = Time()
        result.second = self.second + time.second
        result.minute = self.minute + time.minute
        result.hour = self.hour + time.hour
        if result.second>=60:
            result.second-=60
            result.minute+=1
        if result.minute>=60:
            result.minute-=60
            result.hour+=1
        return result


    def sub(self, time):
        result = Time()
        result.second = self.second - time.second
        result.minute = self.minute - time.minute
        result.hour = self.hour - time.hour
        if result.second<0:
            result.minute-=1
            result.second+=60
        if result.minute<0:
            result.hour-=1
            result.minute+=60
        return result


    def secondtohour(self):
        result = Time()
        result.hour = self.second//3600
        result.minute = (self.second%3600)//60
        result.second = (self.second%3600)%60
        return result


    def hourtosecond(self):
        return self.hour*3600 + self.minute*60 + self.second


    def show(self):
        return str(self.hour)+':'+str(self.minute)+':'+str(self.second)


list1 = list(map(int, input('enter time1: e.g. (hour:minute:second)\n').split(':')))
list2 = list(map(int, input('enter time2: e.g. (hour:minute:second)\n').split(':')))

t1 = Time(list1[0], list1[1], list1[2])
t2 = Time(list2[0], list2[1], list2[2])

sec = Time(0 ,0 ,int(input('give me second convert to time: ')))


print('sum: %s\nsub: %s\ntimeToSec: %s\nsecToTime: %s'%((t1.sum(t2)).show(), t1.sub(t2).show(), t1.hourtosecond(), (sec.secondtohour()).show()))
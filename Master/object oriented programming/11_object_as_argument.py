# adding two times by object as argument

class Time:
    def __init__(self,hr, mins, sec):
        self.hr = hr
        self.mins = mins
        self.sec = sec

    def Add(self, t1):
        temp = Time(0,0,0)
        temp.hr = t1.hr + self.hr
        temp.mins = t1.mins + self.mins
        temp.sec = t1.sec + self.sec
        return temp
    
    def Diff(self, t1):
        temp = Time(0,0,0)
        temp.hr = t1.hr - self.hr
        temp.mins = t1.mins - self.mins
        temp.sec = t1.sec - self.sec
        return temp
    
    def print_data(self):
        print('The time is',self.hr,':',self.mins,':',self.sec)
    

t1 = Time(1,20,3)
t2 = Time(6,35,10)

t3 = t1.Add(t2)
t4 = t1.Diff(t2)

t3.print_data()
t4.print_data()

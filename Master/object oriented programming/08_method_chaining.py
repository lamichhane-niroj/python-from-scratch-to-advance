#if we want to execute one method after another we can use method chaining

class Car():
    def start(self):
        print('Engine is starting')
        return self

    def drive(self):
        print('Driving car')
        return self

    def reach(self):
        print('We have reached to destination')
        return self

    def stop(self):
        print('Engine is stopping')
        return self



tesla = Car()
#method chaining
tesla.start().drive().reach().stop() 
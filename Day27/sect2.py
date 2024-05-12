def add(*args):
    print(type(args))
    print(args)
        
add(1,2,3,4,5,'a','b','v','f')

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get('make')
        self.model = kwargs.get('model')
        
car = Car(make='hyundai', model='avante')
print(car.make)
print(car.model)
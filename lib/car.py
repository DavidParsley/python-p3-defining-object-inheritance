from vehicle import Vehicle

class Car(Vehicle):
    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"
    
pp= Car(37, 99)
print(pp.wheel_number)
print(pp.wheel_size)   
print(pp.fill_up_tank())
print(pp.go())    

print(Car.__bases__)


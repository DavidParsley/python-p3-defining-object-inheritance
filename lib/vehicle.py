class Vehicle:
    def __init__(self, wheel_size, wheel_number):
        self.wheel_size = wheel_size
        self.wheel_number = wheel_number

    def go(self):
            return "vrrrrrrrooom!"
        
    def fill_up_tank(self):
            return "filling up!"
        
McLaren = Vehicle(70, "37")
print(f"Wheel size:{McLaren.wheel_size} \nWheel Number: {McLaren.wheel_number}")
print(f"My Car sounds like: {McLaren.go()}")
print(f"I'm at the gas station {McLaren.fill_up_tank()}")




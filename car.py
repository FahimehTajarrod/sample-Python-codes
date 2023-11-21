
class CAR: 
    def __init__(self, model, year, color):
         self.model = model 
         self.year=year
         self.color=color
         self.wheels=4
         
    def drive(self):
          print(self.model+" is driving.")
 		
    def stop(self):
          print(self.model+" is stoped.")

    def read_wheels(self):
        print(self.model+" has "+str(self.wheels)+" wheels.")
        
    def set_wheels(self, new_wheels):
        self.wheels=new_wheels


class ElectricCar(CAR):
     def __init__(self, model, year, color):
         super().__init__(model, year, color)
         self.battery_size = 70

     def describe_battery(self):
         print(self.model+" has " + str(self.battery_size) + "-kWh battery.")

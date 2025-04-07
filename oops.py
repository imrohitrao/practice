class Car:
    total_car = 0
    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + "!"

    def full_name(self):
        return f"{self.__brand} {self.__model}"

    #withoutdecorator  
    def fuel_type():
        return "Petrol or Diesel"

    #decorator for static method  
    @staticmethod
    def fuel_type():
        return "Petrol or Diesel"

    @property
    def model(self):
        return self.__model

    


class ElectricCar(Car):
    def __init__(self, brand, model, range):
        super().__init__(brand, model)
        self.range = range

    def fuel_type(self):
        return "Eelectric"



class Battery:
    def battery_info(self):
        return "This is a Battery"

class Engine:
    def engine_info(self):
        return "This is a Engine"

class ElectricCarTwo(Battery,Engine,ElectricCar):
    pass

my_new_tesla = ElectricCarTwo("Tesla","Model 3")
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())

# my_car = Car("Toyota", "Camry")
# my_electriccar=ElectricCar("Tesla","Model 3",500)

# print(my_electriccar.model)
# print(isinstance(my_car,ElectricCar))



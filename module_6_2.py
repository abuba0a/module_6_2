class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, __model, __color, __engine_power):
        self.new_color = None
        self.owner = owner
        self.__model = __model
        self.__color = __color
        self.__engine_power = __engine_power

    def get_model(self):
        print('Модель: ', self.__model)

    def get_horsepower(self):
        print('Мощность двигателя: ', self.__engine_power)

    def get_color(self):
        print('Цвет: ', self.__color)

    def set_color(self, new_color):
        self.new_color = new_color

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print('Владелец: ', self.owner)


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner, __model, __color, __engine_power):
        super().__init__(owner, __model, __color, __engine_power)


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
vehicle2 = Sedan('Bob', 'BMW', 'red', 250)

# Изначальные свойства
vehicle1.print_info()
print()
vehicle2.print_info()


# Меняем свойства (в т.ч. вызывая методы)


# set_color('Pink')
# set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
print()
vehicle1.print_info()

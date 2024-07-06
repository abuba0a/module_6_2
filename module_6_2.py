class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, __model, __color, __engine_power):
        def get_model(__model):
            print('Модель: ', __model)

        def get_horsepower(__engine_power):
            print('Мощность двигателя: ', __engine_power)

        def get_color(__color):
            print('Цвет: ', __color)

        def print_info():
            get_model(__model)
            get_horsepower(__engine_power)
            get_color(__color)
            print('Владелец: ', owner)

        print_info()


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner, __model, __color, __engine_power):
        super().__init__(owner, __model, __color, __engine_power)

    def print_info(self):
        pass


# def set_color(new_color):
#     if new_color.__COLOR_VARIANTS:
#         self__color = new_color
#     else:
#         print('Нельзя сменить цвет на ', new_color)


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)


# set_color('Pink')
# set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()

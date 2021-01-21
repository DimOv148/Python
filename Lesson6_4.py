class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = ([is_police])
        self.turn_status = 'left'


    def go(self):
        print(f'{self.name} начинает движение')

    def stop(self):
        print(f'{self.name} останавливается')

    def turn_left(self):
        self.turn_status = 'left'

    def turn_right(self):
        self.turn_status = 'right'

    def show_speed(self):
        print(self.speed)

class TownCar(Car):

    def __init__(self, speed, color, name, is_police, passengers, year):
        Car.__init__(self, speed, color, name, is_police)
        self.passengers = passengers
        self.year = year

    def show_speed(self):
        print(self.speed)
        if self.speed > 60:
            print('Ваша скорость превышена')


class SportCar(Car):

    def __init__(self, speed, color, name, is_police, max_speed, engine_type):
        Car.__init__(self, speed, color, name, is_police)
        self.max_speed = max_speed
        self.engine_type = engine_type

    def max_sped(self):
       print(f'Время прохождения круга на Нюрбургринге составляет :{(5.15 / self.max_speed * 3600):.4} секунды')


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police, load, car_body):
        Car.__init__(self, speed, color, name, is_police)
        self.load = load
        self.car_body = car_body

    def show_speed(self):
        print(self.speed)
        if self.speed > 40:
            print('Ваша скорость превышена')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police, weapon, armor):
        Car.__init__(self, speed, color, name, is_police)
        self.weapon = weapon
        self.armor = armor
    def pursuit(self):
        if self.is_police == [True]:
            self.weapon = 'Weapon charged 100 %'
            self.armor = 'Armor 100%'
        else:
            self.weapon = 'Weapon not charged'
            self.armor = 'Armor 0%'
        return print(self.weapon + ", " + self.armor)






a = Car(123, 'red', 'bmw', False)
a.show_speed()
print(a.color)
print(a.is_police)
b = WorkCar(80, 'green', 'MAZ', False, 12500, 'tent')
b.go()
print(b.name)
print(b.is_police)
print(b.turn_status)
b.turn_right()
print(b.turn_status)
ferrari = SportCar(200, 'red', 'F8 Tributo', False, 340, 'v8 turbo')
ferrari.max_sped()
print(ferrari.is_police)
shevrolet = PoliceCar(120, 'black&white', 'Corvet', True, 'none', 'none')
print(shevrolet.name)
print(shevrolet.is_police)
shevrolet.pursuit()
from abc import ABC, abstractmethod

class Cloth(ABC):

    @abstractmethod
    def coat(self):
        pass

    @abstractmethod
    def suit(self):
        pass

class Coat_suit(Cloth):
    def __init__(self, size, height):
        self.size = size
        self.height = height

    def coat(self):
        return round(self.size / 6.5 + 0.5)

    def suit(self):
        return round(self.height * 2 + 0.3)

    @property
    def all_cloth(self):
        return f'Всего необходимо {self.coat() + self.suit()} метров ткани'


ac = Coat_suit(50, 75)
print(f'Для костюма потребуется {ac.suit()} метров ткани')
print(f'Для пальто потребуется {ac.coat()} метров ткани')
print(ac.all_cloth)


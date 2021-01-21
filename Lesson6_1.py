import time
class TrafficLight:
    def __init__(self):
        self.__color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        count = 0
        while True:
            if count < 3:
                print(f'Сейчас горит {self.__color[count]}')
            if count == 0:
                time.sleep(7)
            elif count == 1:
                time.sleep(2)
            elif count == 2:
                time.sleep(5)
            count +=1
            if count > 3:
                a = input('Надоело стоять на светофоре - жми Enter, если нет любую клавишу')
                if not a:
                    break
                count = 0

crossroad = TrafficLight()
crossroad.running()


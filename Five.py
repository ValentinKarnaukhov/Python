class Buffer:
    def __init__(self):
        self.buff=[]


    def add(self, *a):
        self.buff.extend(a)
        while len(self.buff)>6:
            s = 0
            for i in range(5):
                s+=self.buff.pop(0)
            print(s)

        # добавить следующую часть последовательности


    def get_current_part(self):
        return self.buff

buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part() # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
buf.get_current_part() # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
buf.get_current_part() # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
buf.get_current_part() # вернуть [1]
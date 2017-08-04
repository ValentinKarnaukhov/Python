class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.value=0

    def can_add(self, v):
       if v>self.value:
           return False
       else:
           return True

    def add(self, v):
        self.value+=v


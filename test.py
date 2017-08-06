

class ExtendedStack(list):
    def sum(self):
        a=self.pop()+self.pop()
        self.append(a)

    def sub(self):
        a = self.pop() - self.pop()
        self.append(a)

    def mul(self):
        a = self.pop() * self.pop()
        self.append(a)

    def div(self):
        a = self.pop() // self.pop()
        self.append(a)

r=ExtendedStack([1,2,3,4,5])
r.sum()
print(r)
#single level
class one:
    x=10
    y=20
    def add(self):
        z=self.x+self.y
        print(z)
class second(one):
    t=1
    t2=2
    def mul(self):
        n=self.t*self.t2
        print(n)
k=one()
k.add()
p=second()
p.mul()
p.add()
print(id(p))
print(id(k))
#multiple inheritance
class one:
    x=20
    y=20
    def add(self):
        z=self.x+self.y
        print(z)
class second:
    t1=1
    t2=3
    def mul(self):
        n=self.t1*self.t2
        print(n)
class third(one,second):
    def div(self):
        q=self.x/self.y
        print(q)
k=third()
k.add()
k.mul()
k.div()

#multilevel inheritance
class one:
    x=10
    y=20
    def add(self):
        z=self.x+self.y
        print(z)
class second(one):
    def mul(self):
        n=self.x*self.y
        print(n)
class third(second):
        def div(self):
            z=self.x/self.y
            print(z)
p=third()
p.div()
print(id(p))
p.add()
p.mul()

#hirechal
class one:
    x=20
    y=10
    def add(self):
        z=self.x+self.y
        print(z)
class second(one):
    def mul(self):
        z=self.x*self.y
        print(z)
class third(one):
    def div(self):
        z=self.x/self.y
        print(z)
class fourth(one):
    def rem(self):
        z=self.x%self.y
        print(z)
k=second()
k.mul()
k.add()
p=third()
p.div()
p.add()
u=fourth()
u.rem()
u.add()
#hybrid
class one:
    x=10
    y=20
    def add(self):
        z=self.x+self.y
        print(z)
class second(one):
    def mul(self):
        z=self.x*self.y
        print(z)
class third(second):
    def div(self):
        z=self.x/self.y
        print(z)

class fourth(third):
    def add(self):
        z=self.x+self.y
        print(z)
class fifth(third):
    def mul(self):
        z=self.x*self.y
        print(z)
class sixth(fourth,fifth):
    def rem(self):
        z=self.y%self.t
        print(z)
p=sixth()
p.rem()
p.mul()
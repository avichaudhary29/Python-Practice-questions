class emp:
    _salary = 9000
    __salary = 5000

    def show(self):
        print(self._salary)  # Access the _salary attribute with self


k = emp()
k.salary = 17000
k.show()  # This will print 9000, which is the value of _salary
print(k._salary)  # This will print 17000, which is the value you set
# Accessing the name-mangled __salary attribute
print(k._emp__salary)  # This will print 5000

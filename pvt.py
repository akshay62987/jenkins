class Human:
    __name = "Robinhood"
    def info(self):
        print(Human.__name)
    def get_info(self):
        return self.__name
    def set_info(self,name):
        self.__name= name
o = Human()
print(o._Human__name)
o.info()
print(o.get_info())
o.set_info("Akshay")
print(o.get_info())
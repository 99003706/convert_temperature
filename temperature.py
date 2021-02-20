class Temperature:
    def __init__(self, temp):

        self.temp_cel = temp
        self.temp_far = 0

    def temp(self):
        return self.temp_cel

    def display(self):
        print(self.temp_cel)

    def convert(self):

        self.temp_far = (1.8 * self.temp_cel) + 32
        return round(self.temp_far, 3)

    def __add__(self, other):
        value = self.temp_cel + other.temp_cel
        return Temperature(value)

    def __eq__(self, other):
        if self.temp_cel == other.temp_cel:
              return True
        return False

    def __lt__(self, other):
        if self.temp_cel < other.temp_cel:
            return True
        return False


t1 = Temperature(45)
print(t1.convert())





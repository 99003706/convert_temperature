class Temperature:
    def __init__(self, temp):

        self.cel = temp
        self.farh = 0

    def temp(self):
        return self.cel

    def display(self):
        print(self.cel)

    def convert(self):

        self.temp_far = (1.8 * self.cel) + 32
        return round(self.temp_far, 3)

    def __add__(self, other):
        value = self.cel + other.cel
        return Temperature(value)

    def __eq__(self, other):
        if self.cel == other.cel:
              return True
        return False

    def __lt__(self, other):
        if self.cel < other.cel:
            return True
        return False


# t1 = Temperature(43)
# print(t1.convert())





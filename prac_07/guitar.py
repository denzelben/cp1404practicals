YEAR = 2024
VINTAGE_AGE_THRESHOLD = 50

class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name},{int(self.year)},{float(self.cost)}"


    def get_age(self):
        return YEAR - self.year

    def is_vintage(self):
        return self.get_age() >= VINTAGE_AGE_THRESHOLD

    def __lt__(self, other):
        return self.year < other.year
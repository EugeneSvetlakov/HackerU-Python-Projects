class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_r(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __str__(self):
        return f"Point: {self.x},{self.y}"

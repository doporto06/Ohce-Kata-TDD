class Ohce:
    def __init__(self, name, time):
        self.name = name
        self.time = time

    def greet(self):
        hour = self.time.hour
        if hour == 6 or hour == 9 or (hour == 11 and self.time.minute == 59):
            return "¡Buenos días Diego!"

    def process_input(self):
        pass
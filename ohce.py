class Ohce:
    def __init__(self, name, time):
        self.name = name
        self.time = time

    def greet(self):
        hour = self.time.hour
        name = self.name
        if 6 <= hour < 12:
            return f"¡Buenos días {name}!"
        elif 12 <= hour < 20:
            return f"¡Buenas tardes {name}!"
        elif 20 <= hour or hour < 6:
            return f"¡Buenas noches {name}!"

    def process_input(self, input):
        return input[::-1]
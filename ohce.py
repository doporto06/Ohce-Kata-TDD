class Ohce:
    def __init__(self, name, time):
        self.name = name
        self.time = time

    def greet(self):
        hour = self.time.hour
        name = self.name
        if 6 <= hour < 12:
            return f"¡Buenos días {name}!"
        elif hour == 15 or hour == 12:
            return f"¡Buenas tardes {name}!"

    def process_input(self):
        pass
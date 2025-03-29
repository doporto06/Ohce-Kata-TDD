import sys

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
        if input == "Stop!":
            msg = f"Adios {self.name}"
            print(msg)
            sys.exit(0)
            return msg # When running the script normally (outside of tests), this line will not be reached. In tests, 'sys.exit' is mocked, so that the test passes.
        
        reversed_input = input[::-1]
        if input == reversed_input:
            return f"{reversed_input}\n¡Bonita palabra!"
        return reversed_input
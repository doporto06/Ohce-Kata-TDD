import datetime
from ohce import Ohce

def main():
    name = input("Enter your name: ")
    ohce = Ohce(name, datetime.datetime.now())

    print("> " + ohce.greet())

    while True:
        user_input = input("$ ")
        response = ohce.process_input(user_input)
        print("> " + response)

if __name__ == "__main__":
    main()
import re
import sys

class Converter:
    def __init__(self, conversion_factor, unit):
        self.conversion_factor = conversion_factor
        self.unit = unit

    @staticmethod
    def get_numbers_from_input(data):
        pattern = r'-?\d+\.?\d*'
        numbers = re.findall(pattern, data)
        return [float(num) for num in numbers]

    def convert_and_format(self, numbers):
        converted_numbers = [(int(num / self.conversion_factor * 100)) / 100 for num in numbers]
        return " x ".join([str(num) for num in converted_numbers]) + f" {self.unit}"

    def convert(self, prompt):
        while True:
            user_input = input(prompt)
            if user_input.upper() == "B":
                break
            elif user_input.upper() == "Q":
                sys.exit()
            else:
                numbers = self.get_numbers_from_input(user_input)
                if numbers:
                    result = self.convert_and_format(numbers)
                    print(result)
                    break
                else:
                    print("Invalid input.")


class LengthConverter:
    def __init__(self):
        self.cm_converter = Converter(2.54, "in")
        self.mm_converter = Converter(25.4, "in")

    def length_convert(self):
        while True:
            choice = input("Enter C for CM or M for MM:\n").upper()

            if choice == "C":
                self.cm_converter.convert("Enter the full dimension in CM:\n")
            elif choice == "M":
                self.mm_converter.convert("Enter the full dimension in MM:\n")
            elif choice == "B":
                break
            elif choice == "Q":
                sys.exit()
            else:
                print("Invalid choice. Please enter C, M, B, or Q.")


class WeightConverter:
    def __init__(self):
        self.g_converter = Converter(453.6, "lbs")
        self.kg_converter = Converter(0.4536, "lbs")

    def weight_convert(self):
        while True:
            choice = input("Enter G for Grams or K for Kilograms:\n").upper()

            if choice == "G":
                self.g_converter.convert("Enter the full weight in Grams:\n")
            elif choice == "K":
                self.kg_converter.convert("Enter the full weight in Kilograms:\n")
            elif choice == "B":
                break
            elif choice == "Q":
                sys.exit()
            else:
                print("Invalid choice. Please enter G, K, B, or Q.")


class TempConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    def temp_convert(self):
        while True:
            choice = input("Enter the temperature in Celsius:\n")

            if choice.upper() == "B":
                break
            elif choice.upper() == "Q":
                sys.exit()
            else:
                try:
                    numbers = Converter.get_numbers_from_input(choice)
                    if len(numbers) > 0:
                        temp_celsius = numbers[0]
                        temp_fahrenheit = self.celsius_to_fahrenheit(temp_celsius)
                        print(f"{temp_fahrenheit:.2f}\N{DEGREE SIGN}F")
                    else:
                        print("Invalid input.")
                except ValueError:
                    print("Invalid input.")


class MainApp:
    def __init__(self):
        self.length_converter = LengthConverter()
        self.weight_converter = WeightConverter()
        self.temp_converter = TempConverter()

    def run(self):
        while True:
            print("Enter L for Length, W for Weight, T for Temp.\n"
                "At any time you can enter B to go back or Q to quit the program.\n")
            choice = input().upper()

            if choice == "L":
                self.length_converter.length_convert()
            elif choice == "W":
                self.weight_converter.weight_convert()
            elif choice == "T":
                self.temp_converter.temp_convert()
            elif choice == "Q":
                sys.exit()
            else:
                print("Invalid choice.")


if __name__ == "__main__":
    app = MainApp()
    app.run()

import re
import sys

class Converter:
    @staticmethod
    def get_numbers_from_input(data):
        """
        Extracts numbers from input data.
        
        Args:
        - data (str): Input data string containing numeric values.
        
        Returns:
        - list: List of floats extracted from the input data.
        """
        pattern = r'-?\d+\.?\d*'
        numbers = re.findall(pattern, data)
        return [float(num) for num in numbers]

    @staticmethod
    def format_output(numbers, unit):
        """
        Formats the converted numbers with the specified unit.
        
        Args:
        - numbers (list): List of numbers to format.
        - unit (str): Unit to append to each formatted number.
        
        Returns:
        - str: Formatted string representation of the converted numbers with units.
        """
        return " x ".join([str(num) for num in numbers]) + f" {unit}"

    def convert(self, conversion_factor, unit_from, unit_to):
        """
        Handles conversion process interactively until user quits or goes back.
        
        Args:
        - conversion_factor (float): Factor to multiply input numbers for conversion.
        - unit_from (str): Unit of input data.
        - unit_to (str): Unit to convert input data into.
        """
        while True:
            user_input = input(f"\nEnter the full dimension in {unit_from} (B to go back, Q to quit):\n")
            if user_input.upper() == "B":
                break
            elif user_input.upper() == "Q":
                sys.exit()
            else:
                try:
                    numbers = self.get_numbers_from_input(user_input)
                    if numbers:
                        converted_numbers = self.perform_conversion(numbers, conversion_factor)
                        if converted_numbers:
                            formatted_output = self.format_output(converted_numbers, unit_to)
                            print(f"Converted value: {formatted_output}")
                    else:
                        print("Invalid input. Please enter numeric values.")
                except ValueError:
                    print("Invalid input. Please enter numeric values.")
                except Exception as e:
                    print(f"Error: {e}")

    def perform_conversion(self, numbers, conversion_factor):
        """
        Converts numbers based on conversion factor.
        
        Args:
        - numbers (list): List of numbers to convert.
        - conversion_factor (float): Factor to multiply each number for conversion.
        
        Returns:
        - list: List of converted numbers.
        """
        try:
            return [(int(num / conversion_factor * 100)) / 100 for num in numbers]
        except ZeroDivisionError:
            print("Error: Conversion factor should not be zero.")
            return None

class LengthConverter:
    def __init__(self):
        self.cm_converter = Converter()
        self.mm_converter = Converter()

    def length_convert(self):
        """
        Handles length conversion between CM and MM to inches.
        """
        while True:
            choice = input("\nEnter C for CM or M for MM (B to go back, Q to quit):\n").upper()

            if choice == "C":
                self.cm_converter.convert(2.54, "CM", "inches")
            elif choice == "M":
                self.mm_converter.convert(25.4, "MM", "inches")
            elif choice == "B":
                break
            elif choice == "Q":
                sys.exit()
            else:
                print("Invalid choice. Please enter C, M, B, or Q.")

class WeightConverter:
    def __init__(self):
        self.g_converter = Converter()
        self.kg_converter = Converter()

    def weight_convert(self):
        """
        Handles weight conversion between Grams and Kilograms to lbs.
        """
        while True:
            choice = input("Enter G for Grams or K for Kilograms (B to go back, Q to quit):\n").upper()

            if choice == "G":
                self.g_converter.convert(453.6, "Grams", "lbs")
            elif choice == "K":
                self.kg_converter.convert(0.4536, "Kilograms", "lbs")
            elif choice == "B":
                break
            elif choice == "Q":
                sys.exit()
            else:
                print("Invalid choice. Please enter G, K, B, or Q.")

class TempConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        """
        Converts Celsius to Fahrenheit and rounds to the nearest whole number.
        
        Args:
        - celsius (float): Temperature in Celsius.
        
        Returns:
        - int: Converted temperature in Fahrenheit.
        """
        return round((celsius * 9/5) + 32)

    def temp_convert(self):
        """
        Handles temperature conversion from Celsius to Fahrenheit.
        """
        while True:
            choice = input("\nEnter the temperature in Celsius (B to go back, Q to quit):\n")

            if choice.upper() == "B":
                break
            elif choice.upper() == "Q":
                sys.exit()
            else:
                self.convert_temperature_range(choice)

    def convert_temperature_range(self, temperature_range):
        """
        Converts and prints the temperature range from Celsius to Fahrenheit.
        
        Args:
        - temperature_range (str): Input temperature range in Celsius.
        """
        try:
            pattern = r'^(-?\d+\.?\d*)\s*(-|~)?\s*(-?\d+\.?\d*)?\s*°?C?$'  # Flexible regex pattern for various temperature formats
            match = re.match(pattern, temperature_range.strip())
                    
            if match:
                start_celsius = float(match.group(1))
                end_celsius = float(match.group(3)) if match.group(3) else start_celsius
                
                start_fahrenheit = self.celsius_to_fahrenheit(start_celsius)
                end_fahrenheit = self.celsius_to_fahrenheit(end_celsius)
                
                if start_celsius == end_celsius:
                    output = f"{start_fahrenheit}\N{DEGREE SIGN}F"
                else:
                    output = f"{start_fahrenheit}~{end_fahrenheit}\N{DEGREE SIGN}F"
                
                print(f"\nConverted temperature range: {output}")
            else:
                print("\nInvalid input format. Please enter a valid temperature range.")
        except ValueError:
            print("\nInvalid input. Please enter numeric values for temperature.")
        except Exception as e:
            print(f"\nError: {e}")

class MainApp:
    def __init__(self):
        self.length_converter = LengthConverter()
        self.weight_converter = WeightConverter()
        self.temp_converter = TempConverter()

    def run(self):
        """
        Runs the main application loop, allowing users to choose between length, weight, or temperature conversions.
        """
        while True:
            print("\nEnter L for Length, W for Weight, T for Temp.")
            print("At any time you can enter B to go back or Q to quit the program.\n")
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

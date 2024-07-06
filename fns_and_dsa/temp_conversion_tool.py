# temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius.
    """
    return (Fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        # User input
        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()

        if unit == 'c':
            converted_temp = convert_to_fahrenheit(temperature)
            original_unit = '°C'
            converted_unit = '°F'
        elif unit == 'f':
            converted_temp = convert_to_celsius(temperature)
            original_unit = '°F'
            converted_unit = '°C'
        else:
            raise ValueError("Invalid temperature. Please enter a numeric value.")

        print(f"{temperature:.1f}{original_unit} is {converted_temp:.6f}{converted_unit}")
    except ValueError:
        print("Invalid input. Please enter a valid numeric temperature.")

if __name__ == "__main__":
    main()

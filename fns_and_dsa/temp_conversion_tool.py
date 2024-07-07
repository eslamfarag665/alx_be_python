# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
  """Converts temperature from Fahrenheit to Celsius.

  Args:
      fahrenheit: Temperature in Fahrenheit (float).

  Returns:
      Temperature in Celsius (float).
  """
  return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
  """Converts temperature from Celsius to Fahrenheit.

  Args:
      celsius: Temperature in Celsius (float).

  Returns:
      Temperature in Fahrenheit (float).
  """
  return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR


def main():
  """Prompts user for temperature and unit, performs conversion and displays result."""
  while True:
    try:
      temperature = float(input("Enter the temperature to convert: "))
      unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
      break
    except ValueError:
      print("Invalid temperature. Please enter a numeric value.")

  if unit == "C":
    converted_temp = convert_to_fahrenheit(temperature)
    converted_unit = "F"
  elif unit == "F":
    converted_temp = convert_to_celsius(temperature)
    converted_unit = "C"
  else:
    print("Invalid unit. Please enter 'C' or 'F'.")
    return

  print(f"{temperature:.1f}°{unit} is {converted_temp:.1f}°{converted_unit}")


if __name__ == "__main__":
  main()

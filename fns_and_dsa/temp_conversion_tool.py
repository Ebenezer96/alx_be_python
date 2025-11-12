"""
Temperature Conversion Tool
----------------------------
This script demonstrates the concept of variable scope in Python by using
global variables to store conversion factors for converting between
Celsius and Fahrenheit.
"""

# ===== Global Conversion Factors =====
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


# ===== Conversion Functions =====
def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global conversion factor."""
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius


def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global conversion factor."""
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit


# ===== Main Program =====
def main():
    """Main function to handle user input and display converted temperature."""
    try:
        temp_input = input("Enter the temperature value: ").strip()
        unit_input = input("Is this in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Validate temperature input
        if not temp_input.replace('.', '', 1).isdigit():
            raise ValueError("Invalid temperature. Please enter a numeric value.")

        temperature = float(temp_input)

        # Perform conversion based on unit
        if unit_input == 'C':
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature:.2f}°C is {converted:.2f}°F.")
        elif unit_input == 'F':
            converted = convert_to_celsius(temperature)
            print(f"{temperature:.2f}°F is {converted:.2f}°C.")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as e:
        print(e)


# ===== Run Script =====
if __name__ == "__main__":
    main()

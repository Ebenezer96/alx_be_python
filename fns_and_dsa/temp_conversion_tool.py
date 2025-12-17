CELSIUS_TO_FAHRENHEIT = 9 / 5
FAHRENHEIT_TO_CELSIUS = 5 / 9


def celsius_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS


def main():
    try:
        temperature = float(input("Enter the temperature to convert: "))
        scale = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if scale == "C":
            converted = celsius_to_fahrenheit(temperature)
            print(f"{converted}")
        elif scale == "F":
            converted = fahrenheit_to_celsius(temperature)
            print(f"{converted}")
        else:
            print("Invalid temperature scale")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")


if __name__ == "__main__":
    main()

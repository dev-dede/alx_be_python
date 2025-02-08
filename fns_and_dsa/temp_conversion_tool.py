FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit}°F is {celsius}°C")

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f"{celsius}°C is {fahrenheit}°F")

def main():
    try:
        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()
    
    
        if unit == "c":
            convert_to_fahrenheit(temperature)
        elif unit == "f":
            convert_to_celsius(temperature)
        else:
            print("Invalid unit. Select c or f")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
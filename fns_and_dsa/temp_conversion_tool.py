FAHRENHEIT_TO_CELSIUS_FACTOR=5/9
CELSIUS_TO_FAHRENHEIT_FACTOR=9/5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit



def main():
    try:
        temperature = float(input("Enter the temperature to convert: "))
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        return
    
    temperature_scale = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().capitalize()
    
    if temperature_scale == "F":
        result = convert_to_celsius(temperature)
        print(f"{temperature}°F is {result}°C")
    elif temperature_scale == "C":
        result = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {result}°F")
    else:
        print("Invalid temperature scale! Please enter either 'C' or 'F'.")
        


if __name__ == "__main__":
    main()
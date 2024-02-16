#5. Temperature Converter:
# Build a program that converts temperatures between Celsius and Fahrenheit using a dictionary 
#to store conversion factors
def convert_temperature(temperature, conversion_type):
    conversion_factors = {
        'C to F': lambda c: (c * 9/5) + 32,
        'F to C': lambda f: (f - 32) * 5/9
    }

    if conversion_type in conversion_factors:
        converted_temperature = conversion_factors[conversion_type](temperature)
        return converted_temperature
    else:
        return None

def main():
    while True:
        print("\nOptions:")
        print("1. Convert Celsius to Fahrenheit")
        print("2. Convert Fahrenheit to Celsius")
        print("3. Quit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            celsius_temp = float(input("Enter temperature in Celsius: "))
            converted_temp = convert_temperature(celsius_temp, 'C to F')
            print(f"\n{celsius_temp}°C is {converted_temp:.2f}°F.")

        elif choice == '2':
            fahrenheit_temp = float(input("Enter temperature in Fahrenheit: "))
            converted_temp = convert_temperature(fahrenheit_temp, 'F to C')
            print(f"\n{fahrenheit_temp}°F is {converted_temp:.2f}°C.")

        elif choice == '3':
            print("\nExiting the program. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main_":

    main()

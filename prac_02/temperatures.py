# temperatures.py
# Temperature conversion tool

def main():
    MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit"
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = celsius * 9 / 5 + 32
            print(f"Equivalent in Fahrenheit: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5 / 9
            print(f"Equivalent in Celsius: {celsius:.2f} C")
        else:
            print("Invalid selection. Try again.")
        print(MENU)
        choice = input(">>> ").upper()
    print("Goodbye.")

main()
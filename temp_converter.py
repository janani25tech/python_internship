def convert_temperature(value, unit):
    if unit.lower() == "c":
        return f"{value}°C is {(value * 9/5) + 32}°F"
    elif unit.lower() == "f":
        return f"{value}°F is {(value - 32) * 5/9:.2f}°C"
    else:
        return "Invalid unit! Use 'C' or 'F'."


temp = float(input("Enter temperature value: "))
unit = input("Enter unit (C/F): ")
print(convert_temperature(temp, unit))

def c_to_f(celsius):
    return (celsius * 9/5) + 32

temp_c = float(input("Enter temperature in Celsius: "))
temp_f = c_to_f(temp_c)
print(f"{temp_c}°C is equal to {temp_f}°F")
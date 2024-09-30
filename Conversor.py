"""
TEMPERATURE CONVERSOR: CELSIUS - FARENHEIT
"""

temperature = float(input("Enter temperature:"))
scale = input("Is it Farenheit (ºF) or is it Celcius (ºC)?: ").lower()

if scale == "f":
    celsius = (temperature - 32) * 5/9
    print(celsius)
elif scale == "c":
    farenheit = (temperature * 1.8) + 32
    print(farenheit)
else:
    print("Wrong scale")

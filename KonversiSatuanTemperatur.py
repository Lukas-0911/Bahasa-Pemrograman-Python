# KONVERSI SATUAN TEMPERATUR

# konversi celcius ke satuan lain

print("\nKONVERSI TEMPERATUR\n")

celcius = float(input('Masukan suhu dalam celcius :'))
print("Suhu adalah :",celcius)

# Reamur
    # rumus 4/5 * C
reamur = (4/5) * celcius
print("suhu dalam reamur adalah :",reamur,"reamur")


# Fahrenheit
    # rumus 9/5 * c +32
fahrenheit = (9/5) * celcius +32
print("suhu dalam fahrenheit adalah :",fahrenheit,"fahrenheit")

#Kelvin
    # rumus celcius + 273
kelvin = celcius + 273
print("suhu dalam kelvin adalah :",kelvin,"kelvin")

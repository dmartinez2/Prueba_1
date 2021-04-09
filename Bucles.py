comida = ["manzana", "pan", "queso", "leche"]

# Parte una lista en valores sueltos
for food in comida:
    print(food)

# Parte una cadena de texto en fragmentos
for letter in "hello":
    print(letter)

count = 4
# Repite un bucle hasta que la condición deje de cumplirse, para ello tiene que haber una modificación, sino ppodría ser un bucle infinito
while count <= 10:
    print(count)
    count = count + 1
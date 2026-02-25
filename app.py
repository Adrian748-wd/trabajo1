nombre = input("Escriba su nombre: ")
apellido = input("Escriba su apellido: ")

edad_mayor = int(input("Edad del hermano mayor: "))
edad_menor = int(input("Edad del hermano menor: "))

diferencia = edad_mayor - edad_menor

# Usamos una coma para que Python agregue el espacio automáticamente
print("Nombre completo:", nombre, apellido)

# Eliminamos el símbolo '+' innecesario
print("Diferencia de edad:", diferencia, "años")

nombre = input("Escriba su nombre: ")
apellido = input("Escriba su apellido: ")

edad_mayor = int(input("Edad del hermano mayor: "))
edad_menor = int(input("Edad del hermano menor: "))

diferencia = edad_mayor - edad_menor

print("Nombre completo:", nombre, apellido)
print("Diferencia de edad:", diferencia, "años")
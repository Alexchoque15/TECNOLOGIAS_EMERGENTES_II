# input() siempre recibe los datos como texto (string).
nombre_usuario = input("Introduce tu nombre: ")
print("Hola " + nombre_usuario)

# SUMA:
# Para sumar números, debemos convertirlos con float() o int().
n1 = input("Ingresa el primer número: ")
n2 = input("Ingresa el segundo número: ")

# Si no convertimos, se concatenan (10 + 20 = 1020)
resultado = float(n1) + float(n2)
print("La suma correcta es:", resultado)
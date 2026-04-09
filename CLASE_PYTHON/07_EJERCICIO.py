#Nombre: ALEXANDER CHOQUE SIRPA
#Materia: TECNOLOGIAS EMERGENTES II
# Sistema de Reporte de Ventas

print("--- SISTEMA DE GESTIÓN DE INVENTARIO ---")

# 1. ENTRADA DE DATOS Y VARIABLES
# Pedimos al usuario los datos básicos de la venta.
# input() siempre devuelve texto, por eso usamos float() o int() para convertirlo a números.
producto = input("Ingrese el nombre del producto: ")
precio_unitario = float(input("Ingrese el precio por unidad: "))  # Convertimos el texto a número decimal
cantidad = int(input("Ingrese la cantidad vendida: "))            # Convertimos el texto a número entero

# Definimos el IVA como una constante del 16%
impuesto_porcentaje = 0.16

# 2. OPERACIONES MATEMÁTICAS
# Primero calculamos el subtotal multiplicando el precio por la cantidad vendida
subtotal = precio_unitario * cantidad

# Creamos una variable para el total final
total_con_iva = subtotal

# Usamos *= que es una forma corta de multiplicar el valor actual y guardarlo otra vez
# En este caso estamos agregando el IVA al subtotal
total_con_iva *= (1 + impuesto_porcentaje)

# 3. MANEJO DE TEXTO (STRINGS)
# Limpiamos el nombre del producto por si el usuario puso espacios al inicio o al final
# capitalize() hace que la primera letra quede en mayúscula
producto_reporte = producto.strip().capitalize()

# Convertimos todo a minúsculas para revisar si la palabra "oferta" aparece
# Así no importa si el usuario escribe Oferta, OFERTA o oferta
esta_en_oferta = "oferta" in producto.lower()

# 4. CONDICIONES LÓGICAS
# Si se venden más de 10 unidades, consideramos que es una venta mayorista
es_mayorista = cantidad > 10

# 5. REPORTE FINAL EN PANTALLA
# Usamos f-strings para mostrar los datos de forma clara dentro del texto fu
print("\n" + "="*40)  # Creamos una línea separadora para que el reporte se vea más ordenado
print("       RESUMEN DE VENTA (SISTEMA PYTHON)")
print("="*40)

print(f"Producto: {producto_reporte}")
print(f"Precio Base: ${precio_unitario}")
print(f"Cantidad: {cantidad}")
print(f"Subtotal: ${subtotal}")

# :.2f hace que el número se muestre solo con 2 decimales, como un precio real
print(f"Total con IVA (16%): ${total_con_iva:.2f}")

print("-" * 40)

print(f"¿Venta Mayorista?: {es_mayorista}")
print(f"¿Producto en Oferta?: {esta_en_oferta}")

print("="*40)
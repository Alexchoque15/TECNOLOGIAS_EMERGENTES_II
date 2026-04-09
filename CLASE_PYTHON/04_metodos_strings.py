# Las cadenas en Python son objetos con métodos útiles.
curso = "python para iniciantes"

print(curso.upper())        # Todo a MAYÚSCULAS
print(curso.lower())        # Todo a minúsculas
print(curso.capitalize())   # Primera letra en mayúscula
print(curso.find("p"))      # Busca la posición (índice)
print(curso.replace("python", "Código")) # Reemplaza texto

# Operador 'in' para buscar subcadenas (Sensible a mayúsculas)
print("python" in curso)    # Devuelve True o False
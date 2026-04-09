# Curso de Python: Fundamentos y Entorno de Desarrollo

Este repositorio contiene la guía práctica y el código base del inicio en el lenguaje **Python**. El objetivo es establecer un entorno de desarrollo profesional y dominar los conceptos básicos de sintaxis, tipos de datos y operaciones fundamentales.

------------------------------------------------------------------------------------------------------------------------

## Configuración del Entorno

### 1. Instalación de Python
Se utilizó la versión **3.12.x**. Puntos críticos durante la instalación en Windows:
* **PATH:** Activación de `Add python.exe to PATH` para ejecución global en terminal.
* **Privilegios:** Uso de privilegios de administrador para la instalación.
* **MAX_PATH:** Deshabilitar el límite de 260 caracteres para evitar errores en directorios profundos.

### 2. IDE y Extensiones (Visual Studio Code)
Para un flujo de trabajo eficiente, se configuró **VS Code** con:
* **Extensiones:** `Python (Microsoft)`, `Python Indent` (identación automática) y un formateador de código.
* **Configuraciones clave:**
  * `Auto Save`: Configurado en `onFocusChange`.
  * `Font Size`: Ajustado a `18pt` para legibilidad.
  * `Zoom`: Uso de `Ctrl +` / `Ctrl -`.

------------------------------------------------------------------------------------------------------------------------

## Contenido del Curso

### Fundamentos de Programación
* **Salida de Datos:** Uso de la función `print()` y concatenación avanzada.
* **Entrada de Datos:** Uso de `input()` y transformación de tipos (*Casting*).
* **Variables y Tipos:**
  * `int`: Números enteros.
  * `float`: Números de punto flotante.
  * `str`: Cadenas de texto.
  * `bool`: Valores lógicos (`True`/`False`).

### Operadores Aritméticos
| Operación        | Operador  | Ejemplo         |
| :---             | :---:     | :---            |
| Suma / Resta     | `+` / `-` | `10 + 5`        |
| Multiplicación   | `*`       | `10 * 3`        |
| División (Float) | `/`       | `10 / 3` (3.33) |
| División Entera  | `//`      | `10 // 3` (3)   |
| Módulo (Residuo) | `%`       | `10 % 3` (1)    |
| Exponenciación   | `**`      | `2 ** 4` (16)   |

### Manipulación de Strings (Objetos)
En Python, los strings son objetos con métodos integrados:
* `.upper()` / `.lower()`: Cambio de caja.
* `.capitalize()`: Formato de oración.
* `.find()`: Búsqueda de índices.
* `.replace()`: Sustitución de subcadenas.
* `in`: Operador de pertenencia (Case-sensitive).


# Aplicaciones Web con Flask y Jinja2 

Clase desarrollada para comprender el uso de **Jinja2** en aplicaciones web con **Flask**, incluyendo conceptos fundamentales como renderizado de plantillas, formularios, control de flujo y herencia de vistas.

---

## Objetivo del Proyecto

El objetivo principal es aprender cómo funciona el motor de plantillas **Jinja2** dentro de Flask, permitiendo separar la lógica del backend (Python) de la presentación (HTML).

Este proyecto incluye:

*  Uso de variables dinámicas (`{{ }}`)
*  Control de flujo (`{% if %}`, `{% for %}`)
*  Formularios HTML con método POST
*  Renderización de datos desde Flask
*  Herencia de plantillas (estructura reutilizable)
*  Organización profesional del código

---

## ¿Qué es Jinja2?

**Jinja2** es un motor de plantillas para Python que permite generar HTML dinámico de forma sencilla.

Se utiliza principalmente con Flask para:

* Insertar datos dinámicos en HTML
* Crear estructuras reutilizables
* Aplicar lógica directamente en las vistas
* Mantener el código limpio y organizado

Ejemplo básico:

```html
<h1>Hola, {{ nombre }}</h1>
```

---

## Descripción de Carpetas

### `/avance`

Contiene la implementación de **herencia de plantillas con Jinja2**.

* `base.html`: plantilla base reutilizable
* `home.html`: página que extiende la plantilla base

 Permite entender cómo estructurar aplicaciones grandes de forma ordenada.

---

###  `/ejercicio1` – Formulario Básico

Aplicación que:

* Solicita el nombre del usuario
* Envía datos mediante POST
* Muestra el resultado dinámicamente

Tecnologías usadas:

* Flask
* HTML
* Jinja2

---

###  `/ejercicio2` – Encuesta

Aplicación más completa que incluye:

* Formulario con múltiples campos
* Select (lenguaje de programación)
* Radio buttons (nivel de experiencia)
* Visualización de resultados

Refuerza el uso de formularios y renderización dinámica.

---

## Conceptos

*  Renderización de plantillas con `render_template`
*  Envío de datos con formularios HTML
*  Uso de `request.form`
*  Variables dinámicas en Jinja2
*  Estructuras condicionales y repetitivas
*  Herencia de plantillas (`extends`, `block`)

---

## Conclusión

Esta clase aprendimos a comprender de forma práctica cómo funcionan las aplicaciones web en Flask utilizando Jinja2, estableciendo una base sólida para el desarrollo de sistemas web más complejos.

---

# Aplicaciones Web con Flask y Jinja2

Clase desarrollada para comprender el uso de **Jinja2** en aplicaciones web con **Flask**, incluyendo conceptos fundamentales como renderizado de plantillas, formularios, control de flujo y herencia de vistas.

---

## ▸ Objetivo del Proyecto

El objetivo principal es aprender cómo funciona el motor de plantillas **Jinja2** dentro de Flask, permitiendo separar la lógica del backend (Python) de la presentación (HTML).

Este proyecto incluye:

* Uso de variables dinámicas (`{{ }}`)
* Control de flujo (`{% if %}`, `{% for %}`)
* Formularios HTML con método POST
* Renderización de datos desde Flask
* Herencia de plantillas (estructura reutilizable)
* Organización profesional del código

---

## ▸ ¿Qué es Jinja2?

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

## ▸ Descripción de Carpetas

### avance

Contiene la implementación de **herencia de plantillas con Jinja2**.

* `base.html`: plantilla base reutilizable
* `home.html`: página que extiende la plantilla base

Permite entender cómo estructurar aplicaciones grandes de forma ordenada.

---

### ejercicio1

Aplicación que:

* Solicita el nombre del usuario
* Envía datos mediante POST
* Muestra el resultado dinámicamente

Tecnologías usadas:

* Flask
* HTML
* Jinja2

---

### ejercicio2

Aplicación más completa que incluye:

* Formulario con múltiples campos
* Select (lenguaje de programación)
* Radio buttons (nivel de experiencia)
* Visualización de resultados

Refuerza el uso de formularios y renderización dinámica.

---

## ▸ mini_web_encuesta

Aplicación moderna desarrollada con **Flask + Jinja2** que implementa un sistema de encuestas con visualización de datos en un dashboard.

### Características principales

* Interfaz tipo dashboard con navegación lateral
* Formulario dinámico de encuesta
* Visualización de resultados en tiempo real
* Barras de progreso por lenguaje
* Listado de usuarios registrados
* Diseño limpio y estructurado con CSS moderno
* Preparado para despliegue en Render

---

### Funcionalidades

La aplicación permite:

1. Registrar usuarios mediante una encuesta
2. Seleccionar lenguaje de programación favorito
3. Indicar nivel de experiencia
4. Visualizar estadísticas dinámicas
5. Analizar resultados en un dashboard

---

### Vista del Dashboard

Incluye:

* Total de respuestas
* Conteo por lenguaje
* Barras proporcionales
* Lista de usuarios con sus respuestas

---

### Tecnologías usadas

* Flask
* Jinja2
* HTML5
* CSS3
* Gunicorn

---

---

### Deploy

Este proyecto está preparado para desplegarse en:

* Render

Incluye:

* `requirements.txt`
* `Procfile`
* Configuración lista para producción

---

## ▸ Conceptos Aplicados

* Renderización de plantillas con `render_template`
* Envío de datos con formularios HTML
* Uso de `request.form`
* Variables dinámicas en Jinja2
* Estructuras condicionales y repetitivas
* Herencia de plantillas (`extends`, `block`)
* Separación backend/frontend
* Diseño de interfaces web modernas

---

## ▸ Conclusión

En esta clase se desarrolló una comprensión práctica de cómo funcionan las aplicaciones web en Flask utilizando Jinja2.

Se evolucionó desde ejemplos básicos hasta una aplicación con estructura tipo dashboard, sentando bases sólidas para el desarrollo de sistemas web más completos y organizados.

---

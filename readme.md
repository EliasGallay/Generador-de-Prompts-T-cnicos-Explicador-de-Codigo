# 🧩 Prompt Engineering para Programadores

## 📘 Descripción general
Este proyecto fue desarrollado como entrega final del curso **Prompt Engineering para Programadores (Coderhouse)**.  
Consiste en una aplicación web interactiva creada con **Streamlit**, orientada a mejorar el flujo de trabajo de desarrolladores mediante el uso de **prompts con salida dirigida**.

---

## 🎯 Objetivo
Brindar una herramienta práctica que permita:
1. **Generar prompts técnicos optimizados** para ChatGPT, Copilot u otros modelos de IA.
2. **Explicar código automáticamente** mediante prompts estructurados.
3. **Guardar y reutilizar** las generaciones dentro de un historial local.

El enfoque principal es aplicar los principios del **prompt engineering** a casos reales de desarrollo de software, con formato claro, reutilizable y profesional.

---

## 🧠 Módulos principales

### 🏗️ Generador de Prompts Técnicos
Permite ingresar una tarea técnica (por ejemplo: *“crear un endpoint REST en Express con validaciones y tests”*) y genera un prompt optimizado con estructura de salida dirigida.

**Características:**
- Campos dinámicos (lenguaje, stack, tono, restricciones, formato de salida).  
- Ejemplos predefinidos de uso rápido.  
- Descarga del prompt como archivo `.md`.  
- Persistencia automática en el historial.

---

### 🧩 Explicador de Código
Permite pegar un fragmento de código y generar un prompt que solicita su explicación estructurada (línea por línea, buenas prácticas, refactor, etc.).

**Características:**
- Selección de lenguaje (JS, Python, Java, SQL, etc.).  
- Personalización de los puntos de análisis.  
- Descarga en formato `.md`.  
- Guarda cada explicación generada en el historial local.

---

### 🗂️ Historial
Sección donde se almacenan todos los prompts y explicaciones generadas.

**Funciones:**
- Visualización de cada prompt en formato Markdown.  
- Descarga individual.  
- Filtro por tipo (Generador / Explicador).  
- Persistencia local en `data/history.json`.

---

## 🛠️ Tecnologías utilizadas

| Tecnología | Uso |
|-------------|-----|
| **Python 3.11+** | Lenguaje base |
| **Streamlit** | Framework para interfaz web |
| **JSON / pathlib** | Almacenamiento local |
| **Datetime / importlib** | Manejo de rutas y metadatos |
| **Markdown** | Exportación de prompts |

---

## 📂 Estructura del proyecto

# Generador-de-Prompts-T-cnicos-Explicador-de-Codigo
# Generador-de-Prompts-T-cnicos-Explicador-de-Codigo
# Generador-de-Prompts-T-cnicos-Explicador-de-Codigo

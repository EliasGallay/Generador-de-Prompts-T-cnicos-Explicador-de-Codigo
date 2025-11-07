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

* Campos dinámicos (lenguaje, stack, tono, restricciones, formato de salida).
* Ejemplos predefinidos de uso rápido.
* Descarga del prompt como archivo `.md`.
* Persistencia automática en el historial.

---

### 🧩 Explicador de Código

Permite pegar un fragmento de código y generar un prompt que solicita su explicación estructurada (línea por línea, buenas prácticas, refactor, etc.).

**Características:**

* Selección de lenguaje (JS, Python, Java, SQL, etc.).
* Personalización de los puntos de análisis.
* Descarga en formato `.md`.
* Guarda cada explicación generada en el historial local.

---

### 🗂️ Historial

Sección donde se almacenan todos los prompts y explicaciones generadas.

**Funciones:**

* Visualización de cada prompt en formato Markdown.
* Descarga individual.
* Filtro por tipo (Generador / Explicador).
* Persistencia local en `data/history.json`.

---

## 🛠️ Tecnologías utilizadas

| Tecnología               | Uso                         |
| ------------------------ | --------------------------- |
| **Python 3.11+**         | Lenguaje base               |
| **Streamlit**            | Framework para interfaz web |
| **JSON / pathlib**       | Almacenamiento local        |
| **Datetime / importlib** | Manejo de rutas y metadatos |
| **Markdown**             | Exportación de prompts      |

---

## 📂 Estructura del proyecto

```
PROMPT/
├── app/
│   ├── components/
│   ├── pages/
│   │   ├── 1_Generador_de_Prompts.py
│   │   ├── 2_Explicador_de_Código.py
│   │   ├── 3_Historial.py
│   ├── prompts/
│   │   └── templates.py
│   ├── utils/
│   │   ├── streamlit_app.py
│   │   ├── storage.py
│   │   └── costs.py
│   └── services/
└── data/
    └── history.json
```

---

## 🚀 Ejecución del proyecto

### 1️⃣ Instalar dependencias

```bash
pip install streamlit
```

### 2️⃣ Ejecutar la app

Desde la carpeta raíz del proyecto:

```bash
streamlit run app/streamlit_app.py
```

La aplicación estará disponible en:
👉 [http://localhost:8501](http://localhost:8501)

---

## 🧩 Ejemplo de uso

### **Entrada:**

```
Crear un endpoint REST en Express para /users con validaciones, paginación y tests Jest.
```

### **Salida generada:**

```markdown
# Prompt técnico – ChatGPT
_Generado: 2025-11-06_

**Actuá como** un desarrollador senior.

## Tarea
"Crear un endpoint REST en Express para /users con validaciones, paginación y tests Jest."

## Formato de salida
1) Resumen  
2) Pasos detallados  
3) Código  
4) Pruebas / casos  
5) Riesgos y mitigaciones
```

---

### **Explicador de Código**

**Entrada:**

```js
function getAverage(nums) {
  let sum = 0;
  for (let i = 0; i < nums.length; i++) {
    sum += nums[i];
  }
  return sum / nums.length;
}
```

**Salida generada:**

````markdown
# Explicador de Código – JavaScript
_Generado: 2025-11-06_

## Código a analizar
```js
function getAverage(nums) { ... }
````

## Formato de salida

* Explicación línea por línea
* Buenas prácticas y estilo
* Posibles errores o mejoras
* Recomendaciones de refactorización

````

---

## 📊 Estimación de costos IA

El módulo `utils/costs.py` permite estimar el costo aproximado en USD según tokens generados para distintos modelos (ej. GPT-4o-mini).

```python
from app.utils.costs import estimate_cost
estimate_cost(prompt_chars=1500, completion_chars=2500)
# {'model': 'gpt-4o-mini', 'tokens_in': 375, 'tokens_out': 625, 'usd': 0.0005}
````

---

## ✅ Conclusiones

Se desarrolló una aplicación web funcional con Streamlit y salida dirigida, cumpliendo todos los criterios del proyecto.
✅ Permite generar prompts de alta calidad para tareas técnicas.
✅ Facilita la explicación estructurada de código con IA.
✅ Integra persistencia local, exportación y estimación de costos.

### **Aprendizajes principales:**

* Diseño de prompts efectivos y modulares.
* Integración de IA en flujos reales de desarrollo.
* Implementación práctica de interfaces con Streamlit.

---

## 👤 Autor

**Elias Gallay**
📧 [eliasmgallay@gmail.com]
💼 [GitHub – EliasGallay](https://github.com/EliasGallay)

---

## 🧠 Licencia
Proyecto educativo – Coderhouse 2025

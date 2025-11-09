#  Prompt Engineering para Programadores

##  Descripción general

Este proyecto fue desarrollado como entrega final del curso **Prompt Engineering para Programadores (Coderhouse)**.  
Consiste en una aplicación web interactiva creada con **Streamlit**, orientada a mejorar el flujo de trabajo de desarrolladores mediante el uso de **prompts con salida dirigida** e integración de **modelos de IA (Gemini)**.

---

##  Objetivo

Brindar una herramienta práctica que permita:

1. **Generar prompts técnicos optimizados** para ChatGPT, Copilot u otros modelos.
2. **Explicar código automáticamente** mediante prompts estructurados y claros.
3. **Guardar, filtrar y reutilizar** todas las generaciones en un historial local.
4. **Optimizar los prompts generados** automáticamente con el modelo **Gemini**.

El enfoque principal es aplicar los principios del **prompt engineering** en escenarios reales de desarrollo, integrando herramientas modernas y salida dirigida.

---

##  Módulos principales

###  Generador de Prompts Técnicos

Permite ingresar una tarea técnica (por ejemplo: *“crear un endpoint REST en Express con validaciones y tests”*) y genera un prompt optimizado con estructura de salida dirigida.

**características:**

- Campos dinámicos (lenguaje, stack, tono, restricciones, formato de salida).
- Ejemplos predefinidos con autocompletado.
- Botón adicional **“Generar + Optimizar con IA (Gemini)”**.
- Descarga automática del prompt como `.md`.
- Persistencia automática en el historial local (`data/history.json`).

---

### 🧩 Explicador de Código

Permite pegar un fragmento de código y obtener una explicación técnica completa, generada y mejorada con **Gemini**.

**Características:**

- Detección de lenguaje y nivel de detalle (básico, intermedio, avanzado).
- Explicación detallada paso a paso.
- Identificación de errores, sugerencias y buenas prácticas.
- Descarga en formato `.md`.
- Registro automático en el historial.

---

###  Historial

Centraliza todos los prompts y explicaciones generadas.

**Funciones:**

- Visualización en formato Markdown.
- Filtro por tipo: Generador / Explicador / Todos.
- Descarga individual de cada ítem.
- Persistencia local (no se sube al remoto gracias al `.gitignore`).

---

## 🔧 Estructura del proyecto

```
PROMPT/
├── app/
│   ├── pages/
│   │   ├── 1_Generador_de_Prompts.py
│   │   ├── 2_Explicador_de_Código.py
│   │   └── 3_Historial.py
│   ├── prompts/
│   │   └── templates.py
│   ├── services/
│   │   └── llm_gemini.py
│   ├── utils/
│   │   ├── streamlit_app.py
│   │   ├── storage.py
│   │   └── costs.py
│   └── data/
│       └── history.json  # Ignorado por Git
└── .env  # API Key de Gemini (no versionado)

````

---

## Integración con Gemini

El proyecto incluye conexión directa con **Google Gemini** a través del módulo:

```python
from app.services.llm_gemini import generate_response
````
Este servicio se usa tanto para:

* Mejorar prompts generados (“Optimizar con IA”).
* Generar explicaciones técnicas detalladas.

###  Seguridad

La API key de Gemini se almacena en `.env`:

```
GEMINI_API_KEY=tu_clave_aqui
```

---

##  Ejecución del proyecto

###  Instalar dependencias

```bash
pip install -r requirements.txt
```

O, si no tenés el archivo:

```bash
pip install streamlit google-generativeai python-dotenv
```

###  Ejecutar la app

Desde la carpeta raíz:

```bash
streamlit run app/streamlit_app.py
```

La aplicación estará disponible en:
👉 [http://localhost:8501](http://localhost:8501)

---

##  Ejemplo de uso

### Entrada:

```
Crear un endpoint REST en Express para /users con validaciones, paginación y tests Jest.
```

### Prompt generado:

```markdown
# Prompt técnico – ChatGPT
_Generado: 2025-11-09_

**Actuá como** un desarrollador senior especializado en backend.

## Tarea
"Crear un endpoint REST en Express para /users con validaciones, paginación y tests Jest."

## Formato de salida
1) Resumen  
2) Pasos detallados  
3) Código  
4) Pruebas / casos  
5) Riesgos y mitigaciones
```


##  Estimación de costos IA

Incluye un módulo de cálculo aproximado del costo por tokens:

```python
from app.utils.costs import estimate_cost
estimate_cost(prompt_chars=1500, completion_chars=2500)
# {'model': 'gpt-4o-mini', 'tokens_in': 375, 'tokens_out': 625, 'usd': 0.0005}
```

---

## 👤 Autor

**Elias Gallay**
📧 [[eliasmgallay@gmail.com](mailto:eliasmgallay@gmail.com)]
💼 [GitHub – EliasGallay](https://github.com/EliasGallay)

---

##  Licencia

Proyecto educativo – Coderhouse 2025
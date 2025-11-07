# utils/streamlit_app.py
from pathlib import Path
import sys
import importlib
import streamlit as st

# --- PATHING: permitir imports tipo app.pages.XXX aunque ejecutes desde raíz ---
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

st.set_page_config(
    page_title="Prompt Engineering para Programadores",
    page_icon="🧩",
    layout="wide",
)

# --- Tema visual ---
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
            color: #f1f5f9;
        }
        h1, h2, h3, h4, h5 {
            color: #38bdf8;
        }
        .stButton>button {
            background-color: #0284c7 !important;
            color: white !important;
            border: none !important;
            border-radius: 6px !important;
        }
        .stButton>button:hover {
            background-color: #0369a1 !important;
        }
    </style>
""", unsafe_allow_html=True)


# --- Sidebar / navegación ---
PAGES = {
    "🏗️ Generador de Prompts Técnicos": "app.pages.1_Generador_de_Prompts",
    "🧠 Explicador de Código": "app.pages.2_Explicador_de_Código",
    "🗂️ Historial": "app.pages.3_Historial",  # <-- nuevo
}


with st.sidebar:
    st.markdown("## 🔧 Módulos")
    choice = st.radio(
        "Elegí una herramienta",
        list(PAGES.keys()),
        label_visibility="collapsed",
    )
    st.markdown("---")
    st.caption("Proyecto Final • Coderhouse • Streamlit + Prompt Engineering")

st.title("🧩 Prompt Engineering para Programadores")
st.write(
    "Esta aplicación incluye herramientas con **salida dirigida** para acelerar tareas técnicas: "
    "generación de prompts optimizados y explicación de código."
)

# --- Cargar y renderizar la página seleccionada ---
module_path = PAGES[choice]
try:
    mod = importlib.import_module(module_path)
except ModuleNotFoundError as e:
    st.error(f"No pude importar el módulo `{module_path}`.\n\nDetalle: {e}")
else:
    render = getattr(mod, "render", None)
    if callable(render):
        render()
    else:
        st.info(
            "El módulo seleccionado no expone una función `render()`. "
            "Agregala para que esta página se muestre."
        )

# --- Footer simple ---
st.markdown(
    """
    <hr style="margin-top:3rem;margin-bottom:1rem;opacity:.2">
    <div style="display:flex;justify-content:space-between;opacity:.7;font-size:.9rem">
      <span>Hecho con Streamlit</span>
      <span>© 2025</span>
    </div>
    """,
    unsafe_allow_html=True,
)

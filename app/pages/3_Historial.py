# app/pages/3_Historial.py
import streamlit as st
from app.utils.storage import list_items

def render():
    st.subheader("🗂️ Historial")
    st.caption("Tus prompts y explicaciones generadas, listos para reusar o descargar.")

    filtro = st.segmented_control("Filtrar por", options=["Todos","Generador","Explicador"], default="Todos")
    kind = "all" if filtro == "Todos" else ("generator" if filtro == "Generador" else "explainer")

    items = list_items(kind=kind)
    if not items:
        st.info("Aún no hay elementos en el historial.")
        return

    for it in items:
        with st.expander(f"{it['title']} · {it['created_at']}"):
            st.code(it["content"], language="markdown")
            st.download_button(
                "Descargar .md",
                data=it["content"].encode("utf-8"),
                file_name=f"{it['title'].replace(' ','_')}.md",
                mime="text/markdown",
                use_container_width=True,
            )

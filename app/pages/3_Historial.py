import streamlit as st
from app.utils.storage import list_items, delete_item, clear_items  # ⬅️ NUEVO

def render():
    st.subheader("🗂️ Historial")
    st.caption("Tus prompts y explicaciones generadas, listos para reusar o descargar.")

    top_cols = st.columns([3, 1])
    with top_cols[0]:
        filtro = st.segmented_control("Filtrar por", options=["Todos", "Generador", "Explicador"], default="Todos")
    with top_cols[1]:
        with st.popover("🗑️ Borrar todo"):
            st.write("Esta acción eliminará definitivamente los elementos del historial.")
            kind_for_clear = (
                "all" if filtro == "Todos" else ("generator" if filtro == "Generador" else "explainer")
            )
            if st.button(f"Confirmar borrar {filtro.lower()}", type="primary", use_container_width=True):
                count = clear_items(kind=kind_for_clear)
                st.success(f"Se eliminaron {count} elemento(s).")
                st.rerun()

    kind = "all" if filtro == "Todos" else ("generator" if filtro == "Generador" else "explainer")
    items = list_items(kind=kind)
    if not items:
        st.info("Aún no hay elementos en el historial.")
        return

    for idx, it in enumerate(items):
        header = f"{it.get('title','(sin título)')} · {it.get('created_at','')}"
        with st.expander(header):
            st.code(it.get("content",""), language="markdown")

            cols = st.columns([1, 1])
            with cols[0]:
                st.download_button(
                    label="Descargar .md",
                    data=(it.get("content","")).encode("utf-8"),
                    file_name=f"{it.get('title','item').replace(' ','_')}.md",
                    mime="text/markdown",
                    use_container_width=True,
                    key=f"dl_{it.get('id', idx)}", 
                )
            with cols[1]:
                if st.button("Eliminar este ítem", use_container_width=True, key=f"rm_{it.get('id', idx)}"):
                    deleted = delete_item(it.get("id")) 
                    if deleted:
                        st.success("Ítem eliminado.")
                    else:
                        st.warning("No se pudo eliminar el ítem.")
                    st.rerun()

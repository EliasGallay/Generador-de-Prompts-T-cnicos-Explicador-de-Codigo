import streamlit as st
from app.prompts.templates import build_technical_prompt
from app.utils.storage import add_item
from app.services.llm_gemini import generate_response


def render():
    st.subheader("🏗️ Generador de Prompts Técnicos")
    st.caption("Ingresá una tarea técnica y obtené un prompt optimizado listo para usar.")

    # --- Ejemplos predefinidos ---
    st.markdown("### Ejemplos rápidos")
    ejemplos = {
        "API REST en Express": "Crear un endpoint REST en Express para /users con validaciones, paginación y tests Jest.",
        "Test unitario Jest": "Escribir un test unitario para una función que calcula el total de un carrito de compras.",
        "Query SQL optimizada": "Optimizar una consulta SQL que obtiene usuarios activos con más de 3 pedidos completados.",
        "Script Python ETL": "Crear un script Python que lea un CSV, filtre datos y los exporte en JSON normalizado.",
    }

    cols = st.columns(len(ejemplos))
    for i, (titulo, tarea_ejemplo) in enumerate(ejemplos.items()):
        if cols[i].button(titulo):
            st.session_state["tarea"] = tarea_ejemplo

    with st.form("form_prompt"):
        tarea = st.text_area(
            "¿Qué necesitás hacer?",
            value=st.session_state.get("tarea", ""),
            placeholder="Ej: Crear un endpoint REST en Express para /users con validaciones, paginación y tests…",
            height=160,
        )

        col1, col2 = st.columns(2)
        with col1:
            destino = st.selectbox("Destino", ["ChatGPT", "GitHub Copilot", "Claude", "Otro"])
            lenguaje = st.selectbox(
                "Lenguaje principal",
                ["(no especificar)", "JavaScript/TypeScript", "Python", "Java", "SQL", "Go", "Otro"],
            )
            if lenguaje == "(no especificar)":
                lenguaje = None
        with col2:
            stack = st.multiselect(
                "Stack/Frameworks (opcional)",
                [
                    "Node.js", "Express", "FastAPI", "Django", "React", "Next.js", "NestJS",
                    "PostgreSQL", "MongoDB", "Docker", "PyTest", "Jest",
                ],
            )
            tono = st.selectbox("Tono (opcional)", ["", "didáctico", "conciso", "paso a paso", "estricto"])

        contexto = st.text_area(
            "Contexto (opcional)",
            placeholder="Ej: Proyecto monorepo, CI con GitHub Actions, deploy en Railway…",
            height=100,
        )

        restricciones = st.text_area(
            "Restricciones (opcional, una por línea)",
            placeholder="Ej:\n- No usar librerías externas\n- Mantener compatibilidad con Node 18\n- Evitar ORM; usar SQL puro",
            height=100,
        )

        salida = st.text_area(
            "Formato de salida (opcional, una por línea)",
            placeholder="Ej:\n1) Resumen\n2) Pasos\n3) Código\n4) Tests\n5) Riesgos y mitigaciones",
            height=100,
        )

        col_a, col_b = st.columns(2)
        submit = col_a.form_submit_button("Generar prompt", use_container_width=True, type="primary")
        submit_ai = col_b.form_submit_button("Generar + Optimizar con IA (Gemini)", use_container_width=True)

    if submit or submit_ai:
        if not tarea.strip():
            st.warning("Ingresá una tarea para generar el prompt.")
            return

        restricciones_list = [
            l.strip("- ").strip()
            for l in (restricciones.splitlines() if restricciones else [])
            if l.strip()
        ]
        salida_list = [
            l.strip()
            for l in (salida.splitlines() if salida else [])
            if l.strip()
        ]

        prompt = build_technical_prompt(
            tarea=tarea,
            destino=destino,
            lenguaje=lenguaje,
            stack=stack,
            contexto=contexto,
            restricciones=restricciones_list or None,
            salida=salida_list or None,
            tono=tono or None,
        )

        st.success("Prompt generado.")
        add_item(
            kind="generator",
            title=f"Prompt técnico – {destino}",
            content=prompt,
            meta={"destino": destino, "lenguaje": lenguaje, "stack": stack},
        )
        st.code(prompt, language="markdown")
        st.download_button(
            label="Descargar como .md",
            data=prompt.encode("utf-8"),
            file_name="prompt_tecnico.md",
            mime="text/markdown",
            use_container_width=True,
        )

        # Si el usuario eligió la opción con IA, devolvemos también la versión mejorada
        if submit_ai:
            system = (
                "Actuás como un experto en prompt engineering para programadores. "
                "Revisá y mejorá el prompt para hacerlo claro, estructurado y accionable. "
                "Mantené el tono indicado y sugerí placeholders si falta info."
            )
            try:
                with st.spinner("Optimizando con Gemini…"):
                    improved = generate_response(system, prompt)
                st.text_area("Prompt mejorado por Gemini", value=improved, height=240)
                st.download_button(
                    label="Descargar mejora como .md",
                    data=improved.encode("utf-8"),
                    file_name="prompt_tecnico_mejorado.md",
                    mime="text/markdown",
                    use_container_width=True,
                )
            except Exception as e:
                st.error(f"Ocurrió un error al llamar a Gemini: {e}")

        with st.expander("✨ Mejorar con IA (Gemini)"):
            if st.button("Optimizar prompt con IA", use_container_width=True, key="opt_after"):
                system = (
                    "Actuás como un experto en prompt engineering para programadores. "
                    "Revisá y mejorá el prompt para hacerlo claro, estructurado y accionable. "
                    "Mantené el tono indicado y sugerí placeholders si falta info."
                )
                try:
                    with st.spinner("Generando mejora con Gemini…"):
                        improved2 = generate_response(system, prompt)
                    st.text_area("Prompt mejorado por Gemini", value=improved2, height=240, key="improved2")
                    st.download_button(
                        label="Descargar mejora como .md",
                        data=improved2.encode("utf-8"),
                        file_name="prompt_tecnico_mejorado.md",
                        mime="text/markdown",
                        use_container_width=True,
                    )
                except Exception as e:
                    st.error(f"Ocurrió un error al llamar a Gemini: {e}")

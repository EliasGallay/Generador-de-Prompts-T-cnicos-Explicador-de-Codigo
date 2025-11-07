# app/pages/2_Explicador_de_Código.py
import streamlit as st
from datetime import datetime
from app.utils.storage import add_item


def build_code_explainer_prompt(code: str, language: str, focus: list[str] | None = None) -> str:
    """
    Construye un prompt para explicar y analizar código con salida dirigida.
    """
    focus = focus or [
        "1) Explicación línea por línea",
        "2) Buenas prácticas y estilo",
        "3) Posibles errores o mejoras",
        "4) Recomendaciones de refactorización",
        "5) Ejemplo de versión optimizada (si aplica)",
    ]

    header = f"# Explicador de Código – {language}\n_Generado: {datetime.now().strftime('%Y-%m-%d %H:%M')}_\n\n"
    rol = "Actuá como un revisor técnico experto y mentor de código.\n"
    code_block = f"## Código a analizar\n```{language.lower()}\n{code.strip()}\n```\n\n"
    salida_block = "## Formato de salida (obligatorio)\n" + "\n".join([f"- {s}" for s in focus]) + "\n\n"

    return header + rol + code_block + salida_block + (
        "## Instrucción final\n"
        "Proporcioná una explicación detallada y estructurada. "
        "Si detectás problemas, proponé alternativas justificadas con ejemplos.\n"
    )


def render():
    st.subheader("🧠 Explicador de Código")
    st.caption("Pegá un fragmento de código y obtené una explicación técnica estructurada.")

    with st.form("form_code_explainer"):
        lang = st.selectbox(
            "Lenguaje principal",
            ["JavaScript/TypeScript", "Python", "Java", "C#", "SQL", "Otro"],
            index=0,
        )
        code = st.text_area(
            "Código",
            placeholder="Pegá acá tu código…",
            height=240,
        )
        focus_text = st.text_area(
            "Aspectos a analizar (opcional, una por línea)",
            placeholder="Ej:\n1) Explicación línea por línea\n2) Buenas prácticas\n3) Optimización de performance\n4) Legibilidad\n5) Recomendaciones",
            height=100,
        )

        submit = st.form_submit_button("Generar explicación", type="primary", use_container_width=True)

    if submit:
        if not code.strip():
            st.warning("Pegá un fragmento de código para analizar.")
            return

        focus = [f.strip() for f in focus_text.splitlines() if f.strip()] or None
        prompt = build_code_explainer_prompt(code, lang, focus)

        st.success("Prompt de explicación generado.")

        add_item(
            kind="explainer",
            title=f"Explicador de Código – {lang}",
            content=prompt,
            meta={"lenguaje": lang},
        )

        st.code(prompt, language="markdown")

        st.download_button(
            label="Descargar como .md",
            data=prompt.encode("utf-8"),
            file_name="explicador_codigo.md",
            mime="text/markdown",
            use_container_width=True,
        )

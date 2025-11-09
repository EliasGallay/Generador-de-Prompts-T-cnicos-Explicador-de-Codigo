import streamlit as st
from app.services.llm_gemini import generate_response
from app.utils.costs import estimate_cost

def render():
    st.subheader(" Explicador de Código con IA")
    st.caption("Pegá un fragmento de código y obtené una explicación generada con Gemini.")

    codigo = st.text_area(
        "Tu código",
        placeholder="Pegá aquí el código fuente que querés explicar...",
        height=200,
    )

    col1, col2 = st.columns([1, 1])
    with col1:
        lenguaje = st.selectbox("Lenguaje", ["(auto)", "Python", "JavaScript", "Java", "C#", "SQL", "Go", "Otro"])
    with col2:
        nivel = st.selectbox("Nivel de detalle", ["básico", "intermedio", "avanzado"])

    if st.button("✨ Explicar con IA", use_container_width=True, type="primary"):
        if not codigo.strip():
            st.warning("Pegá un fragmento de código primero.")
            return

        # Prompt para Gemini
        system = (
            "Actuás como un experto en programación y docente técnico. "
            "Tu tarea es analizar y explicar código fuente con claridad y precisión."
        )
        prompt = (
            f"Explicá el siguiente código en {lenguaje or 'lenguaje detectado automáticamente'} "
            f"de forma {nivel}. Incluí:\n"
            "- Qué hace el código\n"
            "- Explicación paso a paso (si aplica)\n"
            "- Posibles errores o mejoras\n"
            "- Buenas prácticas sugeridas\n\n"
            f"CÓDIGO:\n```{lenguaje}\n{codigo}\n```"
        )

        try:
            with st.spinner("Analizando código con Gemini…"):
                explicacion = generate_response(system, prompt)

            st.text_area(" Explicación generada por Gemini", value=explicacion, height=300)
            st.download_button(
                label="Descargar explicación.md",
                data=explicacion.encode("utf-8"),
                file_name="explicacion_codigo.md",
                mime="text/markdown",
                use_container_width=True,
            )

            # Costo estimado usando el tamaño real del prompt + salida
            cost_info = estimate_cost(prompt_chars=len(prompt), completion_chars=len(explicacion))
            st.caption(
                f"💰 **Costo estimado:** {cost_info['usd']:.4f} USD · "
                f"({cost_info['tokens_in']} ⬆️ / {cost_info['tokens_out']} ⬇️ tokens · modelo {cost_info['model']})"
            )

        except Exception as e:
            st.error(f"Ocurrió un error al llamar a Gemini: {e}")

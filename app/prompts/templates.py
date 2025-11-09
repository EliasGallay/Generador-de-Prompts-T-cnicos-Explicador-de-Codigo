from datetime import datetime

def build_technical_prompt(
    tarea: str,
    destino: str = "ChatGPT",
    lenguaje: str | None = None,
    stack: list[str] | None = None,
    contexto: str | None = None,
    restricciones: list[str] | None = None,
    salida: list[str] | None = None,
    tono: str | None = None,
) -> str:
    """
    Genera un prompt técnico con salida dirigida.
    Retorna un string listo para pegar en {destino}.
    """
    stack = stack or []
    restricciones = restricciones or []
    salida = salida or [
        "1) Resumen de la solución",
        "2) Pasos detallados",
        "3) Código autocontenido",
        "4) Pruebas / casos",
        "5) Riesgos y mitigaciones",
    ]

    header = f"# Prompt técnico – {destino}\n"
    meta = f"_Generado: {datetime.now().strftime('%Y-%m-%d %H:%M')}_\n\n"

    rol = "**Actuá como** un/a desarrollador/a senior y mentor/a técnico/a.\n\n"

    tarea_block = f"## Tarea\n\"\"\"\n{tarea.strip()}\n\"\"\"\n\n"

    extra = []
    if lenguaje:
        extra.append(f"- Lenguaje principal: **{lenguaje}**")
    if stack:
        extra.append(f"- Stack/Frameworks: **{', '.join(stack)}**")
    if tono:
        extra.append(f"- Tono: **{tono}** (claro, paso a paso, conciso)")

    extra_block = ("## Preferencias\n" + "\n".join(extra) + "\n\n") if extra else ""

    contexto_block = f"## Contexto\n{contexto.strip()}\n\n" if contexto else ""

    if restricciones:
        restricciones_block = "## Restricciones\n" + "\n".join([f"- {r}" for r in restricciones]) + "\n\n"
    else:
        restricciones_block = ""

    salida_block = "## Formato de salida (obligatorio)\n" + "\n".join([f"- {s}" for s in salida]) + "\n\n"

    criterios = (
        "## Criterios de calidad\n"
        "- Explicá supuestos y decisiones de diseño.\n"
        "- Incluí comentarios en el código donde aporte claridad.\n"
        "- Señalá alternativas si existen enfoques viables.\n"
        "- Considerá performance, seguridad y testabilidad.\n\n"
    )

    cierre = (
        "## Instrucción final\n"
        "Respondé **únicamente** siguiendo el formato de salida indicado. "
        "Si falta información, explícita los supuestos que asumís.\n"
    )

    return header + meta + rol + tarea_block + extra_block + contexto_block + restricciones_block + salida_block + criterios + cierre

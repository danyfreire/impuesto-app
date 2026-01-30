import streamlit as st
from io import BytesIO
from datetime import datetime
import pandas as pd

st.set_page_config(
    page_title="Calculadora de impuestos y descuentos",
    page_icon="🧮",
    layout="centered",
)

st.title("🧮 Calculadora de impuestos y descuentos")
st.caption("Hello app: calcula subtotal, descuento, impuesto y total. Hecha para validar rápido una idea.")

col1, col2 = st.columns(2)

with col1:
    precio_unitario = st.number_input("Precio unitario", min_value=0.0, value=20.0, step=0.5, format="%.2f")
    cantidad = st.number_input("Cantidad", min_value=1, value=1, step=1)
    moneda = st.selectbox("Moneda", ["USD", "EUR", "MXN", "COP"], index=0)

with col2:
    tipo_desc = st.selectbox("Descuento", ["% (porcentaje)", "Valor fijo"], index=0)
    descuento_val = st.number_input("Valor de descuento", min_value=0.0, value=10.0, step=1.0, format="%.2f")

    preset = st.selectbox(
        "Preset de impuesto",
        ["Ecuador (IVA 15%)", "0% (sin impuesto)", "Personalizado"],
        index=0,
    )

    default_tax = 15.0 if preset == "Ecuador (IVA 15%)" else 0.0

    if preset == "Personalizado":
        iva_pct = st.number_input("Impuesto (%)", min_value=0.0, value=default_tax, step=0.5, format="%.2f")
    else:
        iva_pct = default_tax
        st.text(f"Impuesto aplicado: {iva_pct:.2f}%")

aplicar_impuesto_sobre = st.radio(
    "Aplicar impuesto sobre:",
    ["Subtotal - Descuento (lo común)", "Subtotal (antes del descuento)"],
    index=0,
)

# Cálculos
subtotal = precio_unitario * float(cantidad)

if tipo_desc.startswith("%"):
    descuento = subtotal * (descuento_val / 100.0)
else:
    descuento = descuento_val

# No permitir descuento mayor al subtotal
descuento = min(descuento, subtotal)

base = (subtotal - descuento) if aplicar_impuesto_sobre.startswith("Subtotal -") else subtotal
impuesto = base * (iva_pct / 100.0)
total = (subtotal - descuento) + impuesto


def money(x: float) -> str:
    return f"{moneda} {x:,.2f}"


st.divider()

k1, k2, k3, k4 = st.columns(4)
k1.metric("Subtotal", money(subtotal))
k2.metric("Descuento", money(descuento))
k3.metric("Impuesto", money(impuesto))
k4.metric("Total", money(total))

# Detalle (expander)
with st.expander("Detalle del cálculo"):
    st.write(
        {
            "precio_unitario": float(precio_unitario),
            "cantidad": int(cantidad),
            "subtotal": float(subtotal),
            "tipo_descuento": tipo_desc,
            "valor_descuento": float(descuento_val),
            "descuento_aplicado": float(descuento),
            "preset_impuesto": preset,
            "impuesto_pct": float(iva_pct),
            "base_imponible": float(base),
            "impuesto": float(impuesto),
            "total": float(total),
            "moneda": moneda,
        }
    )

# ===== EXPORTAR A EXCEL (FUERA DEL EXPANDER) =====
st.divider()
st.subheader("📤 Exportar")

resumen_df = pd.DataFrame(
    [
        ["Precio unitario", float(precio_unitario)],
        ["Cantidad", int(cantidad)],
        ["Subtotal", float(subtotal)],
        ["Tipo de descuento", tipo_desc],
        ["Valor de descuento", float(descuento_val)],
        ["Descuento aplicado", float(descuento)],
        ["Preset impuesto", preset],
        ["Impuesto (%)", float(iva_pct)],
        ["Base imponible", float(base)],
        ["Impuesto", float(impuesto)],
        ["Total", float(total)],
        ["Moneda", moneda],
        ["Generado", datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
    ],
    columns=["Campo", "Valor"],
)


def build_excel_bytes(summary: pd.DataFrame) -> bytes:
    output = BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        summary.to_excel(writer, sheet_name="Resumen", index=False)
        ws = writer.sheets["Resumen"]
        ws.column_dimensions["A"].width = 22
        ws.column_dimensions["B"].width = 30
    return output.getvalue()


excel_bytes = build_excel_bytes(resumen_df)

st.download_button(
    label="⬇️ Descargar Excel",
    data=excel_bytes,
    file_name=f"calculo_impuestos_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
)

st.caption("Tip: luego le metemos presets (IVA Ecuador 15%, ICE, propinas, etc.) o export a Excel/PDF.")

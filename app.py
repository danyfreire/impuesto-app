import streamlit as st

st.set_page_config(page_title="Calculadora de impuestos y descuentos", page_icon="🧮", layout="centered")

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
    iva_pct = st.number_input("Impuesto (%)", min_value=0.0, value=15.0, step=0.5, format="%.2f")

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

with st.expander("Detalle del cálculo"):
    st.write(
        {
            "precio_unitario": precio_unitario,
            "cantidad": int(cantidad),
            "subtotal": subtotal,
            "descuento": descuento,
            "base_imponible": base,
            "impuesto_pct": iva_pct,
            "impuesto": impuesto,
            "total": total,
        }
    )

st.caption("Tip: luego le metemos presets (IVA Ecuador 15%, ICE, propinas, etc.) o export a Excel/PDF.")

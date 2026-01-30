# 🧮 Calculadora de Impuestos y Descuentos

Web app simple para calcular **subtotal, descuentos, impuestos y total**.  
Creada como **MVP / hello app** para validar ideas rápidamente usando **Python + Streamlit**.

👉 App pública:  
https://impuesto-app-sbvsbod4rksag5kfpnbpiv.streamlit.app/

---

## ✨ Funcionalidades

- Cálculo de subtotal por precio y cantidad
- Descuentos:
  - Porcentaje (%)
  - Valor fijo
- Impuesto configurable (%)
- Opción de aplicar impuesto:
  - Después del descuento (lo común)
  - Antes del descuento
- Visualización clara de:
  - Subtotal
  - Descuento
  - Impuesto
  - Total
- App web responsive (desktop / mobile)

---

## 🛠️ Tecnologías

- **Python 3**
- **Streamlit**
- Deploy gratuito con **Streamlit Community Cloud**
- Código versionado en **GitHub**

---

## 🚀 Cómo correr la app localmente

1️⃣ Clonar el repositorio
git clone https://github.com/danyfreire/impuesto-app.git
cd impuesto-app

2️⃣ Crear y activar entorno virtual
python -m venv venv
venv\Scripts\activate

3️⃣ Instalar dependencias
pip install -r requirements.txt

4️⃣ Ejecutar la app
streamlit run app.py


La app se abrirá en:

http://localhost:8501

🌍 Deploy

La aplicación está desplegada públicamente usando Streamlit Cloud, conectada directamente al repositorio de GitHub.

Cada push a la rama main actualiza automáticamente la app.

🔮 Próximas mejoras (roadmap)

Preset IVA Ecuador 15%

Exportar resultados a Excel / PDF

Historial de cálculos

Modo “precio incluye IVA”

Conexión con dominio personalizado

📄 Licencia

Proyecto personal / experimental.
Libre para usar como referencia o base para otros proyectos.

👤 Autor

Dany Freire
GitHub: https://github.com/danyfreire

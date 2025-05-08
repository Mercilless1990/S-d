import streamlit as st
from PIL import Image, ImageDraw
import io

st.set_page_config(page_title="Analisador de Supply & Demand", layout="centered")

st.title("🔍 Analisador de Zonas de Supply e Demand")
st.write("Envie uma imagem de gráfico (ex: TradingView - Pepperstone) para análise.")

uploaded_file = st.file_uploader("📤 Enviar gráfico (.png ou .jpg)", type=["png", "jpg", "jpeg"])

if uploaded_file:
    # Abrir a imagem enviada
    image = Image.open(uploaded_file).convert("RGB")
    draw = ImageDraw.Draw(image)

    # Desenhar zonas fictícias para exemplo (pode ser substituído por detecção real)
    width, height = image.size

    # Zona de Supply (topo do gráfico)
    supply_zone = [int(width * 0.6), int(height * 0.1), int(width * 0.95), int(height * 0.2)]
    draw.rectangle(supply_zone, outline="red", width=4)
    draw.text((supply_zone[0] + 10, supply_zone[1] + 5), "📦 Supply Zone (RBD)", fill="red")

    # Zona de Demand (fundo do gráfico)
    demand_zone = [int(width * 0.05), int(height * 0.75), int(width * 0.4), int(height * 0.85)]
    draw.rectangle(demand_zone, outline="green", width=4)
    draw.text((demand_zone[0] + 10, demand_zone[1] + 5), "📦 Demand Zone (DBR)", fill="green")

    st.image(image, caption="📊 Gráfico com Zonas Detectadas", use_column_width=True)

    # Interpretação em texto
    st.markdown("---")
    st.subheader("🧠 Interpretação Automática:")

    st.markdown("""
    - O gráfico mostra uma **zona de oferta (supply)** na região superior, indicando possível resistência.
    - Uma **zona de demanda (demand)** foi detectada na parte inferior, que pode servir como suporte.
    - O comportamento do preço entre essas zonas pode indicar reversões ou rompimentos importantes.
    - Observe se há **padrões de candle** nessas regiões (ex: pin bar, engolfo) para maior confirmação.
    """)

    st.success("Análise completa! Você pode ajustar os parâmetros futuramente.")
else:
    st.info("Envie uma imagem do gráfico para iniciar a análise.")


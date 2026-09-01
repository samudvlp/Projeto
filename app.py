import asyncio
from asyncio import wait

import streamlit as st

# Título da página
st.title("🚗 Calculadora de Gasto de Combustível")
st.write("Preencha os dados abaixo para calcular o custo da sua viagem.")

# Recebendo os dados do usuário com campos de formulário
distancia = st.number_input("Distância da viagem (em km)", min_value=0.0)
consumo_km_l = st.number_input("Consumo médio do carro (em km/l)", min_value=0.0)
preco_litro = st.number_input("Preço do litro do combustível (R$)", min_value=0.0)

# Botão para executar o cálculo
if st.button("Calcular Gasto"):
    # Calculando os resultados
    litros_necessarios = distancia / consumo_km_l
    custo_total = litros_necessarios * preco_litro

    # Exibindo os resultados na tela

    st.capti

    st.subheader("📊 Resumo da Viagem")
    st.info(f"**Combustível necessário:** {litros_necessarios:.2f} litros")
    st.success(f"**Custo total estimado:** R$ {custo_total:.2f}")
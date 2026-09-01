import streamlit as st
import pandas as pd


st.title("Calculadora de Gasto de Combustível")
st.write("Preencha os dados abaixo para calcular o custo da sua viagem.")


distancia = st.number_input("Distância da viagem (em km)", min_value=0.0)
consumo_km_l = st.number_input("Consumo médio do carro (em km/l)", min_value=0.0)
preco_litro = st.number_input("Preço do litro do combustível (R$)", min_value=0.0)


if st.button("Calcular Gasto"):

    litros_necessarios = distancia / consumo_km_l
    custo_total = litros_necessarios * preco_litro

    st.subheader("Resumo da Viagem")
    st.success(f"**Combustível necessário:** {litros_necessarios:.2f} litros")
    st.success(f"**Custo total estimado:** R$ {custo_total:.2f}")
    st.caption("""calculo:""")
    st.caption("""Distância dividida pelo consumo do veiculo = a quantidade de gasolina/alcool necessário.""")
    st.caption("""Litros necessários vezes o preço do combustivel = o custo total em reais.""")
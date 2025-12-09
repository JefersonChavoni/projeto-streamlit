import streamlit as st
import pandas as pd
from datetime import date

def gravar_dados(nome, data_nasc, tipo):
    if nome and data_nasc <= date.today():
        st.session_state["sucesso"] = True
    else:
        st.session_state["sucesso"] = False

st.set_page_config(
    page_title="Cadastro de Clientes",
    page_icon="👤",
    layout="wide"
)

st.title("Cadastro de Clientes")
st.divider()

nome = st.text_input("Digite o nome do Cliente",
                     key="|nom_cli")
dt_nasc = st.date_input("Data nascimento",
                        key="Dat_Nas",
                        format="DD/MM/YYYY")
tipo = st.selectbox("Tipo do Cliente",
                    ["Pessoa Juridica", "Pessoa Fisica"])

bt_cad_cli = st.button("Cadastrar",
                       on_click=gravar_dados,
                       args=[nome, dt_nasc, tipo])

if bt_cad_cli:
    if st.session_state["sucesso"]:
        with open("clientes.csv", "a", encoding="utf-8") as file:
            file.write(f"{nome},{dt_nasc}, {tipo}\n")
        st.success("Cliente cadastrado com sucesso")
    else:
        st.error("Houve algum problema no cadastro")
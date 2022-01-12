#Bibliotecas
import streamlit as st 
from stqdm import stqdm
import base64

#Pegando funções
from Scrappers.mercado_livre import ml_final


def download_file(dataset):
    csv = dataset.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{dataset}.csv">Download csv file</a>'

    return st.markdown(href, unsafe_allow_html=True)

#página

#Título
st.title("Buscador de anúncios Huawei")

#Instruções
st.write("Coloque o valor correspondente de cada Marketplace")
st.write("1 - Amazon\n\n\n2 - Mercado Livre\n\n3 - Via Varejo")
escolha = st.number_input("Valor",1,6)

botao = st.button("Buscar dados")

if botao:
    if escolha == 1:
        st.write("Escolheu AMAZON")
    elif escolha == 2:
        st.write("Escolheu MERCADO LIVRE")
        download_file(ml_final())
    else:
        st.write("Algo deu errado")




import streamlit as st
import pandas as pd

# Sidebar (Menu Lateral)
page = st.sidebar.selectbox("Escolha a Página", ["Visão Geral", "Filtros e Dados"])

def show_overview():
    
    # Visão Geral do Projeto
    st.header("Visão Geral do Projeto")
    st.write("Bem-vindo ao projeto de Avaliações de Jogos no Steam! Este projeto gira em torno da análise e apresentação "
             "de avaliações de jogos na plataforma Steam. O conjunto de dados contém várias colunas fornecendo insights "
             "sobre as avaliações dos usuários, incluindo data de postagem, reações engraçadas, reações úteis, horas jogadas, "
             "status de acesso antecipado, recomendações e a própria análise escrita.")
    
    # Como Funciona
    st.header("Como Funciona")
    st.write("O projeto utiliza um conjunto de dados com informações sobre avaliações de jogos. Aqui está uma breve visão "
             "geral dos principais componentes:")
    
    # Objetivo do Projeto
    st.header("Objetivo do Projeto")
    st.write("O principal objetivo deste projeto é obter insights das avaliações de jogos no Steam. Isso inclui entender "
             "os sentimentos dos jogadores, identificar jogos populares e explorar padrões nas recomendações dos jogadores "
             "durante períodos de acesso antecipado.")
    
    # Como Utilizar
    st.header("Como Utilizar")
    st.write("Para explorar o projeto, você pode navegar por diferentes seções usando a barra lateral. As principais seções incluem:")
      
    st.header("Conclusão")
    st.write("Sinta-se à vontade para analisar o conjunto de dados, obter insights e tirar conclusões significativas a partir "
               "dos dados apresentados. Para análises específicas ou dúvidas, novos recursos podem ser incorporados com base nos "
               "objetivos do seu projeto.")
  
    st.write("Aproveite a exploração do projeto de Avaliações de Jogos no Steam!")
# Página de Visão Geral
if page == "Visão Geral":
    show_overview()

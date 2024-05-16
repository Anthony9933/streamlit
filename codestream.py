import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px


# Sidebar (Menu Lateral)
page = st.sidebar.selectbox("Escolha a Página", ["Visão Geral", "Filtros e Dados"])
def show_overview():
    
    # Visão Geral do Projeto
    st.header("Visão Geral do Projeto")
    st.write("Bem-vindo ao projeto de Visualização de dados da loja Moda Antiga! Este projeto gira em torno da análise e apresentação "
             "de dados do estoque e de vendas de produtos da loja Moda Antiga. O conjunto de dados contém várias colunas fornecendo insights "
             "sobre os produtos e informações relativas a vendas, incluindo data, produtos mais vendidos, melhores e piores meses de venda.")
    
    # Como Funciona
    st.header("Como Funciona")
    st.write("O projeto utiliza um conjunto de dados com informações sobre as vendas e o estoque da loja. Aqui está uma breve visão "
             "geral dos principais componentes:")
    
    # Objetivo do Projeto
    st.header("Objetivo do Projeto")
    st.write("O principal objetivo deste projeto é obter insights pela análise dos dados e gráficos criados. Isso inclui entender "
             "o que os dados estão nos dizendo, identificar e explorar padrões dos compradores "
             "prevendo e criando estratégias para aumentar as vendas.")
    
    # Como Utilizar
    st.header("Como Utilizar")
    st.write("Para explorar o projeto, você pode navegar por diferentes seções usando a barra lateral. As principais seções incluem:")
      
    st.header("Conclusão")
    st.write("Sinta-se à vontade para analisar o conjunto de dados, obter insights e tirar conclusões significativas a partir "
               "dos dados apresentados. Para análises específicas ou dúvidas, novos recursos podem ser incorporados com base nos "
               "objetivos do seu projeto.")
  
    st.write("Aproveite a exploração do projeto!")

def show_filters_data():
    st.header("Filtros e Dados")
    df = pd.read_csv('dados.csv', encoding='latin-1', delimiter=';')
    st.header('Gráficos')
    st.dataframe(df)
    # Criar uma nova coluna 'Categoria'
    #df['Categoria'] = df['DESCRIÇÃO']
    
    # Lista de tipos de t-shirts
    #tipos_tshirts = ['t-shirt tipo1', 't-shirt tipo2', 't-shirt tipo3']  # substitua pelos nomes reais dos tipos de t-shirts
    
    # Agrupar todos os tipos de t-shirts em uma única categoria
    #df.loc[df['Categoria'].isin(tipos_tshirts), 'Categoria'] = 'T-Shirt'
    
    # Agora você pode usar a coluna 'Categoria' para suas análises


    # Calcular o lucro provável
    # Criar um novo DataFrame contendo apenas os itens que contêm "t-shirt"
    df_tshirts = df[df['DESCRICAO'].str.contains('T-SHIRTS', case=False, na=False)]
    df_tshirt = df[df['DESCRICAO'].str.contains('T-SHIRT', case=False, na=False)]
    df_camisa = df[df['DESCRICAO'].str.contains('CAMISA', case=False, na=False)]
    df_cropped = df[df['DESCRICAO'].str.contains('CROPPED', case=False, na=False)]
    df_bermuda = df[df['DESCRICAO'].str.contains('BERMUDA', case=False, na=False)]
    df_blusa = df[df['DESCRICAO'].str.contains('BLUSA', case=False, na=False)]
    df_shorts = df[df['DESCRICAO'].str.contains('SHORTS', case=False, na=False)]
    df_short = df[df['DESCRICAO'].str.contains('SHORT', case=False, na=False)]
    df_calça = df[df['DESCRICAO'].str.contains('CALCA', case=False, na=False)]
    df_saia = df[df['DESCRICAO'].str.contains('SAIA', case=False, na=False)]
    df_blazer = df[df['DESCRICAO'].str.contains('BLAZER', case=False, na=False)]
    df_colete = df[df['DESCRICAO'].str.contains('COLETE', case=False, na=False)]
    df_jaqueta = df[df['DESCRICAO'].str.contains('JAQUETA', case=False, na=False)]
    
    fig, axs = plt.subplots(2, 2, figsize=(15, 10))
    axs[0, 0].hist(df_tshirts['DESCRICAO'], bins=20, color='blue', alpha=0.7)
    axs[0, 1].set_title('T-Shirts')
    axs[0, 1].hist(df_camisa['DESCRICAO'], bins=20, color='green', alpha=0.7)
    axs[0, 1].set_title('Camisas')
    axs[1, 0].hist(df_cropped['DESCRICAO'], bins=20, color='red', alpha=0.7)
    axs[1, 0].set_title('Cropped')
    axs[1, 1].hist(df_bermuda['DESCRICAO'], bins=20, color='purple', alpha=0.7)
    axs[1, 1].set_title('Bermudas')
    plt.tight_layout()
    st.pyplot(fig)
    
# Página de Visão Geral
if page == "Visão Geral":
    show_overview()


elif page == "Filtros e Dados":
    show_filters_data()
    
# Página de Filtros de acidentes
#elif page == "Gráficos de Acidentes e Casualidades ao Longo do Tempo":
    #show_graphs()

#elif page == "Número de Acidentes por Hora do Dia":
    #show_accidents_by_hour()

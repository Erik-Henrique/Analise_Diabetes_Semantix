import streamlit as st
import importlib
import config 

# Configuração da barra lateral
selection = st.sidebar.radio("paginas:", ["Início", "Análise do DataFrame", "Análises gráficas", "Resultados"])

# Dicionário para mapear seleção para o nome do módulo
pages = {
  "Início": "paginas.1 - Início",
  "Análise do DataFrame": "paginas.2 - Análise do DataFrame",
  "Análises gráficas": "paginas.3 - Análises gráficas",
  "Resultados": "paginas.4 - Resultados",
}

# Importar e renderizar a página selecionada
module = importlib.import_module(pages[selection])
module.app()

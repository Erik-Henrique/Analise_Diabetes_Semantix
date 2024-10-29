import streamlit as st
import importlib
import config 

# Configuração da barra lateral
selection = st.sidebar.radio("Páginas:", ["Início", "Análise do DataFrame", "Análises gráficas", "Resultados"])

# Dicionário para mapear seleção para o nome do módulo
pages = {
  "Início": "pages.1 - Início",
  "Análise do DataFrame": "pages.2 - Análise do DataFrame",
  "Análises gráficas": "Pages.3 - Análises gráficas",
  "Resultados": "pages.4 - Resultados",
}

# Importar e renderizar a página selecionada
module = importlib.import_module(pages[selection])
module.app()

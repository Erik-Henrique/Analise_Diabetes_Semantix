import streamlit as st
import importlib
import config 

# Configuração da barra lateral
selection = st.sidebar.radio("Páginas:", ["Início", "Análise do DataFrame", "Resultados"])

# Dicionário para mapear seleção para o nome do módulo
pages = {
  "Início": "Pages.1- Início",
  "Análise do DataFrame": "Pages.2 - Análise do DataFrame",
  "Resultados": "Pages.3 - Resultados",
}

# Importar e renderizar a página selecionada
module = importlib.import_module(pages[selection])
module.app()
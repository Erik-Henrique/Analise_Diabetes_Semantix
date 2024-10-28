import streamlit as st
import pandas as pd
import numpy as np
from imblearn.under_sampling import RandomUnderSampler

st.markdown('''## Este é o DataFrame que será usado no projeto. \n ##### Fique à vontade para visualizar todas as informações continas nele''')

DATA_URL = (r"https://raw.githubusercontent.com/Erik-Henrique/Analise_Diabetes_Semantix/refs/heads/main/diabetes_prediction_dataset.csv")
df = pd.read_csv(DATA_URL)
df.drop_duplicates(inplace=True)
df.genero = df.genero.map({'Female': 0, 'Male': 1})

under = RandomUnderSampler()
x_under, y_under = under.fit_resample(df.drop(columns='diabete'), df['diabete'])
df_under = pd.concat([x_under, y_under], axis=1)
df_under.diabete.value_counts()

df_modelos = pd.get_dummies(df_under, columns=['fumante'])
df_modelos.fumante_current = df_modelos.fumante_current.astype(int)
df_modelos.fumante_ever = df_modelos.fumante_ever.astype(int)
df_modelos.fumante_former = df_modelos.fumante_former.astype(int)
df_modelos.fumante_never = df_modelos.fumante_never.astype(int)
df_modelos['fumante_not current'] = df_modelos['fumante_not current'].astype(int)
df_modelos['fumante_No Info'] = df_modelos['fumante_No Info'].astype(int)

col1, col2 = st.columns(2)
  
with col1:
       st.markdown('''
                    | Variável | Significado |
                    |---|---|    
                    | genero | Gênero do paciente -> 1 = Masculino  0 = Feminino |
                    | idade | Idade do paciente |
                    | hipertenso | Se o paciente é hipertenso -> 1 = Sim  0 = Não |
                    | problema_coracao | Se o paciente tem algum problema no coração -> 1 = Sim  0 = Não |
                    | fumante | Se o paciente fuma ou já fumou -> 1 = Sim  0 = Não |
                    | imc | Indice de massa corporal do paciente |
                    | nivel_hemoglobinaA1c | Nível de Hemoblobina A1c no sangue |
                    | nivel_glicose_sangue | Nível de Glicose no sangue |
                    | diabete | Se o paciente é diabetico -> 1 = Sim  0 = Não |
                    ''')
  
  
with col2:
      number1 = st.number_input('Indice inicial', value = 0)
      number2 = st.number_input('Indice final', value = 16964)
      colunas = st.multiselect('Seletor de colunas',default= 'Todas as variáveis',                   
                                                  options=['Todas as variáveis','genero', 'idade', 'hipertenso', 'problema_coracao',
                                                           'fumante', 'imc', 'nivel_hemoglobinaA1c', 'nivel_glicose_sangue', 'diabete'])
    
    
    
      if 'Todas as variáveis' not in colunas:
           if st.button('Visualizar o Data Frame'):
                  st.write(df[colunas][int(number1):int(number2)+1])
    
      if 'Todas as variáveis' in colunas:
           if st.button('Visualizar o Data Frame'):
                  st.write(df[int(number1):int(number2)+1])

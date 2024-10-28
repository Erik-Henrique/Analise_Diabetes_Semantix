import streamlit as st
import pandas as pd
import numpy as np
from imblearn.under_sampling import RandomUnderSampler
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import classification_report
from sklearn.metrics import roc_auc_score , roc_curve , accuracy_score
import matplotlib.pyplot as plt
import seaborn as sn
from pycaret.classification import *

st.set_page_config(layout='wide',
                   page_title='Análise Diabetes')

st.markdown('''## Resultados do modelo.''')

DATA_URL = (r"https://raw.githubusercontent.com/Erik-Henrique/Analise_Diabetes_Semantix/refs/heads/main/diabetes_prediction_dataset.csv")
df = pd.read_csv(DATA_URL)
df.drop_duplicates(inplace=True)
df.genero = df.genero.map({'Female': 0, 'Male': 1})

under = RandomUnderSampler(random_state=0)
x_under, y_under = under.fit_resample(df.drop(columns='diabete'), df['diabete'])
df_under = pd.concat([x_under, y_under], axis=1)

df_modelos = pd.get_dummies(df_under, columns=['fumante'])
df_modelos.fumante_current = df_modelos.fumante_current.astype(int)
df_modelos.fumante_ever = df_modelos.fumante_ever.astype(int)
df_modelos.fumante_former = df_modelos.fumante_former.astype(int)
df_modelos.fumante_never = df_modelos.fumante_never.astype(int)
df_modelos['fumante_not current'] = df_modelos['fumante_not current'].astype(int)
df_modelos['fumante_No Info'] = df_modelos['fumante_No Info'].astype(int)

df_py = df_modelos.sample(frac=0.95, random_state=0)
df_teste = df_modelos.drop(df_py.index)
df_py.reset_index(drop=True, inplace=True)
df_teste.reset_index(drop=True, inplace=True)

setup(data=df_py, target='diabete', session_id=0)

gbc = create_model('gbc')
final_lr = finalize_model(gbc)

plot_model(final_lr, plot = 'confusion_matrix', display_format = 'streamlit')
plot_model(final_lr, plot = 'class_report', display_format = 'streamlit')
plot_model(final_lr, plot = 'auc', display_format = 'streamlit')
plot_model(final_lr, plot = 'pr', display_format = 'streamlit')
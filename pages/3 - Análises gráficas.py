import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def app():
  df = pd.read_csv('/content/diabetes_prediction_dataset.csv')
  df.drop_duplicates(inplace=True)
  df.drop(df[df['genero']=="Other"].index, inplace=True)
  df.genero = df.genero.map({'Female': 0, 'Male': 1})

  under = RandomUnderSampler()
  x_under, y_under = under.fit_resample(df.drop(columns='diabete'), df['diabete'])
  df_under = pd.concat([x_under, y_under], axis=1)
  

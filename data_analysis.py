# Les bibliothéque importées pour l'analyse de données
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind, pointbiserialr, chi2_contingency

# Lecture de la base de données
data = pd.read_csv('C:/Users/Maamar/Desktop/prediction-of-tgv-delays/dataset/regularite-mensuelle-tgv-aqst.csv', delimiter=";")
print(data.head())

#Info sur les types des données du dataset (float, int, object)
print(data.dtypes)

#Info sur chaque colonne du dataset
print(data.info())

#On convertit la colonne 'date' du DataFrame en un format de date spécifique (année-mois)
#en utilisant la fonction pd.to_datetime, et on crée une nouvelle colonne "année" pour faciliter le split
data['date'] = pd.to_datetime(data['date'], format='%Y-%m')
data['annee'] = data['date'].dt.year

#Infos sur le nombre de valeurs nulles (manquantes) dans le dataset
print(data.isnull().sum())
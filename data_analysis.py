# Les bibliothéque importées pour l'analyse de données
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind, pointbiserialr, chi2_contingency

data = pd.read_csv('C:/Users/Maamar/Desktop/prediction-of-tgv-delays/dataset/regularite-mensuelle-tgv-aqst.csv', delimiter=";")
print(data.head())
print(data.dtypes)
print(data.info())

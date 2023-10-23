# prediction-of-TGV-delays
Ce projet vise à développer un modèle de prédiction du retard des Trains à Grande Vitesse (TGV) en utilisant des techniques de machine learning et d'analyse de données. Notre objectif est d'améliorer la fiabilité des prévisions de retard des TGV en exploitant diverses données historiques.

Dans cette branche on va s'intéresser dans un premier temps à l'EDA (exploration et analyse de données ), ainsi que des modèles de régression classiques de MAchine Learning (random Forest, Xgboost, Knn regression..) voir le fichier Data_analysis.ipynb.

Ensuite on va essayer de prédire les retards des trains à l'aide des modèles de Forecasting ( Voir le fichier Forecasting.ipynb), plus particulièrement on va utiliser le modèle Prophet de Meta pour sa robustesse, sa précision et sa simplicité.


Voici le résultat du forecasting sur le trajet le plus réccurent dans la dataset :


![Forecast_full](https://github.com/Enaouram/prediction-of-TGV-delays/assets/124512121/cb9cda62-de82-4ede-8242-0dadcc6f5880)

# Rapport

Voici les élements qui vont constituer notre rapport final. Ici, nous détaillons chaque décision prises quand au choix de
l'utilisation des données ou des méthodes utilisées.

## Data Analysis

Avant de commencer à traiter nos données, nous devons d'abord les comprendre. Pour cela, nous avons cette étape d'analyse
de la donnée.

PLaybook "descriptive_stats" : l'objectif ici et de trouver des statistiques de bases sur la données pour commencer à repérer par exemple des premières corrélation ou des données abérantes...

Ce qu'on essaie de visualiser :

1. L'importance de la gare de départ et d'arrivée dans le retard du train
2. Une corrélation avec la durée moyenne du retard
3. Une corrélation entre le nombre de retard et la durée du retard

## Réflexion

### Réduction de dimension

Faire une réduction de dimension implique d'avoir assez de features corrélées. Cependant, dans nos analyses, il ne semble pas qu'il existe beaucoup de corrélation dans notre dataset. Faire une réduction de dimension ne sera donc soit pas très précise, soit ne retira pas assez de dimension pour être pertinent. Il pourrait être pertinent d'essayer d'ajouter des données au dataset.

### Ajouter des données

- Ajouter la distance :
  Cette donnée ne semble pas assez pertinente. En effet, il semble évident que la durée du trajet dépend directement de la distance entre les deux gares. Plus les gares sont éloignées, plus le trajet sera long. Ajouter cette caractéristique au dataset n'est donc pas pertinente car elle n'apportera pas vraiment de nouvelles perspectives.

- Ajouter le nombre de voies :
  Cette donnée ne semble pas non plus très pertinente. Encore une fois, intuitivement, plus une gare est grande et fréquentée, plus elle aura de trajets prévus en gare et plus elle aura de voies. Donc intuitivement, on peut se dire qu'il y a une corrélation entre le nombre de trajets en gare et le nombre de voies. Cette donnée ne semble pas non plus apporter de nouvelle perspective à notre problème.

- Ajouter la fréquentation :
  Cette donnée semble la plus prometteuse. On peut imaginer qu'une gare avec beaucoup de fréquentation aura forcément beaucoup de trajets prévus. Donc là aussi, ces données seront corrélées. Mais cette donnée donne une nouvelle vision à notre problème : elle permet de se faire une idée de la capacité des trains sur les trajets en question. En effet, une gare avec peu de trajets prévus mais une forte fréquentation implique que les trains prennent plus de passagers pour ces trajets-là. Il est possible que le fait d'augmenter la capacité des trains augmente leurs chances d'être en retard.

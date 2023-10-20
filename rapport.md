# Rapport

Voici les élements qui vont constituer notre rapport final. Ici, nous détaillons chaque décision prises quand au choix de l'utilisation des données ou des méthodes utilisées.

<h2>Analyse de données :</h2>

MAROUANE MAAMAR : Toujours dans la phase d'analyse de données, voici eu une idée sur les données qui sont nulles (manquantes) :
-Colonne 'commentaire_retards_depart' (Toutes les valeurs sont nulles)
-Colonne 'commentaire_annulation' (Toutes les valeurs sont nulles)
-Colonne 'commentaires_retard_arrivee' (7456/8145 données sont nulles ce qui donne 92% des données manquantes)

 J'ai pensé aux méthodes de gestion des données manquantes 'Handling Missing Data' dans le cours que ce soit 'Univariate Imputation' ou 'Multivariate Imputation' pour les cas MCAR ou MAR. Mais plusieurs contraintes sont à considérer : 

 -Il fallait d'abord déterminer la nature des données manquantes (MCAR, MAR ou MNAR) et pour celà il fallait rentrer en contact avec les responsables d'enregistrement de ces données pour la SNCF (contrainte de temps)
 -La nature de ces données est textuel, un encodage normal ne suffisait pas puisqu'il fallait analyser tout le commentaire écrit pour ensuite juger d'une certaine manière comment traiter cette donnée (techniques d'analyse de texte pour extraire des informations à partir des commentaires. Par exemple, l'analyse de sentiments, la détection d'entités nommées, ou la catégorisation des commentaires en fonction de leur contenu.)
 -Pour commenter les autres retards il fallait des données supplémentaires qu'il fallait chercher dans d'autres datasets et alimenter la base de données en s'appuyant sur ces recherches (contrainte de temps encore une fois)

 Solutions : 
 -Créer une nouvelle catégorie : Créez une catégorie "Inconnu" ou "Données manquantes" pour les commentaires manquants, ce qui permettra de les conserver tout en les distinguant des autres commentaires.
 -Supprimer cette colonne avec les 2 autres colonnes nulles.
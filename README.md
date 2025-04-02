# Personal-Medical-Cost

## Description
Ce projet vise à analyser et prédire les coûts médicaux personnels en utilisant des techniques d'analyse de données et d'apprentissage automatique. En examinant divers facteurs tels que l'âge, le sexe, l'IMC, le nombre d'enfants, le statut tabagique et la région géographique, nous cherchons à comprendre leur impact sur les frais médicaux et à développer des modèles prédictifs précis.

## Objectifs
- Explorer les relations entre les caractéristiques démographiques et les coûts médicaux
- Identifier les facteurs les plus déterminants dans la variation des dépenses médicales
- Développer et comparer différents modèles de machine learning pour prédire les coûts
- Fournir des insights utiles pour les professionnels de la santé, les assureurs et les décideurs politiques

## Jeu de données
Le projet utilise un ensemble de données contenant les informations suivantes :
- **âge** : Âge du bénéficiaire
- **sexe** : Genre du bénéficiaire (homme/femme)
- **imc** : Indice de masse corporelle (poids en kg / taille en m²)
- **enfants** : Nombre d'enfants couverts par l'assurance maladie
- **fumeur** : Statut tabagique (oui/non)
- **région** : Zone résidentielle du bénéficiaire aux États-Unis (nord-est, sud-est, sud-ouest, nord-ouest)
- **frais** : Frais médicaux individuels facturés par l'assurance maladie

## Technologies utilisées
- **Python** : Langage de programmation principal
- **Pandas** : Manipulation et analyse des données
- **NumPy** : Calculs numériques
- **Matplotlib/Seaborn** : Visualisation des données
- **Scikit-learn** : Modèles de machine learning et évaluation
- **Jupyter Notebook** : Développement interactif et présentation

## Structure du projet
```
Personal-Medical-Cost/
├── data/
│   ├── raw/              # Données brutes non modifiées
│   └── processed/        # Données nettoyées et préparées
├── notebooks/
│   ├── exploration.ipynb # Analyse exploratoire des données
│   ├── preprocessing.ipynb # Nettoyage et préparation des données
│   └── modeling.ipynb    # Modélisation et évaluation
├── src/
│   ├── data/             # Scripts pour le traitement des données
│   ├── features/         # Scripts pour l'ingénierie des caractéristiques
│   ├── models/           # Scripts pour l'entraînement et l'évaluation des modèles
│   └── visualization/    # Scripts pour la création de visualisations
├── results/
│   ├── figures/          # Graphiques et visualisations générés
│   └── models/           # Modèles entraînés sauvegardés
├── requirements.txt      # Dépendances Python
└── README.md             # Ce fichier
```

## Installation et configuration

### Prérequis
- Python 3.7 ou supérieur
- Pip (gestionnaire de paquets Python)
- Git

### Étapes d'installation
1. Cloner le dépôt :
   ```bash
   git clone https://github.com/DahliaNoir71/Personal-Medical-Cost.git
   cd Personal-Medical-Cost
   ```

2. Créer et activer un environnement virtuel :
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur Windows : venv\Scripts\activate
   ```

3. Installer les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

### Analyse exploratoire des données
Ouvrir et exécuter le notebook d'exploration :
```bash
jupyter notebook notebooks/exploration.ipynb
```

### Prétraitement des données
Exécuter le notebook de prétraitement ou le script :
```bash
jupyter notebook notebooks/preprocessing.ipynb
# ou
python src/data/preprocess.py
```

### Modélisation
Exécuter le notebook de modélisation :
```bash
jupyter notebook notebooks/modeling.ipynb
```

## Modèles implémentés
- Régression linéaire
- Régression Ridge et Lasso (avec régularisation)
- Random Forest
- Gradient Boosting
- Support Vector Regression (SVR)
- Réseaux de neurones

## Métriques d'évaluation
- Erreur quadratique moyenne (MSE)
- Racine de l'erreur quadratique moyenne (RMSE)
- Erreur absolue moyenne (MAE)
- Coefficient de détermination (R²)

## Résultats clés
- Les facteurs les plus influents sur les coûts médicaux sont le statut tabagique, l'âge et l'IMC
- Les modèles de Gradient Boosting et Random Forest offrent les meilleures performances prédictives
- La précision prédictive varie significativement selon les régions géographiques

## Visualisations
Le projet comprend diverses visualisations :
- Distribution des coûts médicaux
- Corrélations entre les variables
- Impact de chaque facteur sur les coûts
- Comparaison des performances des modèles
- Importance des caractéristiques

## Applications potentielles
- Aide à la tarification des assurances santé
- Planification financière personnelle pour les dépenses médicales
- Identification des groupes à risque pour les interventions préventives
- Optimisation des programmes de bien-être et de gestion de la santé

## Travaux futurs
- Incorporer des données longitudinales pour suivre l'évolution des coûts dans le temps
- Intégrer des informations sur les conditions médicales préexistantes
- Développer des interfaces utilisateur pour rendre les prédictions accessibles aux utilisateurs finaux
- Explorer des méthodes d'interprétation des modèles plus avancées

## Contributions
Les contributions sont les bienvenues ! Pour contribuer :
1. Créez un fork du dépôt
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Committez vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Poussez vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

## Licence
Ce projet est distribué sous licence MIT. Voir le fichier `LICENSE` pour plus d'informations.

## Contact
DahliaNoir71 - [Profil GitHub](https://github.com/DahliaNoir71)

Lien du projet : [https://github.com/DahliaNoir71/Personal-Medical-Cost](https://github.com/DahliaNoir71/Personal-Medical-Cost)

## Remerciements
- Fournisseurs du jeu de données original
- Communauté open source pour les bibliothèques et outils utilisés
- Contributeurs et reviewers du projet

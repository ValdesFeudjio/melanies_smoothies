# Projet de Gestion des Commandes - Application Streamlit

## Description

Ce projet consiste en deux applications Streamlit, chacune ayant un rôle distinct, mais travaillant avec une base de données partagée afin de gérer les commandes d'un restaurant. L'objectif est de permettre aux clients de passer des commandes de manière fluide, tout en permettant aux serveurs de suivre, valider et gérer ces commandes en temps réel.

### Applications

1. **Application côté client** : 
   - Permet aux clients de passer leurs commandes en ligne.
   - Permet aux clients de voir l'état de leurs commandes (en cours, traitée, livrée).
   - Fournit une interface simple et interactive pour la sélection des produits, la personnalisation des commandes et la validation.

2. **Application côté restaurant** : 
   - Permet aux serveurs de consulter les commandes passées par les clients.
   - Permet aux serveurs de valider les commandes une fois qu'elles ont été traitées.
   - Met à jour l'état des commandes en temps réel, garantissant ainsi une gestion synchronisée entre les clients et le personnel du restaurant.

Les deux applications sont liées à la même base de données, ce qui permet une gestion cohérente et en temps réel des commandes.

---

## Technologies Utilisées

- **Python 3.x** : Le langage de programmation principal utilisé pour le développement des applications.
- **Streamlit** : Framework permettant de créer des applications interactives en Python de manière rapide et simple.
- **Base de données** : La base de données utilisée est une base relationnelle (préciser le type de base, par exemple MySQL, PostgreSQL, SQLite, etc.), utilisée pour stocker les informations sur les commandes, les utilisateurs et les produits.
- **Bibliothèques Python** :
  - `pandas` : Pour la manipulation et l'analyse des données dans les applications.
  - `SQLAlchemy` : Pour gérer les interactions avec la base de données.
  - `streamlit` : Pour la création des interfaces interactives côté client et côté restaurant.

---

## Prérequis

Avant de commencer, assurez-vous d'avoir les prérequis suivants installés sur votre machine locale :

1. **Python 3.x** :
   - Vous pouvez vérifier votre version de Python avec la commande suivante :
     ```bash
     python --version
     ```

2. **Bibliothèques Python** :
   - Installez les dépendances nécessaires en exécutant la commande suivante :
     ```bash
     pip install -r requirements.txt
     ```

3. **Base de données** :
   - Installez et configurez le serveur de base de données que vous utilisez (par exemple MySQL ou PostgreSQL).
   - Modifiez les paramètres de connexion à la base de données dans le fichier `config.py`.

---

## Installation

### 1. Clonez le projet

Clonez le repository sur votre machine locale en utilisant Git :
```bash
git clone https://votre-repository.git

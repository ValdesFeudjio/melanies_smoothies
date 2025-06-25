# Projet de Gestion des Commandes - Application Streamlit

## 🔍 Description

Ce projet comporte deux applications interactives développées avec Streamlit pour faciliter la gestion des commandes dans un restaurant. Les deux interfaces sont connectées à une **même base de données**, garantissant une expérience cohérente et en temps réel pour les clients comme pour le personnel.

### 🔗 Liens des applications

- 🛒 **Application Client – Passer une commande** :  
  👉 [Accéder à l'application client](https://melaniessmoothies-xappq43wkxa86ppwges5hpf.streamlit.app/)

- 🧾 **Application Restaurant – Gestion des commandes** :  
  👉 [Accéder à l'application restaurant](https://melaniessmoothies-xappq43wkxa86ppwges5hpf.streamlit.app/) *(à remplacer si lien différent)*

---

## 🛠️ Technologies utilisées

- **Python 3.x**
- **Streamlit** : pour créer des interfaces web interactives.
- **Base de données** : relationnelle (ex. SQLite, PostgreSQL…)
- **Bibliothèques Python** :
  - `pandas`, `SQLAlchemy`, `streamlit`, etc.

---

## 🚀 Fonctionnalités

### Application côté **Client**

- Sélection et personnalisation des produits
- Passage de commande
- Suivi de l’état en temps réel (ex. en préparation, servie)

### Application côté **Restaurant**

- Visualisation de toutes les commandes passées
- Validation des commandes prêtes
- Mise à jour instantanée du statut dans l’application client

---

## 🧱 Architecture technique

### Vue d’ensemble

```plaintext
+---------------------+        +--------------------------+
|  Application Client | <----> |  Base de Données Partagée |
+---------------------+        +--------------------------+
         ^
         |
         |
+-------------------------+
| Application Restaurant  |
+-------------------------+

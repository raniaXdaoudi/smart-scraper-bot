# Smart Scraper Bot

Un bot Python simple qui récupère automatiquement certaines informations d’une page web (titres, liens, résumés, paragraphes) à partir d’une commande écrite en français.

> Ce projet a été conçu dans un cadre **personnel** pour apprendre à structurer un bot Python, manipuler du HTML avec BeautifulSoup, et automatiser l’extraction de données à des fins exploratoires (veille, extraction structurée…).

---

## Fonctionnalités

- Interprète une commande utilisateur (ex. : "je veux les titres et les liens")
- Scrape automatiquement les balises HTML associées (`<h1>`, `<a>`, `<p>`, etc.)
- Enregistre les résultats dans un fichier CSV nommé dynamiquement :
  `scraping_titre_lien_2025-10-15.csv`
- Gère les erreurs courantes (URL invalide, contenu vide, balises absentes…)

---

## Technologies utilisées

- Python 3
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- Modules standards : `requests`, `csv`, `datetime`

---

## Installation

```bash
git clone https://github.com/votre-utilisateur/smart-scraper-bot.git
cd smart-scraper-bot
```

---

## Utilisation

```bash
python3 scrap.py
```

Répondez ensuite aux questions :
- Entrez l’URL de la page à analyser
- Décrivez ce que vous voulez récupérer
  (ex. : `titres`, `liens`, `résumés`, `paragraphe`…)

---

## Exemple

```bash
Choisissez le site à scraper : https://www.exemple.com
Que veux-tu extraire ? je veux les titres et les liens

Compris ! Je vais extraire :
- titre (balise <h1>)
- lien (balise <a> avec attribut 'href')

Fichier enregistré sous : scraping_titre_lien_2025-10-15.csv
```

---

## Structure du projet

```
smart-scraper-bot/
├── scrap.py       # Script principal (scraping et création du fichier CSV)
├── moteur.py      # Moteur d’analyse des requêtes utilisateur
├── README.md
```

---

## Améliorations futures

- Scraping quotidien automatisé
- Génération d’un journal personnel avec les données clés
- Export HTML / PDF

---

## Auteur

Projet personnel réalisé par raniaXdaoudi, dans le cadre de mon apprentissage Python et data engineering.


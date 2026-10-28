# Workspace Continuous Architecture

Bienvenue dans l'espace de travail de la communauté [Continuous Architecture](https://continuous-architecture.org).

Ce dépôt sert à travailler ensemble sur les sujets qui intéressent la communauté : notes de réflexion, brouillons d'articles, retours d'expérience, comptes rendus de sessions, propositions de pratiques, etc. Tout membre peut y lancer un sujet ou contribuer à un sujet existant.

## Organisation

Chaque sujet de travail a son propre dossier à la racine du dépôt :

```
workspace/
├── README.md                  ← ce fichier
├── architecture-decision-records/
│   ├── README.md              ← présentation du sujet (obligatoire)
│   └── ...
└── fitness-functions/
    ├── README.md
    └── ...
```

Pour nommer un dossier, utilisez des minuscules et des tirets (`mon-sujet`), sans espaces ni accents.

## Règles d'utilisation

### 1. Un dossier par sujet

Un sujet = un dossier. Avant d'en créer un, vérifiez qu'un dossier existant ne couvre pas déjà le sujet ; si c'est le cas, contribuez-y plutôt que d'en ouvrir un second.

### 2. Un `README.md` obligatoire dans chaque dossier

Chaque dossier contient au minimum un `README.md` qui présente :

- **le sujet** : de quoi il s'agit, la question traitée, l'objectif visé ;
- **les membres** qui y travaillent, et comment les contacter ;
- **l'état d'avancement** : ce qui est fait, ce qui est en cours ;
- **les prochaines étapes**.

Le modèle ci-dessous peut servir de point de départ.

### 3. Markdown de préférence

Rédigez vos documents en Markdown (`.md`). Le format se lit directement sur GitHub, se relit facilement en PR et permet de suivre l'historique des modifications ligne par ligne. Les autres formats (images, PDF, schémas) restent possibles quand le Markdown ne suffit pas, de préférence accompagnés d'un fichier `.md` qui les présente.

### 4. Pull request ou push direct

| Vous voulez...                                                    | Procédure                     |
| ----------------------------------------------------------------- | ----------------------------- |
| Créer un **nouveau dossier** de travail avec ses premiers fichiers | Push direct sur `main` autorisé |
| Modifier un **document existant**                                  | Pull request                  |
| Ajouter un fichier dans un **dossier existant**                    | Pull request                  |

La pull request permet aux membres qui travaillent déjà sur le sujet de relire et de discuter les changements avant leur intégration. Pensez à mentionner (`@pseudo`) les membres listés dans le `README.md` du dossier concerné.

## Démarrer un nouveau sujet

```bash
git clone git@github.com:continuous-architecture/workspace.git
cd workspace
mkdir mon-sujet
# créer mon-sujet/README.md à partir du modèle ci-dessous
git add mon-sujet
git commit -m "Nouveau sujet : mon sujet"
git push origin main
```

## Modèle de `README.md` pour un dossier

```markdown
# Titre du sujet

## Le sujet

De quoi parle-t-on ? Quelle question cherche-t-on à traiter, et pourquoi ?

## Membres

- Prénom Nom (@pseudo-github) : rôle ou contribution
- ...

## État d'avancement

Ce qui a été produit jusqu'ici, avec des liens vers les documents du dossier.

## Prochaines étapes

- [ ] ...
- [ ] ...

## Comment contribuer

Ce qui serait utile, où se trouvent les échanges (canal, réunions...).
```

# Consignes communes pour les agents IA

## Mission
Ce dépôt GitHub public sert à organiser des projets et des groupes de travail, et à conserver des documents Markdown relus par la communauté.

## Rédaction
- Écrire en français, avec des phrases accessibles aux débutants.
- Utiliser uniquement les informations fournies ou vérifiables ; ne jamais inventer un participant, une date, un engagement ou une décision.
- Si des détails essentiels manquent, poser des questions ou écrire explicitement « À confirmer ».
- Utiliser le modèle adapté dans `modeles/` et enregistrer les nouveaux documents dans `projets/<identifiant-du-projet>/`.
- Ne pas insérer de données personnelles, secrets, jetons, adresses privées ou contenus confidentiels.
- Ne modifier que les fichiers liés à la demande, préserver le reste du dépôt.

## Git et contribution
- Travailler sur une branche dédiée du dépôt autorisé par le contributeur (généralement son fork).
- Préparer une PR vers `main`, avec un titre et un résumé compréhensibles.
- Ne pas forcer un push vers `main`, ne pas fusionner une PR, ne pas modifier les paramètres d'accès.
- Si les permissions ne permettent pas de créer une PR inter-forks, expliquer le blocage et préparer le lien ou les instructions pour la faire manuellement dans GitHub.

## Vérification
- Contrôler lisibilité, titres, sources, cohérence et respect de la confidentialité.
- Pour les changements Markdown, exécuter `python3 scripts/check_docs.py` si l'environnement le permet.
- Les instructions ici orientent un agent ; les règles GitHub et les vérifications CI garantissent les protections effectives.

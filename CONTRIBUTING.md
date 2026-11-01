# Comment contribuer

Vous pouvez proposer une idée, créer un document ou améliorer un texte existant. Aucune connaissance en programmation ni de Git n'est nécessaire pour suivre ce guide avec un assistant IA.

Git conserve l'historique des modifications des fichiers. GitHub est le site qui héberge ces fichiers et permet de les relire ensemble. Cet ensemble de fichiers s'appelle un **dépôt**.

**Ce dépôt est public : les documents et les échanges que vous y publiez sont consultables par tous.** Ne transmettez pas de contenu confidentiel, de mot de passe, de jeton d'accès ni de coordonnées privées. Ne citez une personne qu'avec son accord.

## 1. Choisir votre contribution

- Pour échanger sur une idée, utilisez l'espace **Discussions**, s'il est disponible sur la page du dépôt.
- Pour proposer un travail ou signaler un problème, utilisez **Issues** : une issue est une demande que la communauté peut commenter et suivre.
- Pour rédiger ou corriger un texte, suivez les étapes ci-dessous.

Avant de créer un projet, regardez dans le dossier [projets/](projets/) si un projet existant couvre déjà votre sujet.

## 2. Préparer votre espace de travail

Il vous faut un compte GitHub et un assistant auquel vous pouvez donner accès à votre copie du dépôt, par exemple Codex, Claude Code ou Copilot. VS Code est un éditeur dans lequel vous pouvez travailler avec un assistant ; précisez lequel vous utilisez lorsque vous demandez de l'aide.

Les possibilités d'accès à GitHub dépendent de votre outil et de sa configuration. Vous n'avez pas besoin d'utiliser plusieurs outils.

1. Ouvrez le [dépôt de la communauté](https://github.com/continuous-architecture/workspace) sur GitHub et connectez-vous à votre compte.
2. Utilisez **Fork** pour créer une copie du dépôt sous votre compte. Cette copie, appelée **fork**, sert à préparer votre contribution.
3. Vérifiez que l'adresse de votre copie contient votre identifiant : `github.com/VOTRE-IDENTIFIANT/workspace`.
4. Dans votre outil, ouvrez ou connectez cette copie. Si l'outil parle de **cloner** le dépôt, cela signifie télécharger une copie de travail sur votre ordinateur ou dans son environnement.
5. Donnez la consigne suivante à votre assistant, en remplaçant le texte entre crochets :

> Je débute avec Git. J'utilise [nom de l'outil et de l'assistant]. Ma copie du dépôt est [adresse GitHub de mon fork]. Aide-moi à l'ouvrir dans cet outil, puis vérifie que tu travailles bien sur cette copie et que tu peux y préparer des modifications. Lis AGENTS.md. Explique simplement les étapes qui nécessitent mon intervention. Ne me demande jamais de coller un mot de passe ou un jeton dans la conversation.

**Résultat attendu :** votre assistant identifie votre copie et vous indique s'il peut la modifier. S'il n'y a pas encore accès, suivez ses indications de connexion dans l'outil. Si vous restez bloqué, utilisez la solution de secours en fin de guide.

## 3. Demander la rédaction ou la correction

Les textes sont écrits en **Markdown** : ce sont des fichiers terminant par `.md`, où `#` introduit un titre et `-` un élément de liste. Votre assistant peut s'occuper de cette mise en forme.

Une **branche** est un espace de travail séparé dans votre copie : elle regroupe les changements d'une contribution avant leur relecture. Demandez à l'assistant de la créer avant de modifier les fichiers.

Choisissez une des consignes ci-dessous et remplacez les passages entre crochets. Vous pouvez décrire votre besoin avec vos propres mots et fournir des notes publiques.

### Créer un document

> Lis AGENTS.md. Je souhaite créer [une fiche projet / un compte rendu] sur [sujet]. Voici mes informations : [notes]. Vérifie d'abord si un projet existant correspond au sujet. Utilise le modèle adapté dans modeles/ et enregistre le document dans projets/<identifiant-du-projet>/, avec un nom de dossier en minuscules et des tirets, sans espaces ni accents. Travaille sur une nouvelle branche de mon fork. Pose-moi les questions indispensables ; n'invente aucun participant, aucune date, décision ou action. Écris « À confirmer » pour les informations manquantes. Ne publie aucune donnée privée. Prépare le texte et montre-moi le résultat pour relecture avant de l'envoyer sur GitHub.

Modèles disponibles : [fiche projet](modeles/fiche-projet.md) et [compte rendu](modeles/compte-rendu.md). Vous pouvez aussi consulter le [projet d'exemple](projets/exemple-pilote/README.md), qui ne représente aucune décision officielle.

### Modifier un document existant

> Lis AGENTS.md. Je souhaite modifier [chemin ou lien du document] pour [correction ou ajout souhaité]. Voici les informations vérifiables : [notes ou sources publiques]. Travaille sur une nouvelle branche de mon fork. Préserve le reste du dépôt et ne modifie que les fichiers nécessaires. Pose-moi les questions indispensables et n'invente aucune information. Montre-moi le texte et explique les changements pour relecture avant de les envoyer sur GitHub.

## 4. Relire et vérifier

Demandez à l'assistant de vous montrer le texte mis en forme et la liste des fichiers modifiés. Vérifiez :

- que le texte est clair et correspond à votre intention ;
- que les faits et les liens vers les sources sont corrects ;
- que les décisions et les engagements ont réellement été confirmés ;
- que les personnes citées ont donné leur accord et qu'aucune information privée n'apparaît ;
- que les éléments inconnus portent la mention « À confirmer ».

Vous pouvez demander des corrections en langage courant, par exemple : « Cette décision n'a pas été prise, déplace-la dans les questions ouvertes. »

Puis donnez cette consigne :

> Lance python3 scripts/check_docs.py si ton environnement le permet. Corrige les erreurs liées à ma contribution, puis indique le résultat. Si tu ne peux pas lancer cette vérification, dis-le clairement. Ce contrôle automatique ne remplace pas ma relecture du contenu.

## 5. Envoyer votre proposition pour relecture

Une **pull request**, souvent abrégée **PR**, est une proposition de modification envoyée à la communauté. Elle permet de discuter votre texte avant de l'intégrer. La branche `main` contient la version de référence du dépôt.

Après votre relecture, donnez cette consigne :

> Enregistre les changements relus dans un commit, c'est-à-dire un point de l'historique, puis envoie la branche sur mon fork. Prépare une pull request vers main du dépôt continuous-architecture/workspace, avec un titre et un résumé simples. Vérifie qu'elle ne contient que les fichiers de ma contribution. Relie l'issue d'origine si je t'en ai fourni une. Ouvre la proposition si tes permissions le permettent et donne-moi son lien. Ne fusionne rien. Si tu ne peux pas l'ouvrir, donne-moi le lien de comparaison et les étapes pour la créer sur GitHub.

Si vous devez créer la proposition vous-même :

1. Ouvrez votre fork sur GitHub et utilisez **Contribute / Open pull request** ou **Compare & pull request**, selon ce qui est proposé.
2. Vérifiez la destination : dépôt `continuous-architecture/workspace`, branche `main`. La source doit être votre fork et la branche créée pour votre contribution.
3. Relisez la liste des fichiers et les modifications. En cas de doute, copiez votre question dans l'assistant, sans information privée.
4. Renseignez un titre et un résumé, puis créez la pull request.

**Résultat attendu :** vous disposez d'un lien vers une pull request dans le dépôt de la communauté. Sa création signifie que votre texte est proposé à la relecture ; son intégration reste à faire.

## 6. Suivre la relecture

Consultez les commentaires sur la page de votre pull request. Pour y répondre, vous pouvez demander à votre assistant de corriger le texte sur la même branche et d'envoyer les corrections : elles compléteront la proposition existante.

Un référent autorisé pourra **fusionner** la proposition, c'est-à-dire intégrer les modifications à la version de référence, après approbation. Ne la fusionnez pas vous-même si vous n'êtes pas référent autorisé.

## Si vous êtes bloqué ou sans assistant compatible

Vous pouvez proposer votre texte directement dans une **Issue** du dépôt de la communauté : indiquez le sujet, le document concerné s'il existe et votre proposition. Demandez de l'aide pour la publication. Cette demande est elle aussi publique.

Si vous savez déjà utiliser l'éditeur de fichiers de GitHub, vous pouvez également modifier un document dans votre fork et suivre son parcours de proposition de modification.

## Règles communes

- Une proposition doit porter sur un sujet précis.
- Utilisez les modèles et le dossier projets/ pour les nouveaux documents.
- Préparez les modifications sur une branche dédiée et soumettez-les à relecture vers main.
- N'ajoutez pas d'instructions d'agent, de secrets ou de fichiers exécutables sans rapport avec la contribution.
- Relisez toujours le contenu produit par une IA avant de le publier.

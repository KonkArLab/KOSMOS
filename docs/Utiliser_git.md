## Formation Git 

### Initier un git

 - git init est une commande qui permet d'initier un git
 - A la base le dépôt est vide
 - Écrire des choses dans un fichier. (Modifier ce qui est dans le dossier de GIT)
 - git add permet d'indiquer une modification de sauvegarde. "Maintenant j'observe les fichiers à observer"
 

### Sauvegarder le Git
 - git commit : sauvegarder les modifications apportées. "Va aller dans les fichiers à observer et va enregistrer les modifications qui ont été faites"
 - Sauvegarder une version (git tag). Nomme un nom de commit en nom de version


### Travail en parallèle

 - git branch, sauvegarder plusieurs modifications à partir d'une version. 
 - git checkout pour changer de branche (ajouter argument branche ou master).
 - git merge : remettre le contenu d'une branche se remet dans la branche principale. La branche continue à exister 
 - On ne fait pas de commit sur la branche master (en général en informatique)
 - Chaque contributeur travail indépendamment sur une branche
 - le merge fait comme un commit (ce qui fait qu'il peut demander de résoudre des conflits)
 - Ce qui veut dire qu'il faut tout de même se coordonner et ne pas travailler sur le même fichier. 
 

### Préparer un répertoire en ligne

 - git remote configurer une destination à distance (remote) pour le git
 - git push envoie la version actuelle vers le répertoire distant. On peut faire cela par branche (se positionner (checkout) et pousser juste une branche)
 - git pull tirer ce qui est en ligne (mais il faut déjà un git en local)
 - git clone pour copier un répertoire sur un git en ligne
 
`

### Setup
 - git config --global user?name "[firstname lastname]"
 
 

### Liens connexes
 - les commandes de git : https://education.github.com/git-cheat-sheet-education.pdf
 
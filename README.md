# Guide d'utilisation du Script de Mise en forme des rapports d'espionnage

Ce guide vous expliquera comment télécharger, configurer et utiliser le script miseEnPageSpy 
## Téléchargement du Script

1. Cliquez sur le bouton "Code" en haut de cette page.
2. Sélectionnez "Download ZIP" pour télécharger le code source du script sur votre ordinateur.

## Prérequis

Avant d'utiliser le script, assurez-vous d'avoir Python installé sur votre ordinateur.
Normalement, si vous utilisez une distribution linux, Python est déjà installé dans votre système.
Si ce n'est pas le cas, suivez ces étapes :

1. Téléchargez Python depuis le site officiel : [python.org/downloads](https://www.python.org/downloads/).
2. Lancez l'installateur Python téléchargé.
3. Cochez la case "Add Python to PATH" lors de l'installation pour faciliter l'accès à Python.
4. Suivez les instructions pour terminer l'installation.

## Installation du Script

1. Extrayez le contenu du fichier ZIP que vous avez téléchargé.
2. Placez le rapport d'espionnage dans un fichier texte nommé  ```rapport.txt``` dans le même répertoire que le script Python.

## Utilisation du Script

1. Ouvrez un terminal (invite de commandes) sur votre ordinateur. Sur Windows, vous pouvez le trouver en recherchant "cmd" ou "Invite de commandes" dans le menu Démarrer. Sur macOS ou Linux, vous pouvez utiliser le Terminal.

2. Naviguez vers le répertoire où vous avez placé le script et le fichier "rapport.txt" à l'aide de la commande `cd` :

   ```
   cd chemin/vers/le/dossier
   ```

3. Exécutez le script en utilisant la commande suivante :

   ```
   python miseEnPageSpy.py
   ```
   ou
   ```
   python3 miseEnPageSpy.py
   ```
   Si vous utilisez une distribution linux.

5. Le script parcourra le rapport d'espionnage, appliquera la mise en page et créera un fichier de sortie par défaut appelé "rapport_mis_en_page.txt".

6. Ouvrez le fichier de sortie "rapport_mis_en_page.txt" et copiez-collez son contenu dans Apo.

## Licence

Ce script est distribué sous la licence GPL-3.0. Pour plus d'informations sur la licence, consultez : [Licence GPL-3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).

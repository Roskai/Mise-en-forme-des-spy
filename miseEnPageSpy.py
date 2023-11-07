###########################################
# Mise en forme des rapports d'espionnage #
###########################################
# Ce script en Python permet de parcourir un fichier texte, appliquer une mise en page selon les conditions spécifier en forum
# et écrire le résultat dans un fichier de sortie au format BBCode.

# Auteur : Roskaï
# Licence : Ce script est sous licence GPL-3.0. Pour plus d'informations sur la licence, consultez :
# https://www.gnu.org/licenses/gpl-3.0.fr.html


# Ouvrir le fichier en mode lecture
nom_fichier = "rapport.txt"

#Ouvrir pour écriture le fichier de retour
nom_fichier_ecriture = "rapport_mis_en_page.txt"

liste_unite_offensive = {
    "canons ",
    "chasseurs",
    "frégates",
    "corvettes",
    "croiseurs impériaux",
}

liste_croiseur_bombardier = {
    "croiseurs bombardiers ioniques",
    "croiseurs bombardiers hyperatomiques",
    "croiseurs bombardiers ADM",
}

# Couleurs
couleur_titre = "#FFA500"
couleur_offensif = "#AA0000"
couleur_bombardier = "#F551FF"
couleur_speciaux = "#FF0000"

try:
    with open(nom_fichier, "r") as fichier:
        with open(nom_fichier_ecriture, "w") as file_out:
            for ligne in fichier:
                if "Système 20." in ligne:
                    formatted_line = f"\n[b][color={couleur_titre}]{ligne.strip()}[/color][/b]\n"
                else:
                    # Parcourir la liste des unités offensives
                    for unite in liste_unite_offensive:
                        if unite in ligne:
                            ligne = f"[color={couleur_offensif}]{ligne.strip()}[/color]\n"
                            break  # Sortir de la boucle dès qu'une unité est trouvée
                    # Parcourir la liste des croiseurs bombardiers
                    for croiseur in liste_croiseur_bombardier:
                        if croiseur in ligne:
                            ligne = f"[color={couleur_bombardier}]{ligne.strip()}[/color]\n"
                            break  # Sortir de la boucle dès qu'un croiseur bombardier est trouvé

                    # Vérifier les unités militaires spécifiques
                    if "escadres kamikazes" in ligne or "chasseurs Arks" in ligne:
                        # Appliquer la mise en page en couleur violette (#F551FF)
                        formatted_line = f"[color={couleur_speciaux}]{ligne.strip()}[/color]\n"
                    else:
                        # Aucune mise en page spécifique, conserver la ligne telle quelle
                        formatted_line = ligne
                # Écrire la ligne formatée dans le fichier de sortie
                file_out.write(formatted_line )
except FileNotFoundError:
    print(f"Le fichier d'entrée'{nom_fichier}' n'existe pas.")
except Exception as e:
    print(f"Une erreur s'est produite : {str(e)}")

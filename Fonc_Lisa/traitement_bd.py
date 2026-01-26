import os
import pandas
import csv
import random

# print("Dossier courant :", os.getcwd()) # Pour savoir où on est
# print("Contenu du dossier :", os.listdir()) # Pour savoir ce qu'il y a avec nous

# print("poulpe")
pokedex = [] # array
win = 0

with open("Fonc_Lisa/pokemon_data.csv", newline='', encoding="utf-8") as fichier:
    test = csv.reader(fichier, delimiter=",")
    for ligne in test:
        #print(ligne)
        #print("\n")
        pokedex.append(ligne) # On ouvre le fichier csv et on ajout manuellement toutes les lignes dans l'array
    
    # print(type(pokedex))
    print(pokedex[0]) # On affiche pour être sûr
    # print(pokedex[58])

# choix du pokemon "mystère"
n_pkmn_mystere = random.randint(1, 1025) # On choisis un numéro entre 1 et 1025, ce qui choisis le numéro du pokemon "mystère"
print(pokedex[n_pkmn_mystere])

while not win:
    # L'utilisateur choisis un pokemon, pour deviner le pokemon mystère
    n_pkmn_guest = int(input("Try : "))
    print(pokedex[n_pkmn_guest])

    if n_pkmn_guest == n_pkmn_mystere :
        print("Tu as gagner ! C'était bien " + str(pokedex[n_pkmn_mystere][1]))
        win = 1
    else :
        print("Essaie encore")
import os
import pandas
import csv
import random

print("Dossier courant :", os.getcwd())
print("Contenu du dossier :", os.listdir())


print("poulpe")
pokedex = []

with open("Fonc_Lisa/pokemon_data.csv", newline='', encoding="utf-8") as fichier:
    test = csv.reader(fichier, delimiter=",")
    for ligne in test:
        #print(ligne)
        #print("\n")
        pokedex.append(ligne)
    
    # print(type(pokedex))
    # print(pokedex[0])
    # print(pokedex[1])

n_pkmn_mystere = random.randint(1, 1025)
print(pokedex[n_pkmn_mystere])
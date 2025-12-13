import os

argomenti= []
routine = []

percorso = os.getcwd()
percorso += "/Allexercises.csv"

with open(percorso, "r") as my_file:
    for line in my_file:
        argomenti.append(line)

for pos_y in range(0, len(argomenti)):
    argomenti[pos_y] = argomenti[pos_y][:-1]


percorso = os.getcwd()
percorso += "/mie_soluzioni.txt"
with open(percorso, "r") as my_file:
    for line in my_file:
        routine.append(line)


percorso = os.getcwd()
percorso += "/tutti.txt"
with open(percorso, "w") as my_file:
    pos_y = 0

    for pos_y in range(0, len(routine)):
        my_file.write(str(argomenti[pos_y] + ";" + str(routine[pos_y])))

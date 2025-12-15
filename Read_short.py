import os

percorso = "C:/Users/User/AppData/Local/tmc/vscode/mooc-programming-25"
dire_list = []
soluzioni = []

# for directory in os.scandir(percorso):
#     dire_list.append(directory.name)

# dire_list = dire_list[1:]

start = True
for directory in os.scandir(percorso):
    if start == False:
        subpercorso = percorso + "/" + directory.name + "/src"
        #print(f"{subpercorso} : ", end="")
        if directory.name != "web_programming":
            for subdirectory in os.scandir(subpercorso):
                #print(f"{subpercorso} {subdirectory.name}, ", end="")
                if subdirectory.is_file():
                    print(subdirectory.name[-2:], end=" ")
                    if str(subdirectory.name[-2:]) == "py":
                        soluzione = ""
                        #print(subpercorso + "/" + subdirectory.name)
                        with open((subpercorso + "/" + subdirectory.name), "r") as my_file:
                            #soluzione = my_file.readlines()
                            for line in my_file:
                                soluzione += my_file.readline() + "\n"

            print(directory.name, len(soluzione))
            soluzioni.append([directory.name, soluzione, len(soluzione)])


    start = False
with open("elenco.txt", "w", encoding="utf-8") as my_file:
    for esercizio in soluzioni:
        my_file.write(f"{esercizio[0]}, {esercizio[1]} {esercizio[2]}\n")

with open("matrice_elenco.txt", "w", encoding="utf-8") as my_file:
    my_file.write(str(soluzioni))



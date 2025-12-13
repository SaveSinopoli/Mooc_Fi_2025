import os
#editato su desktop studio
class Percorsi:

    def __init__(self, percorso: str):
        #self.percorso = percorso
        self.percorso = "C:/Users/saves/AppData/Local/tmc/vscode/mooc-programming-25"
        self.directory = []
        self.soluzioni = []
        self.sezione = []

    def carica(self):
        try:
            self.directory = os.listdir(self.percorso)
            del self.directory[-1]
            del self.directory[0]
            self.__soluzioni(self.soluzioni)
            return self.directory
        except FileNotFoundError:
            print("La directory specificata non esiste.")
            return "La directory specificata non esiste."
        except PermissionError:
            return "Permesso negato per accedere a questa directory."

    def __soluzioni(self, soluzioni):
        for nome in self.directory:
            self.sezione.append([nome[4:6], nome[7:9], nome[10:]])
            controllo = nome[10:]
            if controllo[0] in "._":
                controllo = controllo[1:]
            new_percorso = self.percorso + "/" + nome + "/src/" + controllo + ".py"
            try:
                with open(new_percorso, "r", encoding="utf-8") as my_file:
                    self.soluzioni.append(my_file.readlines())
            except FileNotFoundError:
                print(f"File non trovato: {new_percorso}")
                self.soluzioni.append(["File non trovato."])


    def get_soluzioni(self):
        return self.soluzioni

    def get_sezione(self):
        return self.sezione

    def __str__(self):
        return f"eserczi(percorso='{self.percorso}', directory={self.directory})"
    def __repr__(self):
        return f"{self.percorso}{self.directory}"



if __name__ == "__main__":
    # percorso = input("Inserisci il percorso della directory: ")
    percorso = "C:/Users/saves/AppData/Local/tmc/vscode/mooc-programming-25"
    direct = Percorsi(percorso)
    lista = direct.carica()
    sezione = direct.get_sezione()
    soluzioni = direct.get_soluzioni()

    print(f"Nomi dei file nella directory {direct.percorso} ({len(lista)}):")

    with open(os.getcwd()+"/mie_soluzioni.txt", "w", encoding="utf-8") as my_file:
        y_pos =0
        for y_pos in range(0, len(soluzioni)):
            stringa = str(soluzioni[y_pos])
            stringa = stringa[1:]
            stringa = stringa[:-1]
            stringa += "\n"
            my_file.write(stringa)
            y_pos += 1

    print(f"soluzione salvata in {os.getcwd()}\\mie_soluzioni.txt")


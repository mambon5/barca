import random

def genera_grups_random(total_seients_disponibles):
    # donats el nombre total de seients disponibles,crea grups de usuaris de diferents tamanys

    # Inicialitzem un diccionari per emmagatzemar el nombre de grups per tipus
    grups_per_tipus = {1: 0, 2: 0, 3: 0, 5: 0, 7: 0, 19: 0}

    # Generem grups aleatòriament fins que no quedin més seients disponibles
    while total_seients_disponibles > 0:
        # Trieu aleatòriament la mida del grup (1, 2, 3, 5 o 7)
        mida_grup = random.choice([1,1, 2,2, 2, 3, 3, 5, 5, 7,7, 19])
        
        # Comprovem si hi ha prou seients per al grup
        if total_seients_disponibles >= mida_grup:
            grups_per_tipus[mida_grup] += 1
            total_seients_disponibles -= mida_grup
        else:
            break

    # Mostrem la quantitat de grups per tipus
    for mida, quantitat in grups_per_tipus.items():
        print(f"Grups de {mida} persones: {quantitat}")

    # Comprovem si queden seients sense assignar
    if total_seients_disponibles > 0:
        print(f"Queden {total_seients_disponibles} seients sense assignar.")

    return grups_per_tipus

def assignar_seients(grups, num_files, seients_per_fila):
    print("Estadi amb {} files de {} seients cadascuna".format(num_files, seients_per_fila))
    fila_actual = 0
    assignats_per_fila = 0
    fila = [[] for _ in range(num_files)]

    # Ordenem els grups de major a menor tamany
    grups_ordenats = sorted(grups.items(), reverse=True)
    grups_ordenats = list(map(list, grups_ordenats))

    while fila_actual < num_files and grups_ordenats:
        fila_plena = False

        grup_index=0
        for tamany, quantitat in grups_ordenats[:]:
            while quantitat > 0:
                if assignats_per_fila < seients_per_fila:
                    if assignats_per_fila < seients_per_fila - tamany + 1: # podem assignar "tamany" persones a la fila
                        fila[fila_actual].append(tamany)
                        assignats_per_fila += tamany
                        quantitat -= 1
                        grups_ordenats[grup_index][1] -= 1
                    else: # hem d'assignar un grup de menor tamany perquè hi càpiguen
                        break
                    
                elif assignats_per_fila == seients_per_fila:
                    fila_plena = True
                    break
                else:
                    raise Exception("Error, s'han assignat més seients dels que hi caben!") 
                
                

            if fila_plena:
                break
                
            grup_index +=1 

        fila_actual += 1
        assignats_per_fila = 0

    return fila

def print_files(resultat): # print the capacity of each row
    suma = map(sum,resultat)
    resi=list(suma)
    print("ocupació de cada fila:")
    print(resi)
    return(resi)

# Exemple d'ús amb la quantitat de grups donada
files=100
seients_per_fila=500
grups = genera_grups_random(files*seients_per_fila)

resultat = assignar_seients(grups, files, seients_per_fila)
print_files(resultat)

# comprovant grups i resultats de l'assignació:
print("grups:")
print(grups)
# print("resultat de l'assignació per grups:")
# print(resultat)





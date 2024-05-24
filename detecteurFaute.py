def ouvrirFichier(fichier):
    return open(fichier)
    #return fichiers


def compteurLigne(fichier):
    compteur = 0
    for ligne in fichier:
        compteur = compteur + 1
    return compteur
def afficherContenue(fichier):
    for ligne in fichier:
        print(ligne)
def compteurChevronOuvrant(fichier):
    compteur = 0
    for ligne in fichier:
        for l in list(ligne):
            if l == '<':
                compteur = compteur + 1
    return compteur
def compteurChevronFermant(fichier):
    compteur = 0
    for ligne in fichier:
        for l in list(ligne):
            if l == '>':
                compteur = compteur + 1
    return compteur

def nombreLigneBody(fichier):
    compteur = 0
    tempo = ''
    for ligne in fichier:
        for caractere in list(ligne):
            if(tempo != 'body'):
                if caractere == 'b':
                    tempo = tempo + caractere
                elif caractere == 'o':
                    tempo = tempo + caractere
                elif caractere == 'd':
                    tempo = tempo + caractere
                elif caractere == 'y':
                    tempo = tempo + caractere
        
        if  tempo == 'body':
            compteur = compteur + 1
        if tempo != 'body':  
            tempo = ''
    return compteur - 1
            
           

fichier = ouvrirFichier('exemple.html')
print('=========================Lignes totales de mon fichier====================================')
print(compteurLigne(fichier))
fichier.close
fichier = ouvrirFichier('exemple.html')
print("====================Chevron Ouvrant===========================")
print(compteurChevronOuvrant(fichier))
fichier.close
fichier = ouvrirFichier('exemple.html')
print("=========================Chevron fermant======================================")
print(compteurChevronFermant(fichier))
fichier.close
fichier = ouvrirFichier('exemple.html')
print("=========================Nombre des lignes dans la balise body=====================================")
print(nombreLigneBody(fichier))

#afficherContenue(fichier)
#print(compteurLigne(fichier))
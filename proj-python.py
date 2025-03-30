import json
import os

# ------------- INITIALISATION -------------- #
with open('eleves.json', 'r') as file:
    data = json.load(file)
    
# Je pense que c'est mieux de mettre les filieres dans un fichier json


# ------------- ADMIN -------------- #

def menu_principal():
    os.system('cls')
    print('1. Connection tant que Eleve.')
    print('2. Connection tant que Administrateur.')
    n = int(input('Donner l\'ordre : '))
    if n==1:
        os.system('cls')
        menu_eleve(eleve=call_eleve())
    elif n==2:
        os.system('cls')
        menu_admin()
    else:
        os.system('cls')
        menu_principal()

def menu_admin():
    print('1 . Ajouter un eleve')
    print('2 . Editer les donnes d\'un eleve')
    print('3 . Supprimer un eleve')
    print('4 . Afficher le classement des eleves')
    print('5 . Afficher les Filieres')
    print('6 . Ajouter une Filiere')
    print('7 . Supprimer une Filiere')
    print('8 . Affecter les eleves aux filieres')
    print('9 . Deconnection')
    n = int(input('Donner l\'ordre : '))
    if n==1:
        os.system('cls')
        ajouter_eleve()
    elif n==2:
        os.system('cls')
        editer_eleve()
    elif n==3:
        os.system('cls')
        supprimer_eleve()
    elif n==4:
        os.system('cls')
        afficher_classement()
    elif n==5:
        os.system('cls')
        afficher_filieres()
    elif n==6:
        os.system('cls')
        ajouter_filiere()
    elif n==7:
        os.system('cls')
        supprimer_filiere()
    elif n==8:
        os.system('cls')
        affecter_eleves_filiere(1)
        return_menu_principal()
    elif n == 9:
        menu_principal()
    else:
        os.system('cls')
        menu_admin()

def return_menu_principal():
    print('---------------------------------')
    print('1. Retourner au Menu Principal')
    n = int(input('Donner l\'ordre : '))
    if n==1:
        os.system('cls')
        menu_admin()
    else:
        return_menu_principal()


def check_id(id):
    for i in range(len(data)):
        if data[i]['id'] == id:
            return True
    return False
def classment_eleve(data):
        #TRIER LES ELEVES PAR ORDRE DECROISSANT
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[i]['note_final'] < data[j]['note_final']:
                data[i], data[j] = data[j], data[i]
    return data
def ajouter_eleve():
    os.system('cls')
    print("Vous choisisez d'ajouter un eleve")
    id = int(input("Donner l'ID de l'eleve : "))
    if(check_id(id)):
        print("L'eleve existe deja")
        ajouter_eleve()
    name = input("Donner le nom complet de l'eleve : ")
    note = float(input("Donner la note de l'eleve : "))
    filieres = ['INDIA', 'GBM', 'IAA'] # SUGGESTION DES FILLIERES PAR DEFAUT
    data.append({'id': id, 'NomComplet': name, 'note_final': note, 'liste_filliere_voulu': filieres})
    with open('eleves.json', 'w') as file:
        json.dump(data, file)
        print("L'eleve a ete ajoute avec succes")
        return_menu_principal()
def editer_eleve( ):
    os.system('cls')
    print("Vous choisisez d'editer les donnes d'un eleve")
    id = int(input("Donner l'ID de l'eleve : "))
    if check_id(id): 
        for i in range(len(data)):
            if data[i]['id'] == id:
                eleve = data[i]
                break
        print("L'eleve a editer est : ", eleve['NomComplet'], " : ", eleve['note_final'])
        name = input("Donner le nom complet de l'eleve : ")
        note = float(input("Donner la note de l'eleve : "))
        eleve['NomComplet'] = name
        eleve['note_final'] = note
        with open('eleves.json', 'w') as file:
            json.dump(data, file)
            print("L'eleve a ete edite avec succes")
def supprimer_eleve():
    os.system('cls')
    print("Vous choisisez de supprimer un eleve")
    id = int(input("Donner l'ID de l'eleve : "))
    if check_id(id):
        for i in range(len(data)):
            if data[i]['id'] == id:
                eleve = data[i]
                break
        data.remove(eleve)
        with open('eleves.json', 'w') as file:
            json.dump(data, file)
            print("L'eleve a ete supprime avec succes")
    else:
        print("L'eleve n'existe pas")
        menu_admin()
def afficher_classement():
    os.system('cls')
    print("Le classement des eleves est : ")
    datas = classment_eleve(data)
    
    for i in range(len(datas)):
        print( i+1, "\t", datas[i]['NomComplet'], "\t-\t", datas[i]['note_final'])
    return_menu_principal()
def afficher_filieres():
    os.system('cls')
    print("Les filieres sont : ")
    with open('filieres.json', 'r') as file:
        filieres = json.load(file)
    for i in range(len(filieres[0]['filieres'])):
        print(filieres[0]['filieres'][i]['nomFiliere'], " - Nb de places offertes : ", filieres[0]['filieres'][i]['NbPlace'])
    return_menu_principal()
def ajouter_filiere():
    os.system('cls')
    print("Vous choisisez d'ajouter une filiere")
    with open('filieres.json', 'r') as file:
        filieres = json.load(file)
    print("Voici les fillieres existentes : ")
    for i in range(len(filieres[0]['filieres'])):
        print(filieres[0]['filieres'][i]['nomFiliere'], " - Nb de places offertes : ", filieres[0]['filieres'][i]['NbPlace'])
    nom = input("Donner le nom de la filiere : ")
    nb = int(input("Donner le nombre de places offertes : "))
    filieres[0]['filieres'].append({'nomFiliere': nom, 'NbPlace': nb})
    with open('filieres.json', 'w') as file:
        json.dump(filieres, file)
        print("La filiere a ete ajoute avec succes")
    return_menu_principal()
def supprimer_filiere():
    print("Vous choisissez de supprimer une filière")
    
    try:
        # Chargement des filières depuis le fichier JSON
        with open('filieres.json', 'r') as file:
            filieres = json.load(file)
        
        vari = filieres[0].get('filieres', [])
        
        # Affichage des filières existantes
        print("Voici les filières existantes :")
        for filiere in vari:
            print(f"{filiere['nomFiliere']} - Nb de places offertes : {filiere['NbPlace']}")
        
        # Demander le nom de la filière à supprimer
        nomf = input("Donner le nom que vous souhaitez supprimer : ")
        
        # Recherche et suppression de la filière
        for filiere in vari:
            if nomf == filiere['nomFiliere']:
                vari.remove(filiere)
                with open('filieres.json', 'w') as file:
                    json.dump(filieres, file, indent=4)
                print("La filière a été supprimée avec succès.")
                return_menu_principal()
                return
        
        # Si la filière n'a pas été trouvée
        print("Cette filière n'existe pas.")
    
    except FileNotFoundError:
        print("Le fichier filieres.json n'existe pas.")
    except json.JSONDecodeError:
        print("Erreur de lecture du fichier JSON.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
    
    return_menu_principal()

            
def afficher_affectation_loop(id, nom, filiere):
    print({'id': id, 'NomComplet': nom, 'filiere': filiere})
def affecter_eleves_filiere(n=0):
    with open('filieres.json', 'r') as file:
        filieres = json.load(file)
    affectation = []
    # Initialiser les places restantes pour chaque filiere avec le nombre de places offertes depuis le fichier filieres.json
    Listes_places_restantes = {
        'INDIA': filieres[0]['filieres'][0]['NbPlace'],
        'GBM': filieres[0]['filieres'][1]['NbPlace'],
        'IAA': filieres[0]['filieres'][2]['NbPlace']
    }


    for etudiant in classment_eleve(data):
        for fil in etudiant['liste_filliere_voulu']:
            # chercher si la filiere existe dans la liste des filieres voulu par l'eleve
            if fil in Listes_places_restantes and Listes_places_restantes[fil] > 0:
                Listes_places_restantes[fil] -= 1  # decrementer le nombre de places restantes
                affectation.append({'id': etudiant['id'], 'NomComplet': etudiant['NomComplet'], 'filiere': fil})
                
                if n == 1 :
                    afficher_affectation_loop( etudiant['id'], etudiant['NomComplet'], fil)
                
                break  # passer a l'eleve suivant
    if n == 1 :
        print("Les eleves ont ete affectes avec succes")
        print(Listes_places_restantes)           
    
     # Sauvegarder les affectations dans un fichier json
    with open('affectation.json', 'w') as file:
        json.dump(affectation, file, indent=4)  # indent=4 pour formater le fichier json

## ----------------- Eleves ----------------- ##
def call_eleve():
    os.system('cls')
    id = int(input("Bienvenue, Donner votre ID : "))
    if check_id(id):
       for i in range(len(data)):
           if data[i]['id'] == id:
               return data[i]
           #initialiser une session pour l'eleve
    else:
        call_eleve()
def menu_eleve(eleve):
    os.system('cls')
    print('Bienvenue ',eleve['NomComplet'],' Dans votre Menu Eleve')
    print('1 . Afficher Mon classement')
    print('2 . Afficher mon classement filieres')
    print('3 . Editer mon classement filiere')
    print('4 . Afficher la filiere affecter')
    print('5 . Deconnection')
    n = int(input('Donner l\'ordre : '))
    if n==1:
        afficher_eleve_classement(eleve)
    elif n==2:
        afficher_eleve_classement_filiere(eleve)
    elif n==3:
        editer_eleve_classement_filiere(eleve)
    elif n == 4:
        afficher_filiere_affecter(eleve)
    elif n == 5:
        menu_principal()
    else:
        # Si 'n' n'est pas dans les choix, on rappelle le menu_eleve
        menu_eleve(eleve)
def admissible(eleve):
    with open('affectation.json', 'r') as file:
        affectation = json.load(file)
    for i in range(len(affectation)):
        if affectation[i]['id'] == eleve['id']:
            return True
    return False
def return_menu_principal_eleve(eleve):
    print('---------------------------------')
    print('1. Retourner au Menu')
    print('2. Retourner au Menu Principal')
    n = int(input('Donner l\'ordre : '))
    if n==1:
        menu_eleve(eleve)
    elif n==2:
        os.system('cls')
        menu_principal()
    else:
        return_menu_principal_eleve(eleve)
def afficher_eleve_classement(eleve):
    os.system('cls')
    print('Nom : ', eleve['NomComplet'])
    print('Note : ', eleve['note_final'])
    dataas = classment_eleve(data)
    for i in range(len(dataas)):
        if dataas[i]['id'] == eleve['id']:
            print('Votre classement est : ', i+1)
            break
    return_menu_principal_eleve(eleve)
def afficher_filieres_eleve(eleve):
    print("Votre classement des filiere est : ")
    for i in range(len(eleve['liste_filliere_voulu'])):
        print(i+1, " - ", eleve['liste_filliere_voulu'][i])
    

def afficher_eleve_classement_filiere(eleve):
    os.system('cls')
    print('Nom : ', eleve['NomComplet'])
    print('Note : ', eleve['note_final'])
    afficher_filieres_eleve(eleve)
    return_menu_principal_eleve(eleve)

def editer_eleve_classement_filiere(eleve):
    os.system('cls')
    print('Nom : ', eleve['NomComplet'])
    print('Note : ', eleve['note_final'])
    afficher_filieres_eleve(eleve)
    fil = int(input("Donner le numero de la filiere que vous souhaite editer : "))
    replaced_fil = int(input("Donner le numero de la filiere que vous souhaite remplacer : "))
    old_fil = eleve['liste_filliere_voulu'][fil-1]
    eleve['liste_filliere_voulu'][fil-1] = eleve['liste_filliere_voulu'][replaced_fil-1]
    eleve['liste_filliere_voulu'][replaced_fil-1] = old_fil
    with open('eleves.json', 'w') as file:
        json.dump(data, file)
        print("Votre classement a ete edite avec succes")
        affecter_eleves_filiere()
    return_menu_principal_eleve(eleve)

def afficher_filiere_affecter(eleve):
    affecter_eleves_filiere()
    os.system('cls')
    print('Nom : ', eleve['NomComplet'])
    print('Note : ', eleve['note_final'])
    afficher_filieres_eleve(eleve)
    if admissible(eleve):
        print("Felicitation, Vous etes admis")
        with open('affectation.json', 'r') as file:
            affectation = json.load(file)
        for i in range(len(affectation)):
            if affectation[i]['id'] == eleve['id']:
                print("Affectation a la filliere : ",affectation[i]['filiere'])
                break
    else:
        print("Vous n'etes pas admissible")
    return_menu_principal_eleve(eleve)
    
menu_principal()
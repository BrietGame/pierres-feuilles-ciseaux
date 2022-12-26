import time
import items

def intro():
    print("Bonjour toi ! Peux-tu me dire ton nom ?")
    name = input()
    print("Oh, enchanté " + name + " !")
    print("Moi je suis Ted et je suis là pour te battre à Pierres, Feuilles, Ciseaux !")
    print("Si t'arrive à gagner, tu auras le droit à une surprise ! Et si tu perds, tu pourras rejouer si t'en as la force.")
    print("Veux-tu jouer avec moi ?")
    isPlay(input())

def startGame():
    print("Let's go !")

def quitGame():
    print("A très vite !")
    exit()

def isPlay(choice):
    if (choice == "Oui"):
        explainGame()
    else:
        quitGame()

def explainGame():
    print("Je t'explique les règles si tu es nouveau :")
    print("Tu dois choisir entre PIERRE, FEUILLE et CISEAUX")
    print("Un compte à rebours aura lieu et tu devras réfléchir à la réponse que tu donnes.")
    print("Cette dernière je ne la verrais seulement quand j'aurais déposé ma réponse en simultané après le compte à rebours.")
    isOk = input("As-tu compris les règles et es-tu prêt à jouer ?")
    round()

def winComputer():
    print("J'ai gagné !!")
    print("Mais je ne suis pas contre une revanche !")
    isPlay(input("Veux-tu rejouer ?"))

def winUser():
    print("Bravo, tu as gagné...")
    print("Mais je ne suis pas contre une revanche !")
    isPlay(input("Veux-tu rejouer ?"))

def checkChoices(userChoice, computerChoice):
    if (userChoice == computerChoice.name):
        print("Egalité !")
        round()
    elif (userChoice == "PIERRE" and computerChoice.name == "FEUILLE"):
        winComputer()
    elif (userChoice == "FEUILLE" and computerChoice.name == "CISEAUX"):
        winComputer()
    elif (userChoice == "CISEAUX" and computerChoice.name == "PIERRE"):
        winComputer()
    elif (userChoice == "PIERRE" and computerChoice.name == "CISEAUX"):
        winUser()
    elif (userChoice == "FEUILLE" and computerChoice.name == "PIERRE"):
        winUser()
    elif (userChoice == "CISEAUX" and computerChoice.name == "FEUILLE"):
        winUser()
    else:
        return False

def round():
    print("Attention, le jeu va commencer !")
    print("A 0, vous devrez donner votre réponse.")
    time.sleep(1)
    print("5")
    time.sleep(1)
    print("4")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("0")
    userChoice = input("Ton choix : ")
    computerChoice = items.getRandomItem()

    if (checkChoices(userChoice, computerChoice) == False):
        print("Choisis entre PIERRE, FEUILLE et CISEAUX !")
        round()
    else:
        print("J'ai choisi " + computerChoice.name + " et tu as choisi " + userChoice)
        checkChoices(userChoice, computerChoice)

# Launch function
intro()
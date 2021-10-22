# @gregoiremahon - contact : greg.mahonfr@gmail.com

# Découverte de Python
# Jeu de Pierre Feuille Ciseaux (Rock Paper Cisors)
# Règles : Les deux joueurs jouent un item (soit Pierre (Rock), Feuille (Paper), ou ciseaux (Cisors)). Les items des deux joueurs sont comparés, et le joueur ayant sélectionné l'item le plus fort devant l'autre gagne.
# Classification des items :
# Paper l'emporte devant Rock 
# Cisors l'emporte devant Paper
# Rock l'emporte devant Cisors
# Si les deux items des deux joueurs sont les mêmes, alors il y a égalité. 


from random import *
 
def userSelection():
    
    player = input("Rock\nPaper\nCisors\n") # Le joueur sélectionne l'item qu'il veut jouer (Pierre, feuille ou ciseaux)
    while player not in ["Rock","Paper","Cisors"]:
        player = input("Rock\nPaper\nCisors\n")
    return(player) # Renvoie la sélection du joueur
 
def botSelection(): # Choix aléatoire de l'ordinateur
    
    n = randint(1,3) # Choix aléatoire entre pierre (1), feuille (2) ou ciseaux (3)
    if n == 1:
        bot = "Rock"
    elif n==2:
        bot = "Paper"
    else:
        bot = "Cisors"
    return(bot) # Renvoie la sélection aléatoire du bot
 
a = userSelection()
b = botSelection()
print(b) # Affiche la sélection du bot


# Partie détermination du vainqueur


if a == "Rock" and b == "Cisors":
    print("You WON !")
    
elif a == "Rock" and b == "Paper":
    print("LOSER !")
    
elif a == "Rock" and b == "Rock":
    print("You both selected the same items. The score is even !")
 
if a == "Paper" and b == "Rock":
    print("You WON !")
    
elif a == "Paper" and b == "Cisors":
    print("LOSER !")
    
elif a == "Paper" and b == "Paper":
    print("You both selected the same items. The score is even !")
    
 
if a == "Cisors" and b == "Paper":
    print("You WON !")
    
elif a == "Cisors" and b == "Paper":
    print("LOSER !")
    
elif a == "Cisors" and b == "Cisors":
    print("You both selected the same items. The score is even !")

# Classe tour de Hanoi

#=======================================================================================
class Tower :
    
    #Constructeur
    def __init__(self, name) :
        self.tower = []
        self.name  = name
        
    def __str__(self):
        return str(self.tower)
#=======================================================================================
        
    
# Creation d'une tour à n disques modelisee sous forme d'une pile : haut de pile = dernier element d'une liste
# n : nombre de disques
# isEmpty : remplissage des tours ou non
def createTower(n, tower) :
    for i in range(n, 0, -1) :    # decrementation pour imiter une pile (modele des tours)
        tower.append(i)           # ajout des disques a la tour, le plus petit en haut de pile (ou en fin de liste)
        
    

# Deplacement du disque d'une liste "début" vers une liste "fin", de sommet à sommet
# Contrainte : on ne peut pas deplacer un disque d'un sommet sur un autre "plus petit"
# begin : tour avec disques à deplacer
# end : tour de depôt des disques
def move(begin, end) :
    print("Deplacer : ", begin.name, " = ", begin.tower, ", ", end.name, " = ", end.tower)
    
    end.tower.append(begin.tower.pop())     # on empile le disque de depart en haut de la tour d'arrivee 
    return 1


# Algorithme de resolution des tours de Hanoi
# n : nombre de disque
# begin : tour de départ
# inter : tour intermediaire
# end   : tour d'arrivee
def Hanoi(n, begin, inter, end) :
    print("nb disques :", n)
    print("Debut : ", begin.name, " = ", begin.tower, ", Inter : ", inter.name, " = ", inter.tower, ", Fin : ", end.name, " = ", end.tower)
    if(n == 1) :
        move(begin, end)
    else :
        Hanoi(n-1, begin, end, inter)
        move(begin, end)
        Hanoi(n-1, inter, begin, end)
        
        
        
#PROGRAMME MAIN
if __name__ == "__main__" :
    # Variables
    n = 3                       # nombre de disque
    
    # Creation des tours
    a = Tower('a')       
    createTower(n, a.tower)        # depart avec disques
    
    b = Tower('b')                 # inter
    
    c = Tower('c')                 # fin


    # Resolution du probleme
    Hanoi(n, a, b, c)









    
    
    
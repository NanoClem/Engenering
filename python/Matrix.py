

class Matrix :

    #Constructeur
    def __init__(self, elem) :
        self.elem = elem
        self.n    = len(elem)       #nb lignes
        self.p    = len(elem[0])    #nb colonnes selon nb elems dans le premier tableau d'une ligne


    #Afficheur
    def __str__(self) :
        return str(self.elem)



    #Taille de la matrice
    def size(self) :
        return [self.n, self.p]


    #Surchage de l'opérateur "+"
    def __add__(self, other) :
        newMat = [[0]*self.p]*self.n                                #matrice resultat de dimensions égales
        
        if(self.n != len(other) | self.p != len(other[0])) :
           print("Erreur : matrices de dimensions differentes")
           return
           
        for i in range(0, self.n) :
           for j in range(0, self.p) :
               newMat[i][j] = self.elem[i][j] + other[i][j]

        return newMat


    #Trace d'une matrice
    def trace(self) :
        if(self.n != self.p):
            print("Erreur, matrice non carree")
            return
        
        res = 0
        for i in range(0, self.n):
            res += self.elem[i][i]

        return res


    #Transposée Matrice
    def trans(self):
        newMat = [[0]*self.n]*self.p                #matrice transposee (dimensions inversees)
        
        for i in range(self.n):
            for j in range(self.p):
                newMat[j][i] = self.elem[i][j]      #les lignes deviennent les colonnes et vice-versa
                
        return newMat
            

    
        

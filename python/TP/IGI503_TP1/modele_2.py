#
# ATTENTION : NE PAS METTRE D'ACCENT, MEME DANS LES COMMENTAIRES
#
# import des bibliotheques
from skimage import io
from skimage.transform import resize
import matplotlib.pyplot as plt
import numpy as np

class image:
    # Initialisation d'une image composee d'un tableau 2D vide
    # (pixels) et de 2 dimensions (H = height et W = width) mises a 0
    def __init__(self):
        self.pixels = None 
        self.H = 0
        self.W = 0
        
    # Remplissage du tableau pixels de l'image self avec un tableau 2D (tab_pixels)
    # et affectation des dimensions de l'image self avec les dimensions 
    # du tableau 2D (tab_pixels) 
    def set_pixels(self, tab_pixels):
        self.pixels = tab_pixels
        self.H,self.W = self.pixels.shape 

    # Lecture d'un image a partir d'un fichier de nom "file_name"
    def load_image(self, file_name):
        self.pixels = io.imread(file_name)
        self.H,self.W = self.pixels.shape 
        print("lecture image : " + file_name + " (" + str(self.H) + "x" + str(self.W) + ")")

    # Affichage a l'ecran d'une image
    def display(self, window_name):
        fig=plt.figure(window_name)
        if (not (self.pixels is None)):
            io.imshow(self.pixels)
            io.show()
        else:
            print("L'image est vide")
            

    #==============================================================================
    # Methode de binarisation
    # 2 parametres :
    #   self : l'image a binariser
    #   S : le seuil de binarisation
    #   on retourne une nouvelle image binarisee
    #==============================================================================

    def binaris(self, S):
        
        # preparaton du resultat : creation d'une image vide 
        im_modif = image()
        # affectation de l'image resultat par un tableau de 0, de meme taille
        # que le tableau de pixels de l'image self
        # les valeurs sont de type uint8 (8bits non signes)
        im_modif.set_pixels(np.zeros((self.H,self.W), dtype=np.uint8))
                                                
        # boucle imbriquees pour parcourir tous les pixels de l'image
        for l in range(self.H):
            for c in range(self.W):
                # modif des pixels d'intensite >= a S
                if self.pixels[l][c] >= S:
                    im_modif.pixels[l][c] = 255
                else :
                    im_modif.pixels[l][c] = 0
        return im_modif
        
        
        
        
    
    #==============================================================================
    # Dans une image binaire contenant une forme noire sur un fond blanc
    # la methode 'localisation' permet de limiter l'image au rectangle englobant
    # la forme noire
    # 1 parametre :
    #   self : l'image binaire que l'on veut recadrer
    #   on retourne une nouvelle image recadree
    #==============================================================================

    def localisation(self):
        
        #creation de la nouvelle image recadree
        im_loc = image()
        
        # declaration des coordonnees de localisation
        l_min = l_max = c_min = c_max = -10
        
        # determination des coordonnees min/max des lignes
        for l in range(self.H) :
            for c in range(self.W) :
                if self.pixels[l][c] == 0 :     # om tombe sur un pixel noir
                    if(l_min == -10) :          # si la valeur n'a pas deja ete trouve, on note les coords
                        l_min = l
                    l_max = l                   # on note les coords max jusqu'a ce qu'on ait plus que des pixels blancs
        
        # determination des coordonnee min/max des colonnes
        for c in range(self.W) :
            for l in range(self.H) :
                if self.pixels[l][c] == 0:
                    if(c_min == -10) :
                        c_min = c
                    c_max = c
                    
        #on affetce les pixels 
        im_loc.set_pixels(self.pixels[l_min:l_max+1, c_min:c_max+1])
        
        print(l_min, l_max, c_min, c_max)
        return im_loc
    
    
    
         
    #==============================================================================
    # Methode de redimensionnement d'image
    #==============================================================================

    def resize_im(self,new_H,new_W) :
        
        # creation de la nouvelle image redimensionnee
        im_resized = image()
        # affectation des nouvelles dimensions
        im_resized.H = new_H
        im_resized.W = new_W
        
        # redimensionnement de l'image 
        im_resized.pixels = resize(self.pixels, (new_H, new_W), 0)
        # normalisation sur l'intervalle de pixels [0, 255] et conversion en uint8
        im_resized.pixels = np.uint8(im_resized.pixels*255)
        
        return im_resized



    #==============================================================================
    # Methode de mesure de similitude entre l'image self et un modele im
    #==============================================================================

    def simil_im(self, im) :
        
        # Nombre de pixels correspondant entre les deux images
        pixels_simil = 0
        #Nombre total de pixels dans l'image de base
        px_total = self.H * self.W
        
        if self.H == im.H & self.W == im.W :
            for l in range(self.H) :
                for c in range(self.W) :
                    if self.pixels[l][c] == im.pixels[l][c] :
                        pixels_simil += 1
        else :
            print("Dimensions differentes")
            
        return pixels_simil / px_total



    #==============================================================================
    # Methode de transformation d'une image en son image negative
    #==============================================================================
    
    def negative(self) :
        
        #creation de l'image negative
        im_neg = image()
        im_neg.pixels = 255 - self.pixels
        
        return im_neg
        
        


   
# fin class image


#==============================================================================
#  Fonction de lecture des fichiers contenant les images modeles
#  Les differentes images sont mises dans une liste
# l'element '0' de la liste de la liste correspond au chiffre 0,
# l'element '1' au chiffre 1, etc.
#==============================================================================

def lect_modeles():

    fichiers= ['_0.png','_1.png','_2.png','_3.png','_4.png','_5.png','_6.png', 
             '_7.png','_8.png','_9.png']
    list_model = []
    for fichier in fichiers:
        model = image()
        model.load_image(fichier);
        list_model.append(model)
    return list_model
   
#==============================================================================
#==============================================================================

#   PROGRAMME PRINCIPAL

#==============================================================================
# # Lecture image
#==============================================================================

im = image()
im.load_image('test10.JPG')
im.display("image initiale")

#==============================================================================
# Binarisation
#==============================================================================
seuil = 150
im_bin = im.binaris(seuil)
im_bin.display("Image binarisee")

#
#==============================================================================
#  Localisation chiffre
#==============================================================================
#

im_loc = im_bin.localisation()
im_loc.display("Localisation du chiffre")


#
#==============================================================================
# Test de la fonction resize
#==============================================================================
new_H = 60
new_W = 100
im_resized = im_loc.resize_im(new_H, new_W)
im_resized.display("Image redimensionnee")


#
#==============================================================================
# Test de la fonction similitude
#==============================================================================

#creation de l'image negative de im_loc
im_loc_neg = im_loc.negative()
im_loc_neg.display("Image negative")

# test de similitudes
simi = im_loc.simil_im(im_loc_neg)
print("Rapport de similitudes entre l'image localisee et son image negative :", simi)

#==============================================================================
# Lecture des chiffres modeles
#==============================================================================

list_model = lect_modeles()
# test verifiant la bonne lecture de l'un des modeles, par exemple le modele '8'
list_model[8].display("modele 8")

#==============================================================================
# Mesure de similitude entre l'image et les modeles 
# et recherche de la meilleure similitude
#==============================================================================




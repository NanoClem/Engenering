#
# ATTENTION : NE PAS METTRE D'ACCENT, MEME DANS LES COMMENTAIRES
#
# import des bibliotheques
from skimage import io
import matplotlib.pyplot as plt
from skimage.transform import resize
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
    # Methode mettant en blanc tous les pixels de l'image self
    # dont l'intensite est superieure ou egale au seuil S
    #==============================================================================

    def modif_ima(self,S):
    
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
                    im_modif.pixels[l][c] = self.pixels[l][c]
        return im_modif
    
    
    #
    #
    #
    #
    
    
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
    
    
    #
    #
    #
    
    # Recadrage de l'image binarisée de manière à englober la forme desiree
    # à partir des pixels noirs
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
        
    
    
    #
    #
    #
    
    
    #==============================================================================
    # Methode de redimensionnement de l'image
    #
    #==============================================================================
    def resize_im(self, new_H, new_W) :
        
        im_resized = image()
        im_resized.set_pixels(self.pixels)
        
        im_resized.resize
        
    
    
    

#==============================================================================
# # Programme principal
#==============================================================================

# Lecure d'une image depuis un fichier
ima_test = image()
ima_test.load_image('test10.jpg')

# Affichage de cette image
ima_test.display("image initiale")


# Creation d'une image modifiee
seuil = 150
ima_modif = ima_test.binaris(seuil)

# Affichage de l'image modifiee
ima_modif.display("image modifiee")


# Recadrage de l'image binarisee
ima_rec = ima_modif.localisation()

#Affichage de l'image recadree
ima_rec.display("image recadree")


print("fin du programme")

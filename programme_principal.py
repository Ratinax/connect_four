import pygame
from pygame.locals import *
from random import *
from time import *
from verifie_gagne import*
# initialisatin pygame
pygame.init()
fen_x=1920
fen_y=int(16/9*fen_x)
fenetre = pygame.display.set_mode( (fen_x,fen_y), FULLSCREEN )
# Variables utiles
liste_jeu=[
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
]
liste_nb_pion_colonne=[0,0,0,0,0,0,0]
nb_pion=0
tour=0
bien_valide=False
# Textes
texte_grand = pygame.font.Font( None , int(0.04*fen_x))
texte_moyen = pygame.font.Font(None, int(fen_x/14.84)) # police moyenne
texte_gagner=False
# Truc pour tempo
pygame.mixer.pre_init(44100, 16, 2, 4096)
#BOUCLE INFINIE initialisation
continuer = 1
continuer2=True
pygame.key.set_repeat(1, 10)
color=(255,255,255) # couleur blanche
for i in range(6):
    for j in range(7):
        pygame.draw.circle(fenetre,color,(j*100+660,i*100+300),45)
pygame.display.flip()
while continuer:
    for event in pygame.event.get():    #Attente des événements
        if event.type == QUIT:
            continuer = 0
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                continuer=0
        if event.type==KEYUP:
            if event.key==K_BACKSPACE:
                if liste_jeu[case_davant[0]][case_davant[1]]!=0:
                    tour+=1
                    liste_nb_pion_colonne[case_davant[1]]-=1
                    liste_jeu[case_davant[0]][case_davant[1]]=0
                    for i in range(6):
                        for j in range(7):
                            if liste_jeu[i][j]==1:
                                color=(255,40,30) # couleur rouge
                            if liste_jeu[i][j]==2:
                                color=(255,235,10) # couleur jaune
                            if liste_jeu[i][j]==0:
                                color=(255,255,255) # couleur blanche
                            pygame.draw.circle(fenetre,color,(j*100+660,i*100+300),45)
                    position_pion=round((pygame.mouse.get_pos()[0]-60)/100,0)*100
                    rectangle = pygame.draw.rect(fenetre,(0,0,0),(0,100,1920,145))
                    if tour%2==0:
                        pygame.draw.circle(fenetre,(255,40,30),(position_pion+60,200),45)
                    elif tour%2==1:
                        pygame.draw.circle(fenetre,(255,235,10),(position_pion+60,200),45)
                    pygame.display.flip()
        if event.type==MOUSEMOTION:
            position_pion=round((pygame.mouse.get_pos()[0]-60)/100,0)*100
            rectangle = pygame.draw.rect(fenetre,(0,0,0),(0,100,1920,145))
            if tour%2==0:
                pygame.draw.circle(fenetre,(255,40,30),(position_pion+60,200),45)
            elif tour%2==1:
                pygame.draw.circle(fenetre,(255,235,10),(position_pion+60,200),45)
            pygame.display.flip()
        if event.type==MOUSEBUTTONDOWN:
            if event.button==1:
                try:
                    liste_nb_pion_colonne[int((pygame.mouse.get_pos()[0]-660+45)/100)]+=10
                    bien_valide=True
                    liste_nb_pion_colonne[int((pygame.mouse.get_pos()[0]-660+45)/100)]-=10
                except:
                    print("sheeeeesh")
                    bien_valide=False
                if bien_valide==True and int((pygame.mouse.get_pos()[0]-660+45))>=0:
                    if liste_nb_pion_colonne[int((pygame.mouse.get_pos()[0]-660+45)/100)]<6:
                        if tour%2==0:
                            try:
                                liste_jeu[5-liste_nb_pion_colonne[int((pygame.mouse.get_pos()[0]-660+45)/100)]][int((pygame.mouse.get_pos()[0]-660+45)/100)]=1
                                case_davant=(5-liste_nb_pion_colonne[int((pygame.mouse.get_pos()[0]-660+45)/100)],int((pygame.mouse.get_pos()[0]-660+45)/100))
                                if verifie(liste_jeu,(5-liste_nb_pion_colonne[int((pygame.mouse.get_pos()[0]-660+45)/100)],int((pygame.mouse.get_pos()[0]-660+45)/100)))==True: #quand le joueur gagne
                                    texte_gagner = texte_moyen.render("Rouge gagne!!",True,(255,40,30))
                                    continuer=False
                                liste_nb_pion_colonne[int((pygame.mouse.get_pos()[0]-660+45)/100)]+=1
                                tour+=1
                                for i in range(7):
                                    nb_pion+=liste_nb_pion_colonne[i]
                                if nb_pion==42:
                                    texte_gagner = texte_moyen.render("égalité.",True,(240,240,240))
                                    continuer=False
                                nb_pion=0
                            except Exception as e:
                                print(e)
                        elif tour%2==1:
                            try:
                                liste_jeu[5-liste_nb_pion_colonne[int((pygame.mouse.get_pos()[0]-660+45)/100)]][int((pygame.mouse.get_pos()[0]-660+45)/100)]=2
                                case_davant=(5-liste_nb_pion_colonne[int((pygame.mouse.get_pos()[0]-660+45)/100)],int((pygame.mouse.get_pos()[0]-660+45)/100))
                                if verifie(liste_jeu,(5-liste_nb_pion_colonne[int((pygame.mouse.get_pos()[0]-660+45)/100)],int((pygame.mouse.get_pos()[0]-660+45)/100)))==True: #quand le joueur gagne
                                    texte_gagner = texte_moyen.render("Jaune gagne!!",True,(255,235,10))
                                    continuer=False
                                liste_nb_pion_colonne[int((pygame.mouse.get_pos()[0]-660+45)/100)]+=1
                                tour+=1
                                for i in range(7):
                                    nb_pion+=liste_nb_pion_colonne[i]
                                if nb_pion==42:
                                    texte_gagner = texte_moyen.render("égalité.",True,(240,240,240))
                                    continuer=False
                                nb_pion=0
                            except:
                                pass
                    bien_valide=False
                for i in range(6):
                    for j in range(7):
                        if liste_jeu[i][j]==1:
                            color=(255,40,30) # couleur rouge
                        if liste_jeu[i][j]==2:
                            color=(255,235,10) # couleur jaune
                        if liste_jeu[i][j]==0:
                            color=(255,255,255) # couleur blanche
                        pygame.draw.circle(fenetre,color,(j*100+660,i*100+300),45)
                position_pion=round((pygame.mouse.get_pos()[0]-60)/100,0)*100
                rectangle = pygame.draw.rect(fenetre,(0,0,0),(0,100,1920,145))
                if tour%2==0:
                    pygame.draw.circle(fenetre,(255,40,30),(position_pion+60,200),45)
                elif tour%2==1:
                    pygame.draw.circle(fenetre,(255,235,10),(position_pion+60,200),45)
                pygame.display.flip()
if texte_gagner!=False:
    while continuer2:
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer2 = False
            if event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    continuer2=False
        fenetre.blit(texte_gagner,(100,100))
        pygame.display.flip()
pygame.quit()
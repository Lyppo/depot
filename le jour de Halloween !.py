"""
Programme réalisé par Coutable, Antonin, 1G8
Et Laurent, Candyce, 1G2
"""
import pygame

salledebain=0

pygame.init()
fenetre = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("le jour de Halloween !")
image1=pygame.image.load("1.png")
image2=pygame.image.load("2.png")
image3=pygame.image.load("3.png")
image4=pygame.image.load("4.png")
image5=pygame.image.load("5.png")
image6=pygame.image.load("6.png")
image7=pygame.image.load("7.png")
image8=pygame.image.load("8.png")
image9=pygame.image.load("9.png")
image10=pygame.image.load("10.png")
image11=pygame.image.load("11.png")
image12=pygame.image.load("12.png")
image13=pygame.image.load("13.png")
image14=pygame.image.load("14.png")
image15=pygame.image.load("15.png")
image16=pygame.image.load("16.png")
image17=pygame.image.load("17.png")
image18=pygame.image.load("18.png")
image19=pygame.image.load("19.png")
image20=pygame.image.load("20.png")
image21=pygame.image.load("21.png")


pieceperso=1
chambre=0
salledebain=0
dehors=0

def quelpiece(piece):
    if piece==1:
        fenetre.blit(image1,(0,0))
    elif piece==2:
        fenetre.blit(image2,(0,0))
    elif piece==3:
        fenetre.blit(image3,(0,0))
    elif piece==4:
        fenetre.blit(image4,(0,0))
    elif piece==5:
        fenetre.blit(image5,(0,0))
    elif piece==6:
        fenetre.blit(image6,(0,0))
    elif piece==7:
        fenetre.blit(image7,(0,0))
    elif piece==8:
        fenetre.blit(image8,(0,0))
    elif piece==9:
        fenetre.blit(image9,(0,0))
    elif piece==10:
        fenetre.blit(image10,(0,0))
    elif piece==11:
        fenetre.blit(image11,(0,0))
    elif piece==12:
        fenetre.blit(image12,(0,0))
    elif piece==13:
        fenetre.blit(image13,(0,0))
    elif piece==14:
        fenetre.blit(image14,(0,0))
    elif piece==15:
        fenetre.blit(image15,(0,0))
    elif piece==16:
        fenetre.blit(image16,(0,0))
    elif piece==17:
        fenetre.blit(image17,(0,0))
    elif piece==18:
        fenetre.blit(image18,(0,0))
    elif piece==19:
        fenetre.blit(image19,(0,0))
    elif piece==20:
        fenetre.blit(image20,(0,0))
    elif piece==21:
        fenetre.blit(image21,(0,0))


def decision(direction,piece):

    global dehors
    global salledebain
    global chambre

    print("Vous désirez allez au",direction)

    memorisePiece=piece

    if direction=='n':
        if piece==1:
            piece=2
        elif piece==2:
              piece=8
        elif piece==3:
              piece=8
        elif piece==5:
              piece=7
        elif piece==6:
              piece=7
        elif piece==9:
              piece=8
        elif piece==12:
              piece=10
        elif piece==10:
              piece=14
        elif piece==14:
            if dehors==0:
                piece=21
            elif dehors==1:
                piece=18
                dehors=2
            elif dehors==2:
                piece=15
        elif piece==13:
            if dehors==0:
                piece=20
            elif dehors==1:
                piece=17
                dehors=2
            elif dehors==2:
                piece=16
        elif piece==19:
              piece=10

    elif direction=='s':
        if piece==1:
            piece=2
        elif piece==7:
            if salledebain==0:
                piece=5
                salledebain=1
                chambre=1
                dehors=1
            elif salledebain==1:
                piece=6
        elif piece==8:
            if chambre==0:
                piece=2
            elif chambre==1:
                piece=3
        elif piece==9:
              piece=10
        elif piece==17:
              piece=13
        elif piece==16:
              piece=13
        elif piece==20:
              piece=13
        elif piece==18:
              piece=14
        elif piece==15:
              piece=14
        elif piece==21:
              piece=14
        elif piece==14:
              piece=10
        elif piece==10:
              piece=12
        elif piece==19:
              piece=10


    elif direction=='e':
        if piece==1:
            piece=2
        elif piece==7:
              piece=8
        elif piece==8:
              piece=9
        elif piece==5:
              piece=4
        elif piece==6:
              piece=4
        elif piece==4:
            if chambre==0:
                piece=2
            elif chambre==1:
                piece=3
        elif piece==13:
              piece=10
        elif piece==10:
              piece=19
        elif piece==19:
              piece=9


    elif direction=='o':
        if piece==1:
            piece=2
        elif piece==19:
              piece=11
        elif piece==8:
              piece=7
        elif piece==2:
              piece=4
        elif piece==3:
              piece=4
        elif piece==4:
            if salledebain==0:
                piece=5
                salledebain=1
                chambre=1
                dehors=1
            elif salledebain==1:
                piece=6
        elif piece==11:
              piece=10
        elif piece==10:
              piece=13


    if memorisePiece==piece:
        if piece==1:
            piece=2
        else:
            print("Déplacement impossible")
    else:
        print("C'est possible")
    return piece


loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        elif event.type == pygame.KEYDOWN:
            pieceperso=decision(event.unicode,pieceperso)
            if event.key == pygame.K_ESCAPE or event.unicode == 'q':
                loop = False
    quelpiece(pieceperso)
    pygame.display.flip()
pygame.quit()
import pygame, chess, sys, time

pygame.init()
pygame.display.set_caption("CHESS")

liste = []
a = 0
screenW, screenH = 512, 512
squareSize = screenW // 8
index = screenW / 8
WHITE = (255, 255, 255)
GREEN = (69, 184, 61)
PURPLE = (128,0,128)
HAMLE = (138,138,138)
board = chess.Board()  #tahta oluşturduk
clock = pygame.time.Clock()  #frame sayısını ayarlamak için nesnemizi oluşturduk


bV = pygame.image.load('pieces/vezirB.png')    #taşlarımızın görsellerini ekledik
bA = pygame.image.load('pieces/atB.png')
bK = pygame.image.load('pieces/kaleB.png')
bP = pygame.image.load('pieces/piyonB.png')
bS = pygame.image.load('pieces/sahB.png')
bF = pygame.image.load('pieces/filB.png')
sV = pygame.image.load('pieces/vezirS.png')
sA = pygame.image.load('pieces/atS.png')
sK = pygame.image.load('pieces/kaleS.png')
sP = pygame.image.load('pieces/piyonS.png')
sS = pygame.image.load('pieces/sahS.png')
sF = pygame.image.load('pieces/filS.png')

screen = pygame.display.set_mode((screenW,screenH))




def tahtaBoya():    #tahtanın renklerini ayarlayan fonk
    for row in range(8):
        for col in range(8):
            x = col * squareSize
            y = row * squareSize
            rect = pygame.Rect(x, y, squareSize, squareSize)
            if (row + col) % 2 == 0:
                pygame.draw.rect(screen, GREEN, rect)
            else:
                pygame.draw.rect(screen, WHITE, rect)


for i in range(8):    #tahtayı görüntülemek için matrix
        liste.append((8)*[" "])      
for i in range(8):
    for j in range(8):
        liste[i][j] = a
        a += 1
                 
def goruntule():    #tahtayı görüntüleyen fonk
    for nokta in chess.SQUARES:
        piece = board.piece_at(nokta)
        if piece is not None:
            for i in range(8):
                for j in range(8):
                    if liste[7-j][i] == nokta:
                        if piece.symbol() == "p":
                            screen.blit(sP, (index*i+10,index*j+10))
                        elif piece.symbol() == "r":
                            screen.blit(sK, (index*i+10,index*j+10))
                        elif piece.symbol() == "n":
                            screen.blit(sA, (index*i+10,index*j+10))
                        elif piece.symbol() == "q":
                            screen.blit(sV, (index*i+10,index*j+10))
                        elif piece.symbol() == "k":
                            screen.blit(sS, (index*i+10,index*j+10))
                        elif piece.symbol() == "b":
                            screen.blit(sF, (index*i+10,index*j+10))
                        elif piece.symbol() == "P":
                            screen.blit(bP, (index*i+10,index*j+10))
                        elif piece.symbol() == "R":
                            screen.blit(bK, (index*i+10,index*j+10))
                        elif piece.symbol() == "N":
                            screen.blit(bA, (index*i+10,index*j+10))
                        elif piece.symbol() == "Q":
                            screen.blit(bV, (index*i+10,index*j+10))
                        elif piece.symbol() == "K":
                            screen.blit(bS, (index*i+10,index*j+10))
                        elif piece.symbol() == "B":
                            screen.blit(bF, (index*i+10,index*j+10))
goruntule()

pygame.display.update()

while True:
    for event in pygame.event.get():  #her hangi bir giriş olup olmadığı kontrol ediliyor
        if event.type == pygame.QUIT:  #çıkış tuşuna basılmışsa
            pygame.quit()
            sys.exit()
        if board.is_checkmate():   #mat durumunu kontrol eder
            time.sleep(0.5)
            tahtaBoya()    #ekrani temizle
            font = pygame.font.SysFont('Arial', 50)
            text = font.render('CHECK MATE!', True, (PURPLE))
            screen.blit(text, (100, 200))
            pygame.display.update()
            time.sleep(2)
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:  #ekrana yapılan tıklamaları algılar
            x, y = event.pos
            square = chess.parse_square(f"{chr((x // 64) + 97)}{8 - (y // 64)}")  #hamle yapilmak istenen karenin koordinatını alır
            legal_square = [move.to_square for move in board.legal_moves if move.from_square == square]  #secilen tasin gidebilecegi kareleri listeler
            for a in legal_square:   #gidilebilen taşları boyadık
                for i in range(8):
                    for j in range(8):
                        if liste[7-j][i] == a:
                            g = index*i+21
                            h = index*j+21
                            pygame.draw.ellipse(screen,(HAMLE),[g,h,20,20],0)
                            pygame.display.update()
                            
            if square:   # kare secilmisse
                try:     
                    x, y = event.pos
                    target_square = None  
                    while not target_square:   #gidilecek yer secilmemisse
                        for event in pygame.event.get(): #girisleri kontrol eder
                            if event.type == pygame.MOUSEBUTTONDOWN:  #gidilecek olan karenin seçilmesini bekler
                                x, y = event.pos
                                target_square = chess.parse_square(f"{chr((x // 64) + 97)}{8 - (y // 64)}")   #hamle yapılma istenen karenin koordinatını alır
                                break
                    for i in legal_square:  #i yi yapilabilen hamleler listesinde gezdirir
                        if target_square == i:   #hamle yapılabiliyor mu diye kontrol eder
                            move = chess.Move(square, target_square)  #hamleyi dönusturduk
                            board.push(move)   #hamleyi uygular
                            if board.turn:   #hamle sırasını diğer oyuncuya verir
                                board.turn = True
                            else:
                                board.turn = False
                            square = None
                except:
                    square = None  #gidilecek yer secilmemisse 1. hamleyi siler
            else:
                square = None


        screen.fill(WHITE)  #ekranı temizler
        tahtaBoya()   #tahtayı yeniden çizer
        goruntule() #tahtaya tasları yerlestirir
        pygame.display.update() #ekranı günceller
        clock.tick(20)   #frame sayısını ayarlar
        

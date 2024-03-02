import pygame

#Inicializa a biblioteca pygame
pygame.init()

#Define o tamanho da tela
tamanho_tela = (960, 540)

#Cria uma tela
tela = pygame.display.set_mode((tamanho_tela))

#Cria um relógio para controlar o fps
relogio = pygame.time.Clock()

#Título da tela
pygame.display.set_caption("Vamp Run")

#Importa a fonte
fonte = pygame.font.Font('assets/Fontes/CyberpunksItalic.ttf', 150)
fonte_sub = pygame.font.Font('assets/Fontes/Cyberpunks.ttf', 50) 

#Imagens de fundo
fundo1 = pygame.image.load('assets/Cenario/1.png') 
fundo2 = pygame.image.load('assets/Cenario/2.png')
fundo3 = pygame.image.load('assets/Cenario/3.png')
fundo4 = pygame.image.load('assets/Cenario/4.png')
fundo5 = pygame.image.load('assets/Cenario/5.png')
estrada = pygame.image.load('assets/Cenario/road.png')

#Arruma a escala das imagens de acordo com o tamanho da tela
fundo1 = pygame.transform.scale(fundo1, tamanho_tela)
fundo2 = pygame.transform.scale(fundo2, tamanho_tela)
fundo3 = pygame.transform.scale(fundo3, tamanho_tela)
fundo4 = pygame.transform.scale(fundo4, tamanho_tela)
fundo5 = pygame.transform.scale(fundo5, tamanho_tela)
estrada = pygame.transform.scale(estrada, tamanho_tela)


#Animação do jogador
index_vanitas_parado = 0
index_vanitas_correndo = 0

lista_vanitas_parado = []
lista_vanitas_correndo = []

for imagem in range(5):
   imagem_vanitas_parado = pygame.image.load(f"assets/Parado/tile00{imagem}.png")
   imagem_vanitas_parado = pygame.transform.scale(imagem_vanitas_parado, (280, 280))
   lista_vanitas_parado.append(imagem_vanitas_parado)

for imagem in range(8):
    imagem_vanitas_correndo = pygame.image.load(f"assets/Correndo/tile00{imagem}.png")
    imagem_vanitas_correndo = pygame.transform.scale(imagem_vanitas_correndo, (280, 280))
    lista_vanitas_correndo.append(imagem_vanitas_correndo) 

#Cria o retângulo do jogador
vanitas_retangulo_parado = lista_vanitas_parado[index_vanitas_parado].get_rect(center = (450, 370))      
vanitas_retangulo_correndo = lista_vanitas_correndo[index_vanitas_correndo].get_rect(center = (90, 370))

titulo = fonte.render("Vamp Run", True, (255, 255, 255)) #Renderiza o titulo
sub_titulo = fonte_sub.render("Aperte ESPAÇO para correr", True, (255, 255, 255)) #Renderiza sub título

jogo_comecou = False
#Laço principal do jogo
while True:
    for evento in pygame.event.get():
        print(evento)

        if evento.type == pygame.QUIT:
            pygame.quit()

            exit()

        #Verifica se uma tecla foi pressionada
        if evento.type == pygame.KEYDOWN:
            #Vefirica se a tecla pressionada foi o espaço
            if evento.key == pygame.K_SPACE:
                jogo_comecou = True
                ativaAnimacao = True


    tela.fill((255, 255, 255))
    #Imagens de fundo
    tela.blit(estrada, (0, 0))   
    tela.blit(fundo1, (0, -80))
    tela.blit(fundo2, (0, -80))
    tela.blit(fundo3, (0, -80))
    tela.blit(fundo4, (0, -80))
    tela.blit(fundo5, (0, -80))

    #Checa se o jogo não começou
    if not jogo_comecou:
        #Mostra o titulo
        tela.blit(titulo, (tamanho_tela[0] / 2 - titulo.get_width() / 2, 50))
        tela.blit(sub_titulo, (tamanho_tela[0] / 2 - titulo.get_width() / 2, 230))

        tela.blit(lista_vanitas_parado[int(index_vanitas_parado)], vanitas_retangulo_parado)

        index_vanitas_parado += 0.3
        if index_vanitas_parado >=len(lista_vanitas_parado):
            index_vanitas_parado = 0

    else: #Se o jogo começou
        if ativaAnimacao:
            tela.blit(lista_vanitas_correndo[int(index_vanitas_correndo)], vanitas_retangulo_correndo)  

            index_vanitas_correndo +=0.5
            if index_vanitas_correndo >=len(lista_vanitas_correndo):
                index_vanitas_correndo = 0     
   
    pygame.display.update()
    #Controla o FPS
    relogio.tick(60)
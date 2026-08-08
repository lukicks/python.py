import pygame
from sys import exit

def imagem_inicial(imagem,superficie,superficie4,fonte ):
    imagem.blit(superficie,superficie4)
    ret_sair = pygame.draw.rect(imagem,(150,0,0), (725,600,400,100),15)
    ret_entrar = pygame.draw.rect(imagem,(30, 128, 0), (725,430,400,100),15)
    textoe = fonte.render('Entrar', False, (30, 128, 0))
    quadradoe = textoe.get_rect(center =  (925, 480))
    textos = fonte.render('Sair', False, (150,0,0))
    quadrados = textos.get_rect(center = (925,650))
    imagem.blit(textoe,quadradoe)
    imagem.blit(textos,quadrados)

    return ret_sair, ret_entrar

def imagem_esc(imagem,fonte):
    pygame.draw.rect(imagem, (220, 220, 0),(700,380,500,400))
    ret_continuar = pygame.draw.rect(imagem, (255, 255, 255), (775,430, 350,90),15)
    ret_sair = pygame.draw.rect(imagem, (255, 255, 255), (775,600,350,90),15)
    textoc = fonte.render('Voltar', False, (255, 255, 255))
    quadradoc = textoc.get_rect(center = ret_continuar.center)
    textos = fonte.render('Sair', False, (255, 255, 255))
    quadrados = textos.get_rect(center = ret_sair.center)
    imagem.blit(textoc,quadradoc)
    imagem.blit(textos,quadrados)

    return ret_continuar, ret_sair

def imagens_torcida():
    estadio_movimento1 = pygame.image.load(r"imagens\Imagem torcida 1.png").convert_alpha()
    estadio_movimento1 = pygame.transform.scale(estadio_movimento1, (1850,1000))

    estadio_movimento2 = pygame.image.load(r"imagens\Imagem torcida 2.png").convert_alpha()
    estadio_movimento2 = pygame.transform.scale(estadio_movimento2, (1850,1000))

    return[estadio_movimento1, estadio_movimento2]

def animacao_torcida(imagem, movimento, index):
    index += 0.2
    if index >= len (movimento):
        index = 0
    superficie_estadio = movimento[int(index)]
    estadio_retangulo = superficie_estadio.get_rect(center = (925,400))
    imagem.blit(superficie_estadio,estadio_retangulo)
    return index


def imagem_campo(imagem,placa,grama,cruzeiro,flamengo):
    pygame.draw.rect(imagem,(90, 128, 0),(0,830,1850,400))
    imagem.blit(placa, (-20, 690))
    imagem.blit(placa, (1128, 690))
    imagem.blit(grama, (-10,800))
    imagem.blit(grama, (380,800))
    imagem.blit(grama, (760,800))
    imagem.blit(grama, (1120,800))
    imagem.blit(grama, (1400,800))
    imagem.blit(grama, (1780,800))
    imagem.blit(cruzeiro, (480, 815))
    imagem.blit(flamengo, (1200,840))

def imagem_estadio(imagem,gole,gole4,gold,gold4,bola,bola4):
    imagem.blit(gole, gole4)
    imagem.blit(gold, gold4)
    imagem.blit(bola,bola4)

def imagem_placar(imagem,placar,placar4,esquer1,esquer2,direita1,direita2,time,time4):
    imagem.blit(placar, placar4)
    imagem.blit(esquer1,(730,883))
    imagem.blit(esquer2,(826,883))
    imagem.blit(direita1,(968,883))
    imagem.blit(direita2,(1068,883))
    imagem.blit(time,time4)

def movimento_jogador(imagem,jogador1,r41,jogador2,r42):
    imagem.blit(jogador1,r41)
    imagem.blit(jogador2,r42)

def main():
    pygame.init()

    # Resolucao-base em que o jogo foi originalmente construido.
    LARGURA_BASE = 1850
    ALTURA_BASE = 1000

    # Descobre a resolucao real do monitor do usuario.
    info_monitor = pygame.display.Info()
    largura_monitor = info_monitor.current_w
    altura_monitor = info_monitor.current_h

    # Janela real do usuario.
    tela_real = pygame.display.set_mode((largura_monitor, altura_monitor))

    # O jogo continua funcionando internamente em 1850x1000.
    # Isso permite manter todas as posicoes, colisoes e velocidades originais.
    tela = pygame.Surface((LARGURA_BASE, ALTURA_BASE))

    # Escala proporcional para nao deformar a imagem.
    escala = min(largura_monitor / LARGURA_BASE, altura_monitor / ALTURA_BASE)
    largura_jogo = int(LARGURA_BASE * escala)
    altura_jogo = int(ALTURA_BASE * escala)

    # Centraliza a imagem caso a proporcao do monitor seja diferente.
    offset_x = (largura_monitor - largura_jogo) // 2
    offset_y = (altura_monitor - altura_jogo) // 2

    pygame.display.set_caption('Soccer Simulator')
    clock = pygame.time.Clock()
    tempo_inicio = 0
    tempo_decrescente = 180
    atividade_jogo = False
    jogo_pausado = False
    inicio_pausa = 0

    imagem_inicio = pygame.image.load(r"imagens\Tela inicio .png").convert_alpha()
    imagem_inicio = pygame.transform.scale(imagem_inicio, (1850, 1000))
    retangulo_inicio = imagem_inicio.get_rect(center = (925,500))
    fonte_texto = pygame.font.Font(r"imagens\Fonte escrita.ttf",65)
    
    estadio_movimento = imagens_torcida()
    index_estadio = 0

    superficie_grama = pygame.image.load(r"imagens\grama estadio.png").convert_alpha()
    superficie_grama = pygame.transform.scale(superficie_grama, (400,30))
    superficie_placa = pygame.image.load(r"imagens\placa publicidade.png").convert_alpha()
    escudo_maior = pygame.image.load(r"imagens\Escudo Maior.png").convert_alpha()
    escudo_maior = pygame.transform.scale(escudo_maior, (200,200))
    escudo_menor = pygame.image.load(r"imagens\Escudo menor.png").convert_alpha()
    escudo_menor = pygame.transform.scale(escudo_menor, (135,160))
   
    superficie_gol = pygame.image.load(r"imagens\Imagem gol.png").convert_alpha()
    superficie_gol_e = pygame.transform.scale(superficie_gol, (150, 350))
    retangulo_gol_e = superficie_gol_e.get_rect(bottomleft = (0, 812))
    superficie_gol_d = pygame.transform.flip(superficie_gol_e, True, False)
    retangulo_gol_d = superficie_gol_d.get_rect(bottomright = (1850,820))

    superficie_placar = pygame.image.load(r"imagens\Imagem placar.png").convert_alpha()
    superficie_placar = pygame.transform.scale(superficie_placar, (500,173))
    retangulo_placar = superficie_placar.get_rect(center = (925,915))
    fonte_pontuacao = pygame.font.Font((r"imagens\DS-DIGIB.TTF"),110)
    fonte_tempo =  pygame.font.Font((r"imagens\DS-DIGIB.TTF"), 41)
    pontuacaoe1 = pontuacaoe2 = pontuacaod1 = pontuacaod2 = 0

    superficie_jogador1 = pygame.image.load(r"imagens\Imagem Jogador 1.png").convert_alpha()
    superficie_jogador1 = pygame.transform.scale(superficie_jogador1, (120,150))
    retangulo_jogador1 = superficie_jogador1.get_rect(bottomleft = (165, 800))
    gravidade_jogador1 = 0
    chute_jogador1 = pygame.image.load(r"imagens\Chute jogador1.png").convert_alpha()
    chute_jogador1 = pygame.transform.scale(chute_jogador1,(160,150))
    chutando_jogador1 = False
    tempo_chute1 = 0

    superficie_jogador2 = pygame.image.load(r"imagens\Jogador 2.png").convert_alpha()
    superficie_jogador2 = pygame.transform.scale(superficie_jogador2, (120,150))
    superficie_jogador2 = pygame.transform.flip(superficie_jogador2, True, False)
    retangulo_jogador2 = superficie_jogador2.get_rect(bottomright = (1690, 800))
    gravidade_jogador2 = 0
    chute_jogador2 = pygame.image.load(r"imagens\Chutando_jogador2.png").convert_alpha()
    chute_jogador2 = pygame.transform.scale(chute_jogador2,(160,150))
    chute_jogador2 = pygame.transform.flip(chute_jogador2, True, False)
    chutando_jogador2 = False
    tempo_chute2 = 0

    superficie_bola = pygame.image.load(r"imagens\imagem_bola.png").convert_alpha()
    superficie_bola = pygame.transform.scale(superficie_bola, (70,70))
    circulo_bola = superficie_bola.get_rect(center = (925,200))
    gravidade_bola = 0
    velocidade_bola = 0

    vitoria1 = pygame.image.load(r"imagens\vitoria cruzeiro.png").convert_alpha()
    vitoria1 = pygame.transform.scale(vitoria1, (1850, 1000))
    retangulo_final = vitoria1.get_rect(center = (925,500))
    vitoria2 = pygame.image.load(r"imagens\vitoria_fla.png").convert_alpha()
    vitoria2 = pygame.transform.scale(vitoria2, (1850, 1000))
    empate = pygame.image.load(r"imagens\empate.png").convert_alpha()
    empate = pygame.transform.scale(empate, (1850,1000))

    canto_torcida1 = pygame.mixer.Sound(r"imagens\Torcida-cruzeiro.wav")
    canto_torcida1.set_volume(0.02)
    canto_torcida2 = pygame.mixer.Sound(r"imagens\torcida flamengo.wav")
    canto_torcida2.set_volume(0.02)
    comemoracao_jogador1 = pygame.mixer.Sound(r"imagens\Comemoracao jogador1.wav")
    comemoracao_jogador1.set_volume(0.1)
    comemoracao_jogador2 = pygame.mixer.Sound(r"imagens\Comemoracao Jogador2.wav")
    comemoracao_jogador2.set_volume(0.1)

    while True:
        if atividade_jogo == False:
            retangulo_sair, retangulo_entrar = imagem_inicial(tela,imagem_inicio,retangulo_inicio,fonte_texto)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if atividade_jogo == False:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_x, mouse_y = event.pos
                        posicao_mause = (
                            int((mouse_x - offset_x) / escala),
                            int((mouse_y - offset_y) / escala)
                        )

                    if retangulo_sair.collidepoint(posicao_mause):
                        pygame.quit()
                        exit()
                    if retangulo_entrar.collidepoint(posicao_mause):
                        atividade_jogo = True
                        tempo_inicio = pygame.time.get_ticks()

                        canto_torcida1.play(loops=-1)
                        canto_torcida2.play(loops=-1)

            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE and tempo_decrescente > 0:
                        if jogo_pausado == False:
                            jogo_pausado = True
                            inicio_pausa = pygame.time.get_ticks()
                            canto_torcida1.set_volume(0)
                            canto_torcida2.set_volume(0)

                if jogo_pausado and event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_x, mouse_y = event.pos
                        posicao_mause = (
                            int((mouse_x - offset_x) / escala),
                            int((mouse_y - offset_y) / escala)
                        )
                        if retangulo_continuar_pausa.collidepoint(posicao_mause):
                            jogo_pausado = False
                            tempo_inicio += (pygame.time.get_ticks() - inicio_pausa)
                            canto_torcida1.set_volume(0.02)
                            canto_torcida2.set_volume(0.02)
                        if retangulo_sair_pausa.collidepoint(posicao_mause):
                            atividade_jogo = False
                            jogo_pausado = False
                            canto_torcida1.stop()
                            canto_torcida2.stop()
                            pontuacaoe1 = pontuacaoe2 = pontuacaod1 = pontuacaod2 = 0
                            retangulo_jogador1.bottomleft = (165, 800)
                            retangulo_jogador2.bottomright = (1690, 800)
                            circulo_bola.center = (925, 200)
                            velocidade_bola = gravidade_bola = 0
                            tempo_decrescente = 180

        if atividade_jogo:

            if jogo_pausado == False:
                teclas = pygame.key.get_pressed()
                posicao_antiga1 = retangulo_jogador1.x
                posicao_antiga2 = retangulo_jogador2.x

                velocidade1 = 7
                if teclas[pygame.K_a]:
                    retangulo_jogador1.x -= velocidade1
                if teclas[pygame.K_d]:
                    retangulo_jogador1.x += velocidade1
                if retangulo_jogador1.left < 3:
                    retangulo_jogador1.left = 3
                if retangulo_jogador1.right > 1847:
                    retangulo_jogador1.right = 1847

                if teclas[pygame.K_w] and (retangulo_jogador1.bottom >= 800 or retangulo_jogador1.bottom == retangulo_jogador2.top):
                    gravidade_jogador1 = -20
                if teclas[pygame.K_s]:
                    chutando_jogador1 = True
                    tempo_chute1 = pygame.time.get_ticks()

                    distancia1_x = circulo_bola.centerx - retangulo_jogador1.centerx 
                    distancia1_y = abs(circulo_bola.centery - retangulo_jogador1.centery)
                    if 0 < distancia1_x < 180 and  distancia1_y < 180:
                        velocidade_bola = 50
                        gravidade_bola = -25

                velocidade2 = 7
                if teclas[pygame.K_LEFT]:
                    retangulo_jogador2.x -= velocidade2
                if teclas[pygame.K_RIGHT]:
                    retangulo_jogador2.x += velocidade2
                if retangulo_jogador2.left < 3:
                    retangulo_jogador2.left = 3
                if retangulo_jogador2.right > 1847:
                    retangulo_jogador2.right = 1847

                if teclas[pygame.K_UP] and (retangulo_jogador2.bottom >= 800 or retangulo_jogador2.bottom == retangulo_jogador1.top):
                    gravidade_jogador2 = -20
                if teclas[pygame.K_DOWN]:
                    chutando_jogador2 = True
                    tempo_chute2 = pygame.time.get_ticks()

                    distancia2_x = retangulo_jogador2.centerx - circulo_bola.centerx
                    distancia2_y = abs(circulo_bola.centery - retangulo_jogador2.centery)
                    if 0 < distancia2_x < 180 and  distancia2_y < 180:
                        velocidade_bola = -50
                        gravidade_bola = -25

                if retangulo_jogador1.colliderect(retangulo_jogador2):
                    j1_por_cima = retangulo_jogador1.bottom <= retangulo_jogador2.centery
                    j2_por_cima = retangulo_jogador2.bottom <= retangulo_jogador1.centery
                    if not (j1_por_cima or j2_por_cima):
                        retangulo_jogador1.x = posicao_antiga1
                        retangulo_jogador2.x = posicao_antiga2

                gravidade_jogador1 += 1
                retangulo_jogador1.y += gravidade_jogador1
                if retangulo_jogador1.bottom >= 800:
                    retangulo_jogador1.bottom = 800
                    gravidade_jogador1 = 0

                gravidade_jogador2 += 1
                retangulo_jogador2.y += gravidade_jogador2
                if retangulo_jogador2.bottom >= 800:
                    retangulo_jogador2.bottom = 800
                    gravidade_jogador2 = 0
            
                if retangulo_jogador1.colliderect(retangulo_jogador2):
                    if retangulo_jogador1.centery < retangulo_jogador2.centery:
                        retangulo_jogador1.bottom = retangulo_jogador2.top
                        gravidade_jogador1 = 0
                    else:
                        retangulo_jogador2.bottom = retangulo_jogador1.top
                        gravidade_jogador2 = 0


                gravidade_bola += 1
                circulo_bola.y += gravidade_bola
                if circulo_bola.bottom >= 800:
                    circulo_bola.bottom = 800
                    gravidade_bola = (gravidade_bola * -0.7)
                    if abs(gravidade_bola) < 2:
                        gravidade_bola = 0

                circulo_bola.x += velocidade_bola
                if velocidade_bola > 23 or velocidade_bola < -23:
                    if velocidade_bola > 0:
                        velocidade_bola -= 1
                    elif velocidade_bola < 0:
                        velocidade_bola += 1
                else:
                    if velocidade_bola > 0:
                        velocidade_bola -= 0.5
                    elif velocidade_bola < 0:
                        velocidade_bola += 0.5

                if retangulo_jogador1.colliderect(circulo_bola):
                    gravidade_bola = -10
                    if retangulo_jogador1.centerx < circulo_bola.centerx:
                        velocidade_bola += 40
                    else:
                        velocidade_bola += -40

                if retangulo_jogador2.colliderect(circulo_bola):
                    gravidade_bola = -10
                    if retangulo_jogador2.centerx < circulo_bola.centerx:
                        velocidade_bola += 40
                    else:
                        velocidade_bola += -40 

                if velocidade_bola >= 60:
                    velocidade_bola = 60
                elif velocidade_bola <= -60:
                    velocidade_bola = -60

                if circulo_bola.left <= 150 and circulo_bola.bottom <= 510:
                    if velocidade_bola < 0:
                        velocidade_bola = velocidade_bola * -1
                if circulo_bola.right >= 1700 and circulo_bola.bottom <= 510:
                    if velocidade_bola >  0: 
                        velocidade_bola = velocidade_bola * -1

                if circulo_bola.left < 0 or circulo_bola.right > 1850:
                    if circulo_bola.left < 0:
                        comemoracao_jogador2.play()
                        pontuacaod2 += 1
                        if pontuacaod2 == 10:
                            pontuacaod1 += 1
                            pontuacaod2 = 0
                    if circulo_bola.right > 1850:
                        comemoracao_jogador1.play()
                        pontuacaoe2 += 1
                        if pontuacaoe2 == 10:
                            pontuacaoe1 += 1
                            pontuacaoe2 = 0

                    circulo_bola.center = (925,200)
                    retangulo_jogador1.bottomleft = (160, 800)
                    retangulo_jogador2.bottomright = (1690,800)
                    gravidade_bola = velocidade_bola = gravidade_jogador1 = gravidade_jogador2 = 0

                tempo_atual = pygame.time.get_ticks()
                tempo_jogado_segundos = (tempo_atual - tempo_inicio) // 1000 
                tempo_decrescente = 180 - tempo_jogado_segundos

                index_estadio = animacao_torcida(tela, estadio_movimento, index_estadio)

            minutos = tempo_decrescente // 60
            segundos = tempo_decrescente % 60

            placar_esquerda1 = fonte_pontuacao.render(str(pontuacaoe1), True, (255, 255, 0))
            placar_esquerda2 = fonte_pontuacao.render(str(pontuacaoe2), True, (255, 255, 0))
            placar_direita1 = fonte_pontuacao.render(str(pontuacaod1), True, (255, 255, 0))
            placar_direita2 = fonte_pontuacao.render(str(pontuacaod2), True, (255, 255, 0))
            tempo = fonte_tempo.render(f'{minutos}:{segundos}', True, (255, 255, 0))
            retangulo_tempo = tempo.get_rect(center = (925,867))

            imagem_atual1 = superficie_jogador1
            if chutando_jogador1:
                if tempo_atual - tempo_chute1 <=  250:
                    imagem_atual1  = chute_jogador1
            else:
                chutando_jogador1 = False

            imagem_atual2 = superficie_jogador2
            if chutando_jogador2:
                if tempo_atual - tempo_chute2 <=  250:
                    imagem_atual2  = chute_jogador2
            else:
                chutando_jogador2 = False

            imagem_campo(tela, superficie_placa, superficie_grama, escudo_maior, escudo_menor)
            imagem_placar(tela,superficie_placar, retangulo_placar, placar_esquerda1,placar_esquerda2,placar_direita1,placar_direita2,tempo,retangulo_tempo)
            movimento_jogador(tela, imagem_atual1, retangulo_jogador1, imagem_atual2, retangulo_jogador2)
            imagem_estadio(tela, superficie_gol_e, retangulo_gol_e, superficie_gol_d, retangulo_gol_d, superficie_bola,circulo_bola)

            if jogo_pausado:
                retangulo_continuar_pausa, retangulo_sair_pausa = imagem_esc(tela,fonte_texto)

            if tempo_decrescente <= 0:
                canto_torcida1.stop()
                canto_torcida2.stop()

                if pontuacaod1 > pontuacaoe1 or (pontuacaod1 == pontuacaoe1 and pontuacaod2 > pontuacaoe2):
                    tela.blit(vitoria2,retangulo_final)
                elif pontuacaod1 == pontuacaoe1 and pontuacaod2 == pontuacaoe2:
                    tela.blit(empate, retangulo_final)
                else:
                    tela.blit(vitoria1,retangulo_final)

                teclas_fim = pygame.key.get_pressed()
                if teclas_fim[pygame.K_SPACE]:
                    atividade_jogo = False

                    pontuacaoe1 = pontuacaoe2 = pontuacaod1 = pontuacaod2 = 0
                    retangulo_jogador1.bottomleft = (165, 800)
                    retangulo_jogador2.bottomright = (1690, 800)
                    circulo_bola.center = (925, 200)
                    velocidade_bola = gravidade_bola = 0
                    tempo_decrescente = 180

        # Redimensiona toda a cena de 1850x1000 para o monitor do usuario.
        tela_redimensionada = pygame.transform.smoothscale(
            tela, (largura_jogo, altura_jogo)
        )

        # Fundo preto nas sobras quando a proporcao da tela for diferente.
        tela_real.fill((0, 0, 0))
        tela_real.blit(tela_redimensionada, (offset_x, offset_y))

        pygame.display.update()
        clock.tick(60)

if (__name__ == '__main__'):
    main()
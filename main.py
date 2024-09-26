import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

from opengl_init import init_opengl
from graphics import draw_support_structure
from textures import load_texture
from camera import setup_camera, handle_camera_movement


# Variáveis do Pêndulo
length = 1.5         # Comprimento do pêndulo
gravity = 9.81       # Aceleração gravitacional
angle = math.pi / 2  # Ângulo inicial
angular_velocity = 0
damping = 0.01       # Amortecimento

# Variáveis para movimentação da câmera
camera_angle_x = 15.0  # Rotação ao longo do eixo X
camera_angle_y = 0.0  # Rotação ao longo do eixo Y
camera_distance = 6.0 # Distância da câmera

# Função para desenhar o pêndulo com textura
def draw_pendulum(angle, base_depth, sphere_texture):  
    glPushMatrix()

    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, sphere_texture)

    # Translação para a linha superior que conecta os suportes (frente e trás)
    glTranslatef(0.0, 2.0, 0.0)

    # Rotação do pêndulo (em torno do eixo Z)
    glRotatef(math.degrees(angle), 0.0, 0.0, 1.0)

    # Desenhar a linha frontal e traseira do pêndulo
    glDisable(GL_TEXTURE_2D)
    glBegin(GL_LINES)
    glVertex3f(0.0, 0.0, base_depth / 2)
    glVertex3f(0.0, -length, 0.0)
    glVertex3f(0.0, 0.0, -base_depth / 2)
    glVertex3f(0.0, -length, 0.0)
    glEnd()

    # Desenhar a esfera com textura
    glTranslatef(0.0, -length, 0.0)  # Posicionar a esfera no centro das linhas
    quadric = gluNewQuadric()
    gluQuadricTexture(quadric, GL_TRUE)
    gluSphere(quadric, 0.1, 20, 20)

    glDisable(GL_TEXTURE_2D)
    glPopMatrix()

# Função para atualizar a simulação do pêndulo
def update_pendulum(dt):
    global angle, angular_velocity, angular_acceleration

    angular_acceleration = -(gravity / length) * math.sin(angle)
    angular_velocity += angular_acceleration * dt
    angular_velocity *= (1 - damping)  # Aplicar amortecimento
    angle += angular_velocity * dt

def handle_speed_control(keys):
    global angular_velocity
    
    speed_increment = 0.1  # Valor para aumentar ou diminuir a velocidade
    
    if keys[K_EQUALS]: # Tecla "+"
        angular_velocity += speed_increment  # Aumenta a velocidade angular
    if keys[K_MINUS]:  # Tecla "-"
        angular_velocity -= speed_increment  # Diminui a velocidade angular

def main():
    pygame.init()
    display = (800, 600)
    base_depth = 1.5
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    init_opengl()

    # Carregar texturas
    base_texture = load_texture('assets/madera.bmp')
    sphere_texture = load_texture('assets/texture.jpg')

    # Variáveis do pêndulo
    global angle, angular_velocity, angular_acceleration
    angle = math.radians(20)  # Ângulo inicial (em radianos)
    angular_velocity = 0.0  # Velocidade angular inicial
    angular_acceleration = 0.0  # Aceleração angular inicial

    last_time = pygame.time.get_ticks() / 1000.0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        keys = pygame.key.get_pressed()
        handle_camera_movement(keys)
        handle_speed_control(keys)  # Controle da velocidade pelo teclado

        # Atualização do tempo
        current_time = pygame.time.get_ticks() / 1000.0
        dt = current_time - last_time
        last_time = current_time

        # Atualizar a simulação do pêndulo
        update_pendulum(dt)

        # Limpar a tela e o buffer de profundidade
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Configurar a câmera e desenhar a cena
        setup_camera()

        # Desenhar a estrutura de suporte e o pêndulo
        draw_support_structure(base_texture)
        draw_pendulum(angle, base_depth, sphere_texture)

        # Trocar os buffers e renderizar a cena
        pygame.display.flip()
        pygame.time.wait(20)

if __name__ == "__main__":
    main()
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import math

# Variáveis do Pêndulo
length = 1.5         # Comprimento do pêndulo
gravity = 9.81       # Aceleração gravitacional
angle = math.pi / 2  # Ângulo inicial
angular_velocity = 0
damping = 0.01       # Amortecimento

# Variáveis para movimentação da câmera
camera_angle_x = 0.0  # Rotação ao longo do eixo X
camera_angle_y = 0.0  # Rotação ao longo do eixo Y
camera_distance = 5.0 # Distância da câmera

# Função para carregar texturas
def load_texture(filename):
    texture_surface = pygame.image.load(filename)
    texture_data = pygame.image.tostring(texture_surface, "RGB", 1)
    width = texture_surface.get_width()
    height = texture_surface.get_height()

    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, texture_data)

    return texture_id

# Função para configurar a iluminação
def setup_lighting():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    light_position = [1.0, 1.0, 2.0, 1.0]
    light_ambient = [0.2, 0.2, 0.2, 1.0]
    light_diffuse = [0.7, 0.7, 0.7, 1.0]
    light_specular = [1.0, 1.0, 1.0, 1.0]

    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)

# Função para desenhar a base e suportes laterais com volume (cilindros) e uma base com volume
def draw_support_structure(base_texture):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, base_texture)

    glPushMatrix()

    base_height = 0.3  # Altura da base com volume
    base_width = 3.0
    base_depth = 1.5
    support_height = 2.0  # Altura das colunas verticais
    bar_radius = 0.05      # Raio dos cilindros (barras)

    # Desenhar a base como um bloco com volume (paralelepípedo) com textura
    glBegin(GL_QUADS)

    # Parte superior da base (com textura)
    glTexCoord2f(0, 0); glVertex3f(-base_width / 2, 0, base_depth / 2)
    glTexCoord2f(1, 0); glVertex3f(base_width / 2, 0, base_depth / 2)
    glTexCoord2f(1, 1); glVertex3f(base_width / 2, 0, -base_depth / 2)
    glTexCoord2f(0, 1); glVertex3f(-base_width / 2, 0, -base_depth / 2)

    # Parte inferior da base (com textura)
    glTexCoord2f(0, 0); glVertex3f(-base_width / 2, -base_height, base_depth / 2)
    glTexCoord2f(1, 0); glVertex3f(base_width / 2, -base_height, base_depth / 2)
    glTexCoord2f(1, 1); glVertex3f(base_width / 2, -base_height, -base_depth / 2)
    glTexCoord2f(0, 1); glVertex3f(-base_width / 2, -base_height, -base_depth / 2)

    # Frente da base (com textura)
    glTexCoord2f(0, 0); glVertex3f(-base_width / 2, -base_height, base_depth / 2)
    glTexCoord2f(1, 0); glVertex3f(base_width / 2, -base_height, base_depth / 2)
    glTexCoord2f(1, 1); glVertex3f(base_width / 2, 0, base_depth / 2)
    glTexCoord2f(0, 1); glVertex3f(-base_width / 2, 0, base_depth / 2)

    # Traseira da base (com textura)
    glTexCoord2f(0, 0); glVertex3f(-base_width / 2, -base_height, -base_depth / 2)
    glTexCoord2f(1, 0); glVertex3f(base_width / 2, -base_height, -base_depth / 2)
    glTexCoord2f(1, 1); glVertex3f(base_width / 2, 0, -base_depth / 2)
    glTexCoord2f(0, 1); glVertex3f(-base_width / 2, 0, -base_depth / 2)

    # Lado esquerdo da base (com textura)
    glTexCoord2f(0, 0); glVertex3f(-base_width / 2, -base_height, -base_depth / 2)
    glTexCoord2f(1, 0); glVertex3f(-base_width / 2, -base_height, base_depth / 2)
    glTexCoord2f(1, 1); glVertex3f(-base_width / 2, 0, base_depth / 2)
    glTexCoord2f(0, 1); glVertex3f(-base_width / 2, 0, -base_depth / 2)

    # Lado direito da base (com textura)
    glTexCoord2f(0, 0); glVertex3f(base_width / 2, -base_height, -base_depth / 2)
    glTexCoord2f(1, 0); glVertex3f(base_width / 2, -base_height, base_depth / 2)
    glTexCoord2f(1, 1); glVertex3f(base_width / 2, 0, base_depth / 2)
    glTexCoord2f(0, 1); glVertex3f(base_width / 2, 0, -base_depth / 2)

    glEnd()

    glDisable(GL_TEXTURE_2D)

    # Desenhar os suportes verticais (cilindros)
    quadric = gluNewQuadric()
    
    # Lado esquerdo da frente (ajustado)
    glPushMatrix()
    glTranslatef(-base_width / 2 + bar_radius, 0, base_depth / 2)  # Ajuste na posição
    glRotatef(-90, 1, 0, 0)  # Rotacionar para alinhar ao eixo Y
    gluCylinder(quadric, bar_radius, bar_radius, support_height, 20, 20)
    glPopMatrix()

    # Lado direito da frente (ajustado)
    glPushMatrix()
    glTranslatef(base_width / 2 - bar_radius, 0, base_depth / 2)  # Ajuste na posição
    glRotatef(-90, 1, 0, 0)
    gluCylinder(quadric, bar_radius, bar_radius, support_height, 20, 20)
    glPopMatrix()

    # Lado esquerdo de trás (ajustado)
    glPushMatrix()
    glTranslatef(-base_width / 2 + bar_radius, 0, -base_depth / 2)  # Ajuste na posição
    glRotatef(-90, 1, 0, 0)
    gluCylinder(quadric, bar_radius, bar_radius, support_height, 20, 20)
    glPopMatrix()

    # Lado direito de trás (ajustado)
    glPushMatrix()
    glTranslatef(base_width / 2 - bar_radius, 0, -base_depth / 2)  # Ajuste na posição
    glRotatef(-90, 1, 0, 0)
    gluCylinder(quadric, bar_radius, bar_radius, support_height, 20, 20)
    glPopMatrix()

    # Desenhar a barra superior conectando os suportes (cilindro horizontal)
    glPushMatrix()
    glTranslatef(-base_width / 2 + bar_radius, support_height, base_depth / 2)  # Mover para o topo do suporte
    glRotatef(90, 0, 1, 0)  # Rotacionar para alinhar ao eixo Z
    gluCylinder(quadric, bar_radius, bar_radius, base_width - 2 * bar_radius, 20, 20)
    glPopMatrix()

    # Desenhar a barra superior de trás (cilindro horizontal)
    glPushMatrix()
    glTranslatef(-base_width / 2 + bar_radius, support_height, -base_depth / 2)  # Mover para o topo do suporte de trás
    glRotatef(90, 0, 1, 0)
    gluCylinder(quadric, bar_radius, bar_radius, base_width - 2 * bar_radius, 20, 20)
    glPopMatrix()

    glPopMatrix()

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

# Configuração básica do OpenGL
def init_opengl():
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.2, 0.3, 0.3, 1.0)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 800 / 600, 0.1, 50.0)

    setup_lighting()

# Função para configurar a câmera e desenhar a cena
def setup_camera():
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    gluLookAt(camera_distance * math.sin(math.radians(camera_angle_y)),
              camera_distance * math.sin(math.radians(camera_angle_x)),
              camera_distance * math.cos(math.radians(camera_angle_y)),
              0.0, 0.0, 0.0,
              0.0, 1.0, 0.0)

# Função para tratar a movimentação da câmera
def handle_camera_movement(keys):
    global camera_angle_x, camera_angle_y, camera_distance

    camera_speed = 0.5
    zoom_speed = 0.1

    if keys[K_LEFT]:
        camera_angle_y -= camera_speed
    if keys[K_RIGHT]:
        camera_angle_y += camera_speed
    if keys[K_UP]:
        camera_angle_x -= camera_speed
    if keys[K_DOWN]:
        camera_angle_x += camera_speed
    if keys[K_w]:
        camera_distance -= zoom_speed
    if keys[K_s]:
        camera_distance += zoom_speed

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
    base_texture = load_texture('madera.bmp')
    sphere_texture = load_texture('texture.jpg')

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
        pygame.time.wait(10)

if __name__ == "__main__":
    main()

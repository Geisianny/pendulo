import math
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *

# Variáveis para movimentação da câmera
camera_angle_x = 15.0  # Rotação ao longo do eixo X
camera_angle_y = 0.0   # Rotação ao longo do eixo Y
camera_distance = 6.0  # Distância da câmera

# Função para configurar a câmera e desenhar a cena
def setup_camera():
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    gluLookAt(camera_distance * math.sin(math.radians(camera_angle_y)),
              camera_distance * math.sin(math.radians(camera_angle_x)),
              camera_distance * math.cos(math.radians(camera_angle_y)),
              0.0, 1, 0,
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

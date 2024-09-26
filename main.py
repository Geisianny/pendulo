import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

from opengl_init import init_opengl
from graphics import draw_support_structure
from textures import load_texture
from camera import setup_camera, handle_camera_movement


length = 1.5
gravity = 9.81
angle = math.pi / 2
angular_velocity = 0
damping = 0.01


def draw_pendulum(angle, base_depth, sphere_texture):  
    glPushMatrix()

    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, sphere_texture)

    glTranslatef(0.0, 2.0, 0.0)

    glRotatef(math.degrees(angle), 0.0, 0.0, 1.0)

    glDisable(GL_TEXTURE_2D)
    glBegin(GL_LINES)
    glVertex3f(0.0, 0.0, base_depth / 2)
    glVertex3f(0.0, -length, 0.0)
    glVertex3f(0.0, 0.0, -base_depth / 2)
    glVertex3f(0.0, -length, 0.0)
    glEnd()

    glTranslatef(0.0, -length, 0.0)
    quadric = gluNewQuadric()
    gluQuadricTexture(quadric, GL_TRUE)
    gluSphere(quadric, 0.1, 20, 20)

    glDisable(GL_TEXTURE_2D)
    glPopMatrix()

def update_pendulum(dt):
    global angle, angular_velocity, angular_acceleration

    angular_acceleration = -(gravity / length) * math.sin(angle)
    angular_velocity += angular_acceleration * dt
    angular_velocity *= (1 - damping)
    angle += angular_velocity * dt

def handle_speed_control(keys):
    global angular_velocity
    
    speed_increment = 0.1
    
    if keys[K_EQUALS]:
        angular_velocity += speed_increment 
    if keys[K_MINUS]: 
        angular_velocity -= speed_increment 

def main():
    pygame.init()
    display = (800, 600)
    base_depth = 1.5
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    init_opengl()

    base_texture = load_texture('assets/madera.bmp')
    sphere_texture = load_texture('assets/texture.jpg')

    global angle, angular_velocity, angular_acceleration
    angle = math.radians(20)
    angular_velocity = 0.0 
    angular_acceleration = 0.0 

    last_time = pygame.time.get_ticks() / 1000.0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        keys = pygame.key.get_pressed()
        handle_camera_movement(keys)
        handle_speed_control(keys)

        current_time = pygame.time.get_ticks() / 1000.0
        dt = current_time - last_time
        last_time = current_time

        update_pendulum(dt)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        setup_camera()

        draw_support_structure(base_texture)
        draw_pendulum(angle, base_depth, sphere_texture)

        pygame.display.flip()
        pygame.time.wait(20)

if __name__ == "__main__":
    main()
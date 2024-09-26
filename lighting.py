from OpenGL.GL import *

def setup_lighting():
    glEnable(GL_LIGHTING)
    
    glEnable(GL_LIGHT0)
    
    glEnable(GL_LIGHT1)
    
    glEnable(GL_LIGHT2)

    light0_position = [1.0, 1.0, 1.0, 0.0]
    light0_ambient = [0.1, 0.1, 0.1, 1.0]
    light0_diffuse = [0.8, 0.8, 0.8, 1.0]
    light0_specular = [1.0, 1.0, 1.0, 1.0]

    glLightfv(GL_LIGHT0, GL_POSITION, light0_position)
    glLightfv(GL_LIGHT0, GL_AMBIENT, light0_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light0_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light0_specular)

    light1_position = [-1.0, 0.5, 0.5, 0.0]
    light1_ambient = [0.2, 0.2, 0.2, 1.0]
    light1_diffuse = [0.3, 0.3, 0.3, 1.0]
    light1_specular = [0.0, 0.0, 0.0, 1.0]

    glLightfv(GL_LIGHT1, GL_POSITION, light1_position)
    glLightfv(GL_LIGHT1, GL_AMBIENT, light1_ambient)
    glLightfv(GL_LIGHT1, GL_DIFFUSE, light1_diffuse)
    glLightfv(GL_LIGHT1, GL_SPECULAR, light1_specular)

    light2_position = [0.0, -1.0, -1.0, 0.0]
    light2_ambient = [0.1, 0.1, 0.1, 1.0]
    light2_diffuse = [0.2, 0.2, 0.2, 1.0]
    light2_specular = [0.0, 0.0, 0.0, 1.0]

    glLightfv(GL_LIGHT2, GL_POSITION, light2_position)
    glLightfv(GL_LIGHT2, GL_AMBIENT, light2_ambient)
    glLightfv(GL_LIGHT2, GL_DIFFUSE, light2_diffuse)
    glLightfv(GL_LIGHT2, GL_SPECULAR, light2_specular)
    
    global_ambient = [0.2, 0.2, 0.2, 1.0]
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, global_ambient)
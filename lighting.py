from OpenGL.GL import *

def setup_lighting():
    glEnable(GL_LIGHTING)
    
    # Luz principal (forte)
    glEnable(GL_LIGHT0)
    
    # Luz de preenchimento suave
    glEnable(GL_LIGHT1)
    
    # Luz de fundo para suavizar sombras
    glEnable(GL_LIGHT2)

    # Configurações da luz principal (luz solar)
    light0_position = [1.0, 1.0, 1.0, 0.0]  # Direção da luz solar
    light0_ambient = [0.1, 0.1, 0.1, 1.0]  # Baixa iluminação ambiente
    light0_diffuse = [0.8, 0.8, 0.8, 1.0]  # Luz difusa forte
    light0_specular = [1.0, 1.0, 1.0, 1.0]  # Reflexão especular forte

    glLightfv(GL_LIGHT0, GL_POSITION, light0_position)
    glLightfv(GL_LIGHT0, GL_AMBIENT, light0_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light0_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light0_specular)

    # Configurações da luz de preenchimento (suave, sem sombras marcantes)
    light1_position = [-1.0, 0.5, 0.5, 0.0]  # Posição oposta à luz principal
    light1_ambient = [0.2, 0.2, 0.2, 1.0]  # Ambiente suave
    light1_diffuse = [0.3, 0.3, 0.3, 1.0]  # Luz difusa fraca
    light1_specular = [0.0, 0.0, 0.0, 1.0]  # Sem reflexão especular

    glLightfv(GL_LIGHT1, GL_POSITION, light1_position)
    glLightfv(GL_LIGHT1, GL_AMBIENT, light1_ambient)
    glLightfv(GL_LIGHT1, GL_DIFFUSE, light1_diffuse)
    glLightfv(GL_LIGHT1, GL_SPECULAR, light1_specular)

    # Luz de fundo para suavizar sombras
    light2_position = [0.0, -1.0, -1.0, 0.0]  # Luz de fundo para suavizar sombras
    light2_ambient = [0.1, 0.1, 0.1, 1.0]  # Ambiente suave
    light2_diffuse = [0.2, 0.2, 0.2, 1.0]  # Luz difusa fraca
    light2_specular = [0.0, 0.0, 0.0, 1.0]  # Sem reflexão especular

    glLightfv(GL_LIGHT2, GL_POSITION, light2_position)
    glLightfv(GL_LIGHT2, GL_AMBIENT, light2_ambient)
    glLightfv(GL_LIGHT2, GL_DIFFUSE, light2_diffuse)
    glLightfv(GL_LIGHT2, GL_SPECULAR, light2_specular)

    # Aumentar levemente a iluminação ambiente global da cena
    global_ambient = [0.2, 0.2, 0.2, 1.0]
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, global_ambient)
from OpenGL.GL import *
from OpenGL.GLU import *

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
    glNormal3f(0, 1, 0)  # Normal para cima
    glTexCoord2f(0, 0); glVertex3f(-base_width / 2, 0, base_depth / 2)
    glTexCoord2f(1, 0); glVertex3f(base_width / 2, 0, base_depth / 2)
    glTexCoord2f(1, 1); glVertex3f(base_width / 2, 0, -base_depth / 2)
    glTexCoord2f(0, 1); glVertex3f(-base_width / 2, 0, -base_depth / 2)

    # Parte inferior da base (com textura)
    glNormal3f(0, -1, 0)  # Normal para baixo
    glTexCoord2f(0, 0); glVertex3f(-base_width / 2, -base_height, base_depth / 2)
    glTexCoord2f(1, 0); glVertex3f(base_width / 2, -base_height, base_depth / 2)
    glTexCoord2f(1, 1); glVertex3f(base_width / 2, -base_height, -base_depth / 2)
    glTexCoord2f(0, 1); glVertex3f(-base_width / 2, -base_height, -base_depth / 2)

    # Frente da base (com textura)
    glNormal3f(0, 0, 1)  # Normal para frente
    glTexCoord2f(0, 0); glVertex3f(-base_width / 2, -base_height, base_depth / 2)
    glTexCoord2f(1, 0); glVertex3f(base_width / 2, -base_height, base_depth / 2)
    glTexCoord2f(1, 1); glVertex3f(base_width / 2, 0, base_depth / 2)
    glTexCoord2f(0, 1); glVertex3f(-base_width / 2, 0, base_depth / 2)

    # Traseira da base (com textura)
    glNormal3f(0, 0, -1)  # Normal para trás
    glTexCoord2f(0, 0); glVertex3f(-base_width / 2, -base_height, -base_depth / 2)
    glTexCoord2f(1, 0); glVertex3f(base_width / 2, -base_height, -base_depth / 2)
    glTexCoord2f(1, 1); glVertex3f(base_width / 2, 0, -base_depth / 2)
    glTexCoord2f(0, 1); glVertex3f(-base_width / 2, 0, -base_depth / 2)

    # Lado esquerdo da base (com textura)
    glNormal3f(-1, 0, 0)  # Normal para o lado esquerdo
    glTexCoord2f(0, 0); glVertex3f(-base_width / 2, -base_height, -base_depth / 2)
    glTexCoord2f(1, 0); glVertex3f(-base_width / 2, -base_height, base_depth / 2)
    glTexCoord2f(1, 1); glVertex3f(-base_width / 2, 0, base_depth / 2)
    glTexCoord2f(0, 1); glVertex3f(-base_width / 2, 0, -base_depth / 2)

    # Lado direito da base (com textura)
    glNormal3f(1, 0, 0)  # Normal para o lado direito
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

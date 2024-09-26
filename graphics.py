from OpenGL.GL import *
from OpenGL.GLU import *

def draw_support_structure(base_texture):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, base_texture)

    glPushMatrix()

    base_height = 0.3
    base_width = 3.0
    base_depth = 1.5
    support_height = 2.0
    bar_radius = 0.05

    glBegin(GL_QUADS)

    glNormal3f(0, 1, 0)
    glTexCoord2f(0, 0); glVertex3f(-base_width / 2, 0, base_depth / 2)
    glTexCoord2f(1, 0); glVertex3f(base_width / 2, 0, base_depth / 2)
    glTexCoord2f(1, 1); glVertex3f(base_width / 2, 0, -base_depth / 2)
    glTexCoord2f(0, 1); glVertex3f(-base_width / 2, 0, -base_depth / 2)

    glNormal3f(0, -1, 0)
    glTexCoord2f(0, 0); glVertex3f(-base_width / 2, -base_height, base_depth / 2)
    glTexCoord2f(1, 0); glVertex3f(base_width / 2, -base_height, base_depth / 2)
    glTexCoord2f(1, 1); glVertex3f(base_width / 2, -base_height, -base_depth / 2)
    glTexCoord2f(0, 1); glVertex3f(-base_width / 2, -base_height, -base_depth / 2)

    glNormal3f(0, 0, 1)
    glTexCoord2f(0, 0); glVertex3f(-base_width / 2, -base_height, base_depth / 2)
    glTexCoord2f(1, 0); glVertex3f(base_width / 2, -base_height, base_depth / 2)
    glTexCoord2f(1, 1); glVertex3f(base_width / 2, 0, base_depth / 2)
    glTexCoord2f(0, 1); glVertex3f(-base_width / 2, 0, base_depth / 2)

    glNormal3f(0, 0, -1)
    glTexCoord2f(0, 0); glVertex3f(-base_width / 2, -base_height, -base_depth / 2)
    glTexCoord2f(1, 0); glVertex3f(base_width / 2, -base_height, -base_depth / 2)
    glTexCoord2f(1, 1); glVertex3f(base_width / 2, 0, -base_depth / 2)
    glTexCoord2f(0, 1); glVertex3f(-base_width / 2, 0, -base_depth / 2)

    glNormal3f(-1, 0, 0)
    glTexCoord2f(0, 0); glVertex3f(-base_width / 2, -base_height, -base_depth / 2)
    glTexCoord2f(1, 0); glVertex3f(-base_width / 2, -base_height, base_depth / 2)
    glTexCoord2f(1, 1); glVertex3f(-base_width / 2, 0, base_depth / 2)
    glTexCoord2f(0, 1); glVertex3f(-base_width / 2, 0, -base_depth / 2)

    glNormal3f(1, 0, 0)
    glTexCoord2f(0, 0); glVertex3f(base_width / 2, -base_height, -base_depth / 2)
    glTexCoord2f(1, 0); glVertex3f(base_width / 2, -base_height, base_depth / 2)
    glTexCoord2f(1, 1); glVertex3f(base_width / 2, 0, base_depth / 2)
    glTexCoord2f(0, 1); glVertex3f(base_width / 2, 0, -base_depth / 2)

    glEnd()

    glDisable(GL_TEXTURE_2D)

    quadric = gluNewQuadric()
    
    glPushMatrix()
    glTranslatef(-base_width / 2 + bar_radius, 0, base_depth / 2)
    glRotatef(-90, 1, 0, 0)
    gluCylinder(quadric, bar_radius, bar_radius, support_height, 20, 20)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(base_width / 2 - bar_radius, 0, base_depth / 2)
    glRotatef(-90, 1, 0, 0)
    gluCylinder(quadric, bar_radius, bar_radius, support_height, 20, 20)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-base_width / 2 + bar_radius, 0, -base_depth / 2)
    glRotatef(-90, 1, 0, 0)
    gluCylinder(quadric, bar_radius, bar_radius, support_height, 20, 20)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(base_width / 2 - bar_radius, 0, -base_depth / 2)
    glRotatef(-90, 1, 0, 0)
    gluCylinder(quadric, bar_radius, bar_radius, support_height, 20, 20)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-base_width / 2 + bar_radius, support_height, base_depth / 2)
    glRotatef(90, 0, 1, 0)
    gluCylinder(quadric, bar_radius, bar_radius, base_width - 2 * bar_radius, 20, 20)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-base_width / 2 + bar_radius, support_height, -base_depth / 2)
    glRotatef(90, 0, 1, 0)
    gluCylinder(quadric, bar_radius, bar_radius, base_width - 2 * bar_radius, 20, 20)
    glPopMatrix()

    glPopMatrix()

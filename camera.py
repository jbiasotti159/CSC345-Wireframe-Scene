# ==============================
# James Jacobson, Neel Bains, Jill Biasotti, Joe Ruiz, Julia Wilkinson, Lauren Atkinson
# CSC345: Computer Graphics
#   Spring 2021
# Description:
#   Assignment 2 for graphics: Creating car animation with 2 cones and a moving camera
# ==============================

import math
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from utils import *

class Camera:
   

    def __init__(self, camAngle=45, aspRatio=1, near=0.1, far=1000, eye=Point(0,0,0), lookAngle=0):

        self.camAngle = camAngle
        self.aspRatio = aspRatio
        self.near = near
        self.far = far
        self.eye = eye
        self.lookAngle = lookAngle

    def __str__(self):
        #camera description
        return "Camera Eye at %s with angle (%f)"%(self.eye, self.lookAngle)

    # moves view to set projection 
    def setProjection(self):
        glMatrixMode(GL_PROJECTION);
        glLoadIdentity();
        gluPerspective(self.camAngle, self.aspRatio, self.near, self.far)
    
    def placeCamera(self):
        glMatrixMode(GL_MODELVIEW);
        glLoadIdentity();

        # Compute the look at point based on the turn angle
        rad = math.radians(self.lookAngle)
        lookX = self.eye.x - math.sin(rad)
        lookY = self.eye.y
        lookZ = self.eye.z - math.cos(rad)

        # Place the camera
        gluLookAt(self.eye.x, self.eye.y, self.eye.z,  
                  lookX, lookY, lookZ,                
                  0, 1, 0)                             

    #move camera along x, y, z axes     
    def slide(self, du, dv, dn):
        rad = math.radians(self.lookAngle)
        lookDX = math.sin(rad)
        lookDZ = math.cos(rad)
        
        self.eye.x += dn*lookDX
        self.eye.y += dv
        self.eye.z += dn*lookDZ
    
    #rotate camera by given angle
    def turn(self, angle):
        self.lookAngle += angle
        if self.lookAngle < 0: self.lookAngle += 360  
        elif self.lookAngle >= 360: self.lookAngle -= 360  
        

# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""
import OpenGL.GL as gl

class Section:
    # Constructor
    def __init__(self, parameters = {}) :  
        # Parameters
        # position: position of the wall 
        # width: width of the wall - mandatory
        # height: height of the wall - mandatory
        # thickness: thickness of the wall
        # color: color of the wall        

        # Sets the parameters
        self.parameters = parameters
        
        # Sets the default parameters
        if 'position' not in self.parameters:
            self.parameters['position'] = [0, 0, 0]        
        if 'width' not in self.parameters:
            raise Exception('Parameter "width" required.')   
        if 'height' not in self.parameters:
            raise Exception('Parameter "height" required.')   
        if 'orientation' not in self.parameters:
            self.parameters['orientation'] = 0              
        if 'thickness' not in self.parameters:
            self.parameters['thickness'] = 0.2    
        if 'color' not in self.parameters:
            self.parameters['color'] = [0.5, 0.5, 0.5]       
        if 'edges' not in self.parameters:
            self.parameters['edges'] = False             
            
        # Objects list
        self.objects = []

        # Generates the wall from parameters
        self.generate()   
        
    # Getter
    def getParameter(self, parameterKey):
        return self.parameters[parameterKey]
    
    # Setter
    def setParameter(self, parameterKey, parameterValue):
        self.parameters[parameterKey] = parameterValue
        return self     

    # Defines the vertices and faces 
    def generate(self):
        self.vertices = [ 
                [0, 0, 0 ],
                [0, 0, self.parameters['height']], 
                [self.parameters['width'], 0, self.parameters['height']],
                [self.parameters['width'], 0, 0],
                [0, self.parameters['thickness'], 0 ], 
                [0, self.parameters['thickness'], self.parameters['height']], 
                [self.parameters['width'], self.parameters['thickness'], self.parameters['height']],
                [self.parameters['width'], self.parameters['thickness'], 0]
                ]
        self.faces = [
                [0, 3, 2, 1],
                [0, 1, 5, 4],
                [0, 3, 7, 4],
                [6, 2, 1, 5],
                [6, 5, 4, 7],
                [6, 2, 3, 7]
                ]   

    # Checks if the opening can be created for the object x
    def canCreateOpening(self, x):
        if self.getParameter('position')[0]<x.getParameter('position')[0] and self.getParameter('position')[1]==x.getParameter('position')[1]and self.getParameter('position')[2]<x.getParameter('position')[2] and self.getParameter('position')[0]+self.getParameter('width')>x.getParameter('position')[0]+x.getParameter('width') and self.getParameter('thickness')==x.getParameter('thickness') and self.getParameter('position')[2]+self.getParameter('height')>x.getParameter('position')[2]+x.getParameter('height'):
          return True
    # Creates the new sections for the object x
    def createNewSections(self, x):
        # A compléter en remplaçant pass par votre code
        pass              
        
    # Draws the edges
    def drawEdges(self):
        gl.glPushMatrix()
        gl.glTranslatef(self.parameters['position'][0],self.parameters['position'][1],self.parameters['position'][2])
        gl.glRotatef(self.parameters['orientation'],0,0,1)
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_LINE) # on trace les faces : GL_FILL
        gl.glBegin(gl.GL_QUADS) # Tracé d’un quadrilatère
        gl.glColor3fv([0, 0, 0]) # Couleur noir
        for k in self.faces:
          for i in k:
              gl.glVertex3fv(self.vertices[i])
        gl.glEnd()
        gl.glPopMatrix()
                    
    # Draws the faces
    def draw(self):
        if self.parameters['edges']==True:
            self.drawEdges()
        gl.glPushMatrix()
        gl.glTranslatef(self.parameters['position'][0],self.parameters['position'][1],self.parameters['position'][2])
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL) # on trace les faces : GL_FILL
        gl.glBegin(gl.GL_QUADS) # Tracé d’un quadrilatère
        gl.glColor3fv([0.5, 0.5, 0.5]) # Couleur gris moyen
        for k in self.faces:
          for i in k:
              gl.glVertex3fv(self.vertices[i])
        gl.glEnd()
        gl.glPopMatrix()

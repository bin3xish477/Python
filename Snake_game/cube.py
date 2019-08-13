from snake import *
import pygame

class cube(object):
	rows = 20
	columns = 600
	def __init__(self,start,dirnx=1, dirny=0,color=(255,0,0)):
		self.pos = start
		self.dirnx = 1
		self.dirny = 0
		self.color = color

	def move(self,dirnx, dirny):
		self.dirnx = dirnx
		self.dirny = dirny
		self.pos = (self.pos[0] + self.dirnx,self.pos[1] + self.dirny)

	def draw(self, surface,eyes=False):
		dist = self.columns // self.rows
		i = self.pos[0]
		j = self.pos[1]

		pygame.draw.rect(surface,self.color,(i*dist+1,j*dist+1,dist-2,dist-2))

		if eyes:
			centre = dist // 2
			radius = 3
			circleMiddle = (i*dist+centre-radius,j*dist+8)
			circleMiddle2 = (i*dist+dist-radius*2,j*dist+8)
			pygame.draw.circle(surface,(0,0,0), circleMiddle, radius)
			pygame.draw.circle(surface,(0,0,0), circleMiddle2, radius)
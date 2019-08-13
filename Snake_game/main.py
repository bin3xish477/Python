'''
Snake game with pygame
'''

import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox
from snake import *
from cube import *

def drawGrid(column,rows,surface):
	size_betw = columns // rows

	x = 0
	y = 0
	for l in range(rows):
		x += size_betw
		y += size_betw

		pygame.draw.line(surface, (255,255,255), (x,0), (x,columns))
		pygame.draw.line(surface, (255,255,255), (0,y), (columns,y))


def redrawWindow(surface):
	global rows,columns,s,snack
	surface.fill((0,0,0))
	s.draw(surface)
	snack.draw(surface)
	drawGrid(columns,rows,surface)
	pygame.display.update()

def randomSnack(rows,item):
	positions = item.body

	while True:
		x = random.randrange(rows)
		y = random.randrange(rows)
		if len(list(filter(lambda x:x.pos == (x,y), positions))) > 0:
			continue
		else:
			break

	return (x,y)

def message_box(subject,content):
	root = tk.Tk()
	root.attributes('-topmost', True)
	root.withdraw()
	messagebox.showinfo(subject,content)
	try:root.destroy()
	except:pass

def main():
	global columns,rows,s,snack
	columns = 600
	height = 600
	rows = 20
	win = pygame.display.set_mode((columns, height))
	s = snake((255,0,0),(10,10))
	snack = cube(randomSnack(rows,s), color=(0,255,0))
	flag = True

	clock = pygame.time.Clock()

	while flag:
		pygame.time.delay(50)
		clock.tick(10)
		s.move()
		if s.body[0].pos == snack.pos:
			s.addCube()
			snack = cube(randomSnack(rows,s), color=(0,255,0))

		for x in range(len(s.body)):
			if s.body[x].pos in list(map(lambda x:x.pos,s.body[x+1:])):
				print('Score: ' + str(len(s.body)))
				message_box('You lost!', 'Play again')
				s.reset((10,10))
				break

		redrawWindow(win)
	pass

if __name__ == '__main__':
	main()
  

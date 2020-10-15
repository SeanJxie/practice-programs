
import os
import time

"""
Graphics in the console with Python.
"""


class ConsoleDisplay:
	def __init__(self, wt: int, ht: int, char='█'):
		self.wt = wt
		self.ht = ht
		self.char = char

		self.surfaceStr = char * wt

		self.draw_coords = []

	def draw_surface(self):
	    for i in range(self.ht):
	    	self.surfaceStr = self.char * self.wt

	    	for c in self.draw_coords:
	    		if i == c[1]:
	    			tempList = list(self.surfaceStr)
	    			tempList[c[0]] = c[2]
	    			self.surfaceStr = ''.join(tempList)

	    	print(self.surfaceStr)

	def draw_point(self, x, y, char):
		self.draw_coords.append((x, y, char))

	def clear(self):
		self.draw_coords = []

	def update(self):
		os.system('CLS') # Clear screen command


WT, HT = 40, 10
displayInstance = ConsoleDisplay(WT, HT)
MAXFPS = 60
sTime = 0

x = 0
y = 0

speedX = 1
speedY = 1

while 1:
	fTime = time.time()

	displayInstance.draw_point(x, y, 'O')
	displayInstance.draw_surface()
	
	x += speedX
	y += speedY

	if y > HT - 1 or y < 0:
		speedY *= -1
	if x > WT - 2 or x < 0:
		speedX *= -1

	if sTime > 0:
		time.sleep(sTime)

	lTime = time.time()

	dTime = lTime - fTime
	sTime = 1 / MAXFPS - dTime

	print(1 / dTime, x, y)

	displayInstance.clear()
	displayInstance.update()

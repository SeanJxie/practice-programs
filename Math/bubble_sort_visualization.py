import pygame
import sys
import random

"""

A visualization of the Bubble Sort algorithm using rectangles.


"""

# Colors
WINDOW = (2000, 700)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
BLUE = (0, 0, 255)
SPECIAL_COL = (123, 123, 255)


def visualize_list(surface, l):
	rect_width = WINDOW[0] / len(l)
	x = 0

	scale_factor = WINDOW[1] / max([e[0] for e in l])

	for value in l:
		pygame.draw.rect(surface, value[1], (x, WINDOW[1], rect_width, -value[0] * scale_factor))
		x += rect_width


def generate_random_int_input_list(n, inclusiveMin, inclusiveMax):
	output = []

	for _ in range(n):
		val = random.randint(inclusiveMin, inclusiveMax)
		output.append([val, SPECIAL_COL])

	return output

def bubble_sort_single_iter(lst):
	for i in range(1, len(lst)):
		if lst[i - 1][0] > lst[i][0]:
			temp = lst[i - 1][0]
			lst[i - 1][0] = lst[i][0]
			lst[i][0] = temp


	return lst



def main():
	pygame.init()
	WINDOW_SURFACE = pygame.display.set_mode(WINDOW)
	pygame.display.set_caption("Bubble Sort Visualization")

	input_list = generate_random_int_input_list(n=500, inclusiveMin=1, inclusiveMax=10000)

	SORT_TICK_INTERVAL = 1
	tick_count = 1

	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.display.quit()
				sys.exit()

		if tick_count == SORT_TICK_INTERVAL:
			input_list = bubble_sort_single_iter(input_list)
			tick_count = 0


		WINDOW_SURFACE.fill(WHITE)
		visualize_list(WINDOW_SURFACE, input_list)
		pygame.display.update()
		tick_count += 1



if __name__ == "__main__":
	main()


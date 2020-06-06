import arcade as acd
from PyGrapher import function

WINDOW_SIZE = (700, 700)
WINDOW_TITLE = 'Interactive Graph'
UPDATE_INTERVAL = 1 / 60  # Seconds

HALF_WINDOW_WT = WINDOW_SIZE[0] / 2
HALF_WINDOW_HT = WINDOW_SIZE[1] / 2
GRAPH_COL = (255, 0, 0)  # Red
BACKGROUND_COL = (255, 255, 255)  # White
AXIS_COL = (0, 0, 0)  # Black

LINE_WIDTH_FACTOR = 100  # The lower, the thicker the line
ZOOM_RENDER_COMPENSATION = 50  # The higher the number, the higher the quality and the lower the frame rate

while 1:  # Program loop.

    expression = input('Input function: y=')
    precision = float(input('Input x-step: '))

    print()

    zoom = 0  # Applied to all values in their respective directions
    x_offset = 0  # Applied to all x-values
    y_offset = 0  # Applied to all y-values


    def render_graph(points, line_width):
        for i in range(len(points) - 1):

            if points[i][1] is not None and points[i + 1][1] is not None:
                line = acd.create_line(points[i][0], points[i][1], points[i + 1][0], points[i + 1][1], GRAPH_COL, line_width)
                acd.render(line)


    def update(delta_time):
        global scale
        acd.start_render()
        scale = 1 + zoom  # Standard viewport/domain is 1. We add/subtract the zoom var to scale up and down the graph.

        # Render axis:
        acd.draw_line(0, -scale + y_offset, 0, scale + y_offset, AXIS_COL, scale / LINE_WIDTH_FACTOR)
        acd.draw_line(-scale + x_offset, 0, scale + x_offset, 0, AXIS_COL, scale / LINE_WIDTH_FACTOR)

        if zoom >= 0:
            acd.set_viewport(-scale + x_offset, scale + x_offset, -scale + y_offset, scale + y_offset)

        new_domain = [-scale + x_offset, scale + x_offset]

        # As the user zooms out, graph precision decreases to compensate for more rendering.
        func = function.Function(expression=expression, domain=new_domain, precision=scale / ZOOM_RENDER_COMPENSATION)

        render_graph(func.get_point_set(), line_width=scale / LINE_WIDTH_FACTOR)


    def scroll(x, y, scroll_x, scroll_y):
        global zoom
        if scroll_y < 0:
            zoom += 1

        elif scroll_y > 0 and zoom > 0:
            zoom -= 1


    def drag(x, y, dx, dy, button, modifiers):
        global x_offset, y_offset

        if button == acd.MOUSE_BUTTON_LEFT:
            x_offset -= dx
            y_offset -= dy


    def main():
        acd.open_window(WINDOW_SIZE[0], WINDOW_SIZE[1], WINDOW_TITLE)
        acd.schedule(update, UPDATE_INTERVAL)

        acd.set_background_color(BACKGROUND_COL)

        window = acd.get_window()
        window.on_mouse_scroll = scroll
        window.on_mouse_drag = drag

        acd.run()


    if __name__ == '__main__':
        main()

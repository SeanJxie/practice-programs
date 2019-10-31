"""
A simple camera that tracks a point.

"""

import arcade as acd
from code import settings as st


class Camera:
    def __init__(self, track_x, track_y):
        self.tx = track_x
        self.ty = track_y

    def track(self):
        acd.set_viewport(
            self.tx - st.SCREEN_WIDTH / 2, self.tx + st.SCREEN_WIDTH / 2,
            self.ty - st.SCREEN_HEIGHT / 2, self.ty + st.SCREEN_HEIGHT / 2
        )

    def get_camera_center(self):
        return self.tx, self.ty

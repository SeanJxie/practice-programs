import pygame as pg
import sys
import math
import random

import matrix

WINWT = 2560
WINHT = 1440

pg.init()

MAIN_SURFACE = pg.display.set_mode((WINWT // 2, WINHT // 2))
pg.display.set_caption("Perspective Projection")


def camera_transform(proj_point, cam, theta):
    m1 = matrix.M3xN(3)
    m1.set_entire(
        [
            [1,                   0,                  0], 
            [0, math.cos(theta[0]) , math.sin(theta[0])],
            [0, -math.sin(theta[0]), math.cos(theta[0])]
        ]
    )

    m2 = matrix.M3xN(3)
    m2.set_entire(
        [
            [math.cos(theta[1]), 0, -math.sin(theta[1])], 
            [0                 , 1,                   0],
            [math.sin(theta[1]), 0,  math.cos(theta[1])]
        ]
    )

    m3 = matrix.M3xN(3)
    m3.set_entire(
        [
            [math.cos(theta[2]) , math.sin(theta[2]), 0], 
            [-math.sin(theta[2]), math.cos(theta[2]), 0],
            [0                  , 0                 , 1]
        ]
    )

    m4 = matrix.M3xN(1)
    m4.set_entire(
        [
            [proj_point[0]],
            [proj_point[1]],
            [proj_point[2]]
        ]
    )

    m5 = matrix.M3xN(1)
    m5.set_entire(
        [
            [cam[0]],
            [cam[1]],
            [cam[2]]
        ]
    )

    return m1 * m2 * m3 * (m4 - m5)


def main():
    CAMERA_POS       = [0, 0, -1]
    ANGLE            = [0, 0, 0]
    IMAGE_PLANE      = [0, 0, 1]

    #vertices = load_obj.get_v_list("spoon.obj")
    vertices = [
        [random.randint(0, 100) for _ in range(3)] for _ in range(100)
    ]

    up = False
    down = False
    left = False
    right = False
    m_in = False
    m_out = False

    yaw = False
    pitch = False
    roll = False

    speed = 1
    rspeed = 0.01

    while 1:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    right = True
                elif event.key == pg.K_LEFT:
                    left = True
                elif event.key == pg.K_DOWN: 
                    down = True
                elif event.key == pg.K_UP: 
                    up = True
                elif event.key == pg.K_w: 
                    m_in = True
                elif event.key == pg.K_s: 
                    m_out = True

                elif event.key == pg.K_z:
                    yaw = True
                elif event.key == pg.K_x:
                    pitch = True
                elif event.key == pg.K_c:
                    roll = True

            elif event.type == pg.KEYUP:
                if event.key == pg.K_RIGHT:
                    right = False
                elif event.key == pg.K_LEFT:
                    left = False
                elif event.key == pg.K_DOWN: 
                    down = False
                elif event.key == pg.K_UP: 
                    up = False
                elif event.key == pg.K_w: 
                    m_in = False
                elif event.key == pg.K_s: 
                    m_out = False

                elif event.key == pg.K_z:
                    yaw = False
                elif event.key == pg.K_x:
                    pitch = False
                elif event.key == pg.K_c:
                    roll = False

        if right:
            CAMERA_POS[0] += speed
        if left:
            CAMERA_POS[0] -= speed
        if up: 
            CAMERA_POS[1] -= speed
        if down: 
            CAMERA_POS[1] += speed
        if m_in: 
            CAMERA_POS[2] += speed
        if m_out: 
            CAMERA_POS[2] -= speed
        if yaw:
            ANGLE[0] += rspeed
        if pitch:
            ANGLE[1] += rspeed
        if pitch:
            ANGLE[2] += rspeed


        MAIN_SURFACE.fill((0, 0, 0))

        for p in vertices:
            proj = camera_transform(
                p, 
                CAMERA_POS, 
                ANGLE, 
            )

            dz = proj.get(2, 0)
            if dz != 0:
                x = (proj.get(0, 0) - IMAGE_PLANE[0]) * (IMAGE_PLANE[2] / dz)
                y = (proj.get(1, 0) - IMAGE_PLANE[1]) * (IMAGE_PLANE[2] / dz)

                pg.draw.circle(MAIN_SURFACE, [random.randint(0, 255) for _ in range(3)], (x * 50, y * 50), 5)
    
        pg.display.update()


if __name__ == "__main__":
    main()

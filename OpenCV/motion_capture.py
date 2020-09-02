import cv2

"""

Motion Capture

"""


def avg_rgb(image, square_size):
    total = (0, 0, 0)
    count = 1

    half_ht = window_size['ht'] // 2
    half_wt = window_size['wt'] // 2

    for x in range(half_ht - square_size // 2, half_ht + square_size // 2 + 1):
        for y in range(half_wt - square_size // 2, half_wt + square_size // 2 + 1):
            total = add_lists(total, image[x, y])
            count += 1

    return [c / count for c in total]


def check_rgb_change(prev, curr, offset):
    change = False

    for i in range(3):
        if not (curr[i] - offset <= prev[i] <= curr[i] + offset):
            change = True
            break

    return change


def add_lists(l1, l2):
    return [a + b for a, b in list(zip(l1, l2))]


cap = cv2.VideoCapture(0)

window_size = {'obtained': False, 'wt': 0, 'ht': 0}
WIN_NAME = 'Mobile Capture'

prev_rgb = []
capture_count = 1

while 1:
    ret, frame = cap.read()

    if ret:
        if not window_size['obtained']:
            window_size['wt'], window_size['ht'] = cv2.getWindowImageRect(WIN_NAME)[2:]
            window_size['obtained'] = True

        cv2.imshow(WIN_NAME, frame)

        curr_rgb = avg_rgb(frame, 100)
        if prev_rgb and check_rgb_change(prev_rgb, curr_rgb, 2):
            print('Movement detected')
            cv2.imwrite(f'MotionCapture{capture_count}.jpg', frame)
            capture_count += 1
        prev_rgb = curr_rgb

    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()

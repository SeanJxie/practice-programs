import cv2

"""

Motion Detect

"""

def avg_rgb(image, square_size):
    total = (0, 0, 0)
    count = 0

    half_ht = window_size['ht'] // 2
    half_wt = window_size['wt'] // 2

    for x in range(half_wt - square_size // 2, half_wt + square_size // 2 + 1):
        for y in range(half_ht - square_size // 2, half_ht + square_size // 2 + 1):
            total = add_lists(total, image[y, x])
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
WIN_NAME = 'Video'

prev_rgb = []
capture_count = 1

DETECTION_SIZE = 100

while 1:
    ret, frame = cap.read()

    if ret:
        if not window_size['obtained']:
            window_size['ht'], window_size['wt'] = frame.shape[:2]
            window_size['obtained'] = True

        p1 = window_size['wt'] // 2 - DETECTION_SIZE // 2, window_size['ht'] // 2 - DETECTION_SIZE // 2
        p2 = window_size['wt'] // 2 + DETECTION_SIZE // 2, window_size['ht'] // 2 + DETECTION_SIZE // 2
        cv2.rectangle(frame, p1, p2, (0, 0, 0))

        cv2.imshow(WIN_NAME, frame)

        curr_rgb = avg_rgb(frame, DETECTION_SIZE)
        if prev_rgb and check_rgb_change(prev_rgb, curr_rgb, 5):
            print(f'Movement detected {capture_count}')
            cv2.imwrite(f'MotionCapture{capture_count}.jpg', frame)
            capture_count += 1
        prev_rgb = curr_rgb

    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()

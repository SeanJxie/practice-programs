import cv2
import time
from PIL import Image, ImageDraw
import os


def draw_data(avg_array, img_size):
    rectWidth = img_size[0] // len(avg_array)

    img = Image.new("RGB", img_size)
    draw = ImageDraw.Draw(img)

    i = 0

    print("Drawing gradient...")
    for x in range(rectWidth // 2, img_size[0], rectWidth):
        botLeftX = x - rectWidth / 2
        botLeftY = img_size[1]
        topRightX = x + rectWidth / 2
        topRightY = 0

        # Fill param takes the bgr values of the average array, rounds
        # them to the nearest integer, and reverses it to rgb
        draw.rectangle((botLeftX, botLeftY, topRightX, topRightY), fill=tuple(reversed([round(e) for e in avg_array[i][:3]])))
        i += 1

    pathName = os.getcwd() + f"//gradient{time.time()}.jpg"
    img.save(pathName)

    return pathName


def get_data():
    captureTime = int(input("Total capture time (seconds): "))  # Seconds
    while not captureTime >= 1:
        print("Capture time must be greater than or equal to 1")
        captureTime = int(input("Total capture time (seconds): "))

    intervalTime = int(input("Interval time between captures (seconds): "))
    while not 1 <= intervalTime <= captureTime:
        print("Interval time must be greater than or equal to one and less than or equal to total capture time")
        intervalTime = int(input("Interval time between captures (seconds): "))

    averages = []
    cam = cv2.VideoCapture(0)

    print("Starting capture...")
    startTime = time.time()

    while time.time() - startTime < captureTime:

        _, frame = cam.read()  # BGR format
        # cv2.imshow("frame", frame)

        # t1 and t2 determine the avg calculation time
        t1 = time.time()
        averages.append(cv2.mean(frame))
        t2 = time.time()

        print(f"Frame processed at {time.time() - startTime} seconds")

        if (t2 - t1) < intervalTime:  # If (t2 - t1) > intervalTime, the given intervalTime, obviously, will not be met.
            time.sleep(intervalTime - (t2 - t1))

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

    return averages


if __name__ == '__main__':
    size = (int(input("Enter output image width: ")), int(input("Enter output image height: ")))

    while not size[0] > 0 and size[1] > 0:
        print("Image dimensions must be greater than 0")
        size = (int(input("Enter output image width: ")), int(input("Enter output image height: ")))

    avg = get_data()
    path = draw_data(avg, size)

    print(f"Done! Image has been saved with path {path}")

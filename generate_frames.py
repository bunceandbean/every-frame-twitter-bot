import cv2
from sys import argv
from sys import exit

filename, frame_offset = argv[1], argv[2]

try:
    vidcap = cv2.VideoCapture(filename)
    frame_offset = int(frame_offset)
except TypeError:
    exit("Argument two incorrect - not an integer")
except:
    exit("Filename incorrect - does not exist")


success,image = vidcap.read()
count = 0
img_tag = 0
while success:
    if count % frame_offset == 0:
        cv2.imwrite("frames/frame%d.jpg" % img_tag, image)
        img_tag += 1
    success,image = vidcap.read()
    count += 1

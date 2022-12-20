# Samuel Teigland
# December 1st, 2022
# The purpose of this program is to write a program in Python that
# uses the camera when compiled.

# install the necessary libraries
import cv2

# take input of the person's name
name = input("Please enter your name: ")

# create the videocapture object
capture = cv2.VideoCapture(0)

while True:
    # read each frame
    success, frame = capture.read()

    # show the output
    cv2.imshow("Frame", frame)

    # if 'c' is pressed then take the picture
    if cv2.waitKey(1) == ord('c'):
        filename = 'faces/'+name+'.jpg'
        cv2.imwrite(filename, frame)
        print("Image Saved- ", filename)

import cv2
import time
cam = cv2.VideoCapture(0)
time.sleep(3)
img_counter = 0
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

###### Timestamp file name
def timestmp():
    return time.strftime('%Y%m%d%H%M%S', time.localtime())

while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        break
    k = cv2.waitKey(1)
    #print(k)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 104:
        # SPACE pressed
        img_name = "/Users/rpmcandrew/home/python/test/run1/heads/heads_{}.jpg".format(timestmp())
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
      
    elif k%256 == 116:
        # SPACE pressed
        img_name = "/Users/rpmcandrew/home/python/test/run1/tails/tails_{}.jpg".format(timestmp())
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
       
    elif k%256 == 115:
        # SPACE pressed
        img_name = "/Users/rpmcandrew/home/python/test/run1/side/side_{}.jpg".format(timestmp())
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
              
cam.release()

cv2.destroyAllWindows()
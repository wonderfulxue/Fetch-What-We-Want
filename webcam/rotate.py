import sys
import time
import serial
from arduino.cam_control import *
from arduino.catch_image import get_position_of_box
from yolov3.yolo import YOLO

port = 'COM3'
ard = serial.Serial(port,9600,timeout=5)
global initial_speed, rotate_degree, rotate_times
initial_speed = -5
rotate_degree = 1
rotate_times = 0

def object_detecting(x_pos, current_pos):
    """检测物体，未检测到前循环旋转"""
    global initial_speed
    if x_pos == -1:
        current_pos = current_pos + initial_speed
        if current_pos < 5:
            initial_speed = -initial_speed
        elif current_pos > 96:
            initial_speed = -initial_speed
        else:
            info = str(6) + ',' + str(current_pos)
            #print(current_pos)
            ard.write(str.encode(info))
        return True, current_pos

    else:
        return False, current_pos

def centroid_detecting(x_pos, current_pos):
    global rotate_times, rotate_degree
    screen_mid = 640 #屏幕中心点

    if abs(x_pos - screen_mid) < 5:
        return True

    elif x_pos > screen_mid:
        current_pos = current_pos - rotate_degree
        info = str(6) + ',' + str(current_pos)
        ard.write(str.encode(info))
    else:
        current_pos = current_pos + rotate_degree
        info = str(6) + ',' + str(current_pos)
        ard.write(str.encode(info))
    return False


def centroid_detecting(x_pos, current_pos):
    global rotate_times, rotate_degree
    screen_mid = 640 #屏幕中心点

    if abs(x_pos - screen_mid) < 5:
        return True, current_pos

    elif x_pos > screen_mid:
        current_pos = current_pos - rotate_degree
        info = str(6) + ',' + str(current_pos)
        ard.write(str.encode(info))
    else:
        current_pos = current_pos + rotate_degree
        info = str(6) + ',' + str(current_pos)
        ard.write(str.encode(info))
    return False, current_pos



if __name__ == '__main__':
    current_position = 96
    cap = cv2.VideoCapture(1)
    count = 0
    yolo = YOLO()
    while(True):
        count += 1
        ret, frame = cap.read()
        # print(count)
        cv2.imshow('frame', frame)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        name = 'images/object.jpg'
        cv2.imwrite(name, frame)
            # break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


        position = get_position_of_box(yolo, 'drug A')
        time.sleep(0.2)
        flag, current_position = object_detecting(position, current_position)

        if not flag:
            stop = False
            while(not stop):
                stop, current_position = centroid_detecting(position, current_position)
                position = get_position_of_box(yolo, 'drug A')
                time.sleep(0.4)
            break

    yolo.close_session()
    cap.release()
    cv2.destroyAllWindows()



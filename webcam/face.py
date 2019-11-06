from PIL import Image, ImageDraw
import cv2
import os
import time
import face_recognition

unknown_pic_path = '/Users/wonderful_xue/Desktop/Robotic-Arm/unknown_pictures'
known_pic_path = '/Users/wonderful_xue/Desktop/Robotic-Arm/known_people'


def get_cam():
    # webcam 的代号是 1 ，电脑自带前置摄像头是 0
    cap = cv2.VideoCapture(0)

    # 设置分辨率
    cap.set(3, 640)
    cap.set(4, 480)

    if cap.isOpened():

        tag = time.ctime()
        pic_name = ''
        while (True):

            # Capture frame-by-frame
            ret, frame = cap.read()

            frame = cv2.putText(frame, 'please enter q to identify your face', (0, 400), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                color=(0, 0, 255))

            cv2.imshow('frame', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                pic_name = 'save' + '.jpg'
                pic_name = os.path.join(unknown_pic_path, pic_name)
                cv2.imwrite(pic_name, frame)
                break

            # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()
        return pic_name
    else:
        raise Exception('reboot the camera')


def myFace_recognition(pic):
    # Load known pictures and learn how to recognize it.
    xue_image = face_recognition.load_image_file(os.path.join(known_pic_path, 'xue.jpg'))
    xue_face_encoding = face_recognition.face_encodings(xue_image)[0]

    zhou_image = face_recognition.load_image_file(os.path.join(known_pic_path, 'zhou.jpg'))
    zhou_face_encoding = face_recognition.face_encodings(zhou_image)[0]

    yao_image = face_recognition.load_image_file(os.path.join(known_pic_path, 'yao.jpg'))
    yao_face_encoding = face_recognition.face_encodings(yao_image)[0]

    known_face_encodings = [
        xue_face_encoding,
        zhou_face_encoding,
        yao_face_encoding
    ]

    known_face_names = [
        'Xue Zhijun',
        "Zhou Liangboya",
        "yao Ruigang"
    ]

    # Load unknown_face
    unknown_image = face_recognition.load_image_file(pic)

    # Find all the faces and face encodings in the unknown image
    unknown_face_locations = face_recognition.face_locations(unknown_image)
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

    pil_image = Image.fromarray(unknown_image)

    draw = ImageDraw.Draw(pil_image)

    (top, right, bottom, left) = unknown_face_locations[0]

    match = face_recognition.compare_faces(known_face_encodings, unknown_encoding, 0.45)

    print(match)
    name = 'Unknown'

    if True in match:
        name_index = match.index(True)
        name = known_face_names[name_index]

    # Draw a box around the face using the Pillow module
    draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

    # Draw a label with a name below the face
    text_width, text_height = draw.textsize(name)

    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
    draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))

    # Remove the drawing library from memory as per the Pillow docs
    del draw

    save = "image_with_boxes.png"
    pil_image.save(save)

    display_img = cv2.imread(save)
    cv2.imshow('show', display_img)
    k = cv2.waitKey(delay=0)
    if k == 27:  # wait for ESC key to exit
        # time.sleep(1)
        cv2.destroyAllWindows()

    return name


#  return drug number relative to name via face_recognition

def matching(name):
    repo = {'Xue Zhijun': 'drug A', "Zhou Liangboya": 'drug B', "yao Ruigang": 'drug C'}

    if name in repo:
        return repo[name]
    else:
        raise Exception('Your name has not been registered')


if __name__ == '__main__':
    pic = '/Users/wonderful_xue/Desktop/Robotic-Arm/try.png'
    # pic = get_cam()
    name = myFace_recognition(pic)
    res = matching(name)

    print(res)
    # cv2.namedWindow('image',cv2.WINDOW_NORMAL)
    # display = cv2.imread("image_with_boxes.png")
    # cv2.imshow('image',display)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

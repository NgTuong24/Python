import cv2
import dlib

# read image
img = cv2.imread("image.jpg")

# resize
img = cv2.resize(img, (600, 500))

# chuyển ảnh sang đen trắng 3D > 2D
gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)

# dlib: AI nhận diện
face_detector = dlib.get_frontal_face_detector()

# load the predictor: -> return mat mui mieng cam
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

#use detector to find face landmarks
faces = face_detector(gray)


for face in faces:
    x1 = face.left() #left Point
    y1 = face.top()  #top point
    x2 = face.right()
    y2 = face.bottom()

    # Vex hinh chu nhat
    cv2.rectangle(img = img, pt1=(x1, y1), pt2=(x2, y2),
                  color=(0, 255, 0), thickness=3)


    # 68 điểm mắt mũi miệng
    face_features = predictor(image=gray, box=face)
    # Loop through all 68 points
    for n in range(0, 68):
        x = face_features.part(n).x
        y = face_features.part(n).y

        # Draw a circle                      bán kính
        cv2.circle(img = img, center=(x, y), radius = 2, color=(0,255,0), thickness=5)

# show image
cv2.imshow(winname="Face Recognition", mat=img)

# wait for a key press to exit
cv2.waitKey(delay=0)

# Close All windows
cv2.destroyAllWindows()
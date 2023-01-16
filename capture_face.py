# 20221214_오후 5시

from libs.FacialExpression import FacialExpressionRecognizer
from libs.Face import FacialLandmarkDetector
import libs.Face as Face
import numpy as np
import cv2

save_file = "./img1.PNG"

# 표정 인식에서 참조할 부분의 인덱스
RIGHT_EYE_INDEX = [463, 362, 382, 398, 384, 381, 385, 380, 386, 374, 387, 373, 388, 390, 466, 249, 263, 359]
LEFT_EYE_INDEX = [130, 33, 246, 7, 161, 163, 160, 144, 159, 145, 158, 153, 157, 154, 173, 155, 133, 243]
LIPS_INDEX = [78, 80, 88, 82, 87, 312, 317, 310, 318, 308]
RIGHT_EYEBROW_INDEX = [285, 336, 295, 296, 334, 282, 283, 293, 276, 300]
LEFT_EYEBROW_INDEX = [55, 52, 53, 46, 70, 63, 105, 66, 107, 65]
BETWEEN_EYEBROW_INDEX = [168, 417, 8, 193, 9]
CHIN_INDEX = [152, 400, 379, 397, 288, 361, 323, 454, 176, 150, 172, 58, 132, 93, 234]
FEATURE_INDEX = RIGHT_EYE_INDEX + LEFT_EYE_INDEX + LIPS_INDEX + RIGHT_EYEBROW_INDEX + LEFT_EYEBROW_INDEX + BETWEEN_EYEBROW_INDEX + CHIN_INDEX


# 감정 출력 함수
def switch(key):
    emotion = {0: "anger", 1: "happiness",
               2: "disgust", 3: "surprise",
               4: "sadness", 5: "neutral"}.get(key, "None")
    print("Emotion :", emotion)


# 정규화 함수
def min_max_normalization(value):
    value = list(value)

    _max = max(value)
    _min = min(value)

    result = []

    for val in value:
        _val = (val - _min) / (_max - _min)
        result.append(_val)

    return np.array(result)


def main():
    face_svm_model = FacialExpressionRecognizer()
    face_svm_model.load("SVM_Model_20221214_1.pkl")

    facial_landmark_detector = FacialLandmarkDetector(
        model=Face.FACIAL_LANDMARK_DETECTION_MODEL_MEDIAPIPE,
        face_detector=Face.FACE_DETECTION_MODEL_OPENCV_DNN)

    face_x = []
    face_y = []
    test = []
    result = []

    # 사진 촬영
    cap = cv2.VideoCapture(0)

    while True:

        _, frame = cap.read()

        frame = cv2.flip(frame, 1)

        if cv2.waitKey(2) & 0xFF == ord('1'):
            cv2.imwrite(save_file, frame)
            print("Capture Complete !")

        facial_landmark_detector.feed(frame)

        cv2.imshow("frame", frame)

        key = cv2.waitKey(1)

        if key == 27:
            break

    cap.release()

    img = cv2.imread(save_file)

    facial_landmark_detector.feed(img)

    if facial_landmark_detector.getIsDetect():

        landmarks = facial_landmark_detector.getFacialLandmark()

        x = landmarks.getX()
        y = landmarks.getY()

        for idx in range(landmarks.size):
            cv2.circle(frame, (int(x[idx]), int(y[idx])), 1, (255, 0, 0), 1)

            face_x.append(x[idx])
            face_y.append(y[idx])

    # 정규화 과정
    normalized_face_x = min_max_normalization(face_x)
    normalized_face_y = min_max_normalization(face_y)

    for i in FEATURE_INDEX:
        test.append(normalized_face_x[i])
        test.append(normalized_face_y[i])

    result.append(test)

    print(np.array(result).shape)

    face_svm_model.feed(result)
    prediction = face_svm_model.getPrediction()

    switch(prediction[0])


if __name__ == '__main__':
    main()
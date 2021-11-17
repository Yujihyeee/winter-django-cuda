import cv2


class MyOpenCV:
    def __init__(self):
        pass

    def execute(self):
        # haarcascade 불러오기
        # - 얼굴과 눈을 찾기위한 미리 학습된 샘플 데이터
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

        # 이미지 불러오기
        # '샘플이미지경로': 얼굴을 검출하고싶은 이미지 경로를 작성해주세요
        img = cv2.imread('C:\\Users\\bitcamp\\Downloads\\sample_image')

        # 이미지 전처리
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # 얼굴 찾기
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # 눈 찾기
            roi_color = img[y:y + h, x:x + w]
            roi_gray = gray[y:y + h, x:x + w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        # 결과 출력
        cv2.imshow('image', img)

        key = cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == '__main__':
    m = MyOpenCV()
    m.execute()

import base64
import hashlib
import cv2

def text(n):
    text_string = n
    encoded_text_string = base64.b64encode(text_string.encode())  #  인코딩
    sha_text = hashlib.sha256(encoded_text_string).hexdigest()  # 인코딩된 text_string 에 sha256 적용
    return sha_text

def image(ph):
    with open(ph, 'rb') as imageFile:  # 이미지 byte 읽기 모드로 오픈
        image_encoding = base64.b64encode(imageFile.read())  # 인코딩
        sha_image = hashlib.sha256(image_encoding).hexdigest()  # sha256 적용
    return sha_image

def video(ph):
    cap3 = cv2.VideoCapture(ph)  # 비디오 캡쳐 객체 생성
    total_frame3 = int(cap3.get(cv2.CAP_PROP_FRAME_COUNT))  # cap3 프레임 수 확인
    count = 1
    info = ''  # 프레임 hash 값을 저장할 string

    while cap3.isOpened():
        ret, frame = cap3.read()
        if ret:
            cv2.imwrite(r'capture_data\%d.jpg' % count, frame)  # 프레임 번호를 이름으로 프레임 jpg 이미지 저장
            with open(r'capture_data\%d.jpg' % count, 'rb') as imageFile:  # 저장된 프레임 이미지 열기
                string = base64.b64encode(imageFile.read())
                info += hashlib.sha256(string).hexdigest()  # 프레임 sha256 적용 후 txt 파일에 저장
            count += 1
        if count >= total_frame3 + 1:
            break
    cap3.release()

    inform = bytes(info.encode())  # info 를 인코딩
    sha_inform = hashlib.sha256(inform).hexdigest()  # inform 에 sha256 적용
    return sha_inform

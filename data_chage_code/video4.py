import hashlib
import base64
import cv2

cap3 = cv2.VideoCapture(r'data\movie\original_data\3sec.mp4')  # 비디오 캡쳐 객체 생성, 3초 영상
total_frame3 = int(cap3.get(cv2.CAP_PROP_FRAME_COUNT))  # cap3 프레임 수 확인
print(total_frame3)
count = 1
info = ''  # 프레임 hash 값을 저장할 string

while cap3.isOpened():
    ret, frame = cap3.read()
    if ret:
        cv2.imwrite(r'data\movie\capture_data\%d.jpg' % count, frame)  # 프레임 번호를 이름으로 프레임 jpg 이미지 저장
        with open(r'data\movie\capture_data\%d.jpg' % count, 'rb') as imageFile:  # 저장된 프레임 이미지 열기
            string = base64.b64encode(imageFile.read())
            info += hashlib.sha256(string).hexdigest()  # 프레임 sha256 적용 후 txt 파일에 저장
        count += 1
    if count >= total_frame3 + 1:
        break
print("finish")
cap3.release()

print(info)
inform = bytes(info.encode())  # info 를 인코딩
print(type(inform), inform)
print(hashlib.sha256(inform).hexdigest())  # inform 에 sha256 적용

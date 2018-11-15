import cv2

cap3 = cv2.VideoCapture(r'data\movie\original_data\3sec.mp4')  # 비디오 캡쳐 객체 생성, 3초 영상
total_frame3 = int(cap3.get(cv2.CAP_PROP_FRAME_COUNT))  # cap3 프레임 수 확인
print(total_frame3)
count = 1

while cap3.isOpened():
    ret, frame = cap3.read()  # cap3 읽기
    if ret:
        cv2.imwrite(r'data\movie\capture_data\%d.jpg' % count, frame)  # 프레임 번호를 이름으로 프레임 jpg 이미지 저장
        count += 1
    if count >= total_frame3 + 1:  # 저장된 프레임 수와 영상의 프레임 수가 같아지면 종료
        break

print("finish")
cap3.release()

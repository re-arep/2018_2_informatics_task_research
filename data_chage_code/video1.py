import cv2

cap3 = cv2.VideoCapture(r'data\movie\original_data\3sec.mp4')  # 비디오 캡쳐 객체 생성, 3초 영상
total_frame3 = int(cap3.get(cv2.CAP_PROP_FRAME_COUNT))  # cap3의 프레임수 확인
print(total_frame3)
cap3.release()  # cap3 닫기

cap5 = cv2.VideoCapture(r'data\movie\original_data\5sec.mp4')  # 5초 영상
total_frame5 = int(cap5.get(cv2.CAP_PROP_FRAME_COUNT))
print(total_frame5)
cap5.release()

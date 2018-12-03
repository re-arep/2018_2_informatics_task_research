import base64
import hashlib

def text(ph):
    with open(ph, 'rb') as textFile:  # 텍스트 byte 읽기 모드로 오픈
        text_encoding = base64.b64encode(textFile.read())  # 인코딩
        sha_text = hashlib.sha256(text_encoding).hexdigest()  # sha256 적용
    return sha_text

def image(ph):
    with open(ph, 'rb') as imageFile:  # 이미지 byte 읽기 모드로 오픈
        image_encoding = base64.b64encode(imageFile.read())  # 인코딩
        sha_image = hashlib.sha256(image_encoding).hexdigest()  # sha256 적용
    return sha_image

def video(ph):
    with open(ph, 'rb') as videoFile:  # 비디오 byte 읽기 모드로 오픈
        video_encoding = base64.b64encode(videoFile.read())  # 인코딩
        sha_video = hashlib.sha256(video_encoding).hexdigest()  # sha256 적용
    return sha_video

def audio(ph):
    with open(ph, 'rb') as audioFile:  # 오디오 byte 읽기 모드로 오픈
        audio_encoding = base64.b64encode(audioFile.read())  # 인코딩
        sha_audio = hashlib.sha256(audio_encoding).hexdigest()  # sha256 적용
    return sha_audio

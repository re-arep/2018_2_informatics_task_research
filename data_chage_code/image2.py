import base64
import hashlib

'''
2test1 : 흑백 이미지
3test1 : RGB 컬러 이미지
2test11 : 디코딩 된 흑백 이미지
3test11 : 디코딩 된 컬러 이미지
'''

with open(r'data\image\2test1.jpg', 'rb') as imageFile:  # jpg 이미지 byte 읽기 모드로 오픈
    string = base64.b64encode(imageFile.read())  # 인코딩
    print(string)
    print(hashlib.sha256(string).hexdigest())  # sha256 적용

with open(r'data\image\3test1.jpg', 'rb') as imageFile:
    string1 = base64.b64encode(imageFile.read())
    print(string1)
    print(hashlib.sha256(string1).hexdigest())

fbw = open(r'data\image\2test11.jpg', 'wb')
fbw.write(base64.b64decode(string))  # 디코딩 후 저장
fbw.close()

fcl = open(r'data\image\3test11.jpg', 'wb')
fcl.write(base64.b64decode(string1))
fcl.close()

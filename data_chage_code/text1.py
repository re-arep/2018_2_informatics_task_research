import base64
import hashlib

print("start english")

en_string = 'a'  # 영어
encoded_en_string = base64.b64encode(en_string.encode())  # en_string 인코딩
sha_en = hashlib.sha256(encoded_en_string).hexdigest()  # 인코딩된 en_string 에 sha256 적용

print(type(en_string), en_string)
print(type(encoded_en_string), encoded_en_string)
print(type(sha_en), sha_en)
print(type(hashlib.sha256(encoded_en_string).hexdigest()))

print(base64.b64decode(encoded_en_string))  # 디코딩
print(str(base64.b64decode(encoded_en_string), encoding='utf-8'))  # utf-8로 디코딩


print("\n"+"start korean")

ko_string = '안'  # 한국어
encoded_ko_string = base64.b64encode(ko_string.encode())  # ko_string 인코딩
sha_ko = hashlib.sha256(encoded_ko_string).hexdigest()  # 인코딩된 ko_string 에 sha256 적용

print(type(ko_string), ko_string)
print(type(encoded_ko_string), encoded_ko_string)
print(type(sha_ko), sha_ko)

print(base64.b64decode(encoded_ko_string))  # 디코딩
print(str(base64.b64decode(encoded_ko_string), encoding='utf-8'))  # utf-8로 디코딩

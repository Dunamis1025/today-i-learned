import hashlib

# ---------------------------------------------------------
# 저장된 아이디와 비밀번호 설정
# ---------------------------------------------------------

stored_username = "admin"

# "password123"을 해시해서 stored_password에 저장
original_password = "password123"                 # 원래 비밀번호
original_password_bytes = original_password.encode()  # 바이트로 변환
stored_hash_object = hashlib.sha256(original_password_bytes)  # 해시 객체 생성
stored_password = stored_hash_object.hexdigest()  # 16진수 문자열로 변환

# 로그인 시도 횟수
login_attempts = 0

# ---------------------------------------------------------
# 로그인 시도 (최대 3번)
# ---------------------------------------------------------
while login_attempts < 3:
    username = input("Enter username: ")
    password = input("Enter password: ")

    # 입력한 비밀번호도 같은 방식으로 해시해야 비교 가능
    password_bytes = password.encode()               # 바이트로 변환
    hash_object = hashlib.sha256(password_bytes)     # 해시 객체 생성
    hashed_password = hash_object.hexdigest()        # 16진수 문자열로 변환

    # 아이디와 비밀번호가 모두 맞는지 확인
    if username == stored_username and hashed_password == stored_password:
        print("Login successful")
        exit()  # 프로그램 종료
    else:
        login_attempts = login_attempts + 1
        print("Login failed")

# ---------------------------------------------------------
# 3번 실패하면 계정 잠금
# ---------------------------------------------------------
if login_attempts == 3:
    print("Account locked")

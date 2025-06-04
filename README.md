

## ✅ 실행 절차 요약 (Windows 기준, Anaconda 사용)
### 0. 아나콘다 설치 
구글 -> anaconda download 검색 -> 검색시 나오는 첫번째 사이트에서 윈도우용 설치
![image](https://github.com/user-attachments/assets/38f58b90-48c0-4740-acfe-0da4f1cbc382)
설치시 위 사진처럼 체크 선택
### 압축해제 후 ksj_page 폴더를 C:/USER/사용자/ 로 이동
C:\Users\pdqov\Downloads\py_Django-main\py_Django-main\ksj_page -> 폴더 이동
### 1. 아나콘다 프롬프트 실행
시작 메뉴 → **Anaconda Prompt** 실행


### 2. 가상환경 생성 및 활성화
conda create -n ll_env python=3.12 \n
conda activate ll_env
### 3. 해당 폴더로 이동
cd 경로\ksj_page
### 4. 장고 설치
conda install django
### 5. 서버 실행
python manage.py runserver
### 6. 웹 접속
http://127.0.0.1:8000

## ✅ 실행 절차 (Windows 기준, Anaconda 사용)

### 1. 아나콘다 설치 
구글 -> anaconda download 검색 -> 검색시 나오는 첫번째 사이트에서 윈도우용 설치
![image](https://github.com/user-attachments/assets/38f58b90-48c0-4740-acfe-0da4f1cbc382)
설치시 위 사진처럼 체크 선택
### 2. 깃퍼브 폴더 설치 및 환경설정
![image](https://github.com/user-attachments/assets/e5eb66e5-1e23-4c7a-bad6-4a316c5626c6)  

기존 폴더 설치하면 C:\Users\pdqov\Downloads\py_Django-main\py_Django-main\ksj_page 으로 설치되는데  
위 경로의 ksj_page를 C:\USER\사용자이름\ 로 이동
### 3. 아나콘다 프롬프트 실행
시작 메뉴 → **Anaconda Prompt** 실행


### 4. 가상환경 생성
conda create -n ll_env python=3.12  
**설치 중 나오는 모든 질문에 y 엔터**  
### 5. 가상환경 활성화
conda activate ll_env  
### 6. 해당 폴더로 이동
cd C:\USER\사용자이름/\ksj_page  
### 7. 장고 설치
conda install django  
**설치 중 나오는 모든 질문에 y 엔터**  
### 8. 서버 실행
python manage.py runserver
### 9. 웹 접속
http://127.0.0.1:8000

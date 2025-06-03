

## ✅ 실행 절차 요약 (Windows 기준, Anaconda 사용)

### 1. 아나콘다 프롬프트 실행
시작 메뉴 → **Anaconda Prompt** 실행


### 2. 가상환경 생성 및 활성화
conda create -n ll_env python=3.12
conda activate ll_env
### 3. 해당 폴더로 이동
cd 경로\ksj_page
### 4. 장고 설치
conda install django
### 5. 서버 실행
python manage.py runserver
### 6. 웹 접속
http://127.0.0.1:8000

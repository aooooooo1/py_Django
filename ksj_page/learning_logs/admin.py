from django.contrib import admin

# 모듈 파일 models.py에서 entry클래스 import
from .models import Topic, Entry

# 관리자페이지에서 모델 Topic 등록
admin.site.register(Topic)

# 관리자페이지에서 모델 Entry 등록
admin.site.register(Entry)

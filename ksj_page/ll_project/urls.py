# ll_project폴더의 urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # admin 도메인 추가
    path("admin/", admin.site.urls),
    # account 도메인 추가
    path("accounts/", include('accounts.urls')),
    # 모든 /하위 페이지 접속시 learning_logs/urls을 참조하겠따.
    path('', include('learning_logs.urls')),

]

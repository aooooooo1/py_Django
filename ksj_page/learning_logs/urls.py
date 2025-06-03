# learning_logs폴더의 urls.py
from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # 기본 페이지
    path('', views.index, name='index'),

    # 토픽 페이지
    path('topics/', views.topics, name='topics'),

    # 토픽 상세 페이지
    path('topic/<int:topic_id>/', views.topic, name='topic'),

    # 새 토픽페이지 만들면
    path('new_topic/', views.new_topic, name='new_topic'),

    # 새 엔트리 추가
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # 엔트리 편집
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
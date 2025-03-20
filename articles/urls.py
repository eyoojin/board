from django.urls import path
from . import views

app_name = 'articles'

# 'articles/' 생략
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),
]
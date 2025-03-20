from django.urls import path
from . import views

# 'articles/' 생략
urlpatterns = [
    path('', views.index)
]
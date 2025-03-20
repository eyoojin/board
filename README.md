# 오늘 목표: 중복 줄이기

## 0. setting

- 가상환경 설정
- .gitignore

## 1. Django

- 프로젝트 생성
    - 프로젝트 이름 = 서비스 이름

- 앱 생성
    - 앱 이름 = 내가 다루고자 하는 모델/데이터의 복수형
    - 장고에게 앱 등록했다고 알려주기

- urls.py
    - Function views -> 지금까지 우리가 url 생성했던 방법
    - Including another URLconf -> 오늘 해볼 방법
- include 함수 사용한 path 설정 
    - `path('articles/', include('articles.urls'))`
    - `from django.urls import include`
    - `articles/urls.py` 생성
- articles/urls.py에서 path 설정
```python
from django.urls import path
from . import views

# 'articles/' 생략
urlpatterns = [
    path('', views.index)
]
```

- `views.py`에서 함수 생성

- `articles/templates/`
- `../templates/`
    - `base.html` 구멍 뚫기
```html
<!-- base.html -->
{% block 변수이름 %}
{% endblock %}

<!-- index.html -->
{% extends 'base.html' %}

{% block 변수이름 %}
<h1>index</h1>
{% endblock %}
```
- 장고에게 알려주기
    - `settings.py`
```python
TEMPLATES = [{'DIRS': [BASE_DIR / 'templates']}]
```
- `models.py`
    - `class Article()`에 들어오는 data field 설정

- migration
    - 번역본 생성 -> 이주
```shell
python manage.py makemigrations
python manage.py migrate
```

- 관리자 페이지에서 Article 모델 관리하기 위한 등록 
    - `admin.py`
```python
from .models import Article
admin.site.register(Article)
```

- 관리자 계정 생성
```shell
python manage.py createsuperuser
```

---세팅---

- `base.html`에 bootstrap 적용
    - table 사용
```html
<!-- 표 -->
<table class="table">
    <!-- table haed -->
    <thead>
        <!-- 가로로 나누기 -->
        <tr>
            <!-- 세로로 나누기 -->
            <th>title</th>
            <th>content</th>
        </tr>
    </thead> 
    
    <!-- table body -->
    <tbody>
        <tr>
            <!-- 세로로 나누기 -->
            <td>temp title</td>
            <td>temp content</td>
        </tr>
    </tbody>
</table>
```

- 전체 게시판 Read all 기능 구현
    - `views.py` -> `Article.objects.all()`
    - 디자인
        - `div.container`
        - `navbar`
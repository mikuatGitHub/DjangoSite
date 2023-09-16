"""blogapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf.urls import include
# 静的メディアファイルを扱うため静的ルーティング
from django.conf.urls.static import static
from django.conf import settings
# 詳細ページのためappフォルダpostsのviewsを呼び出す
from posts import views

# []+の記述は間をあけない
urlpatterns = [
    path('admin/', admin.site.urls),
    # プロジェクトurlからapp「posts」のurl呼び出すため追加
    path('posts/', include('posts.urls')),
    # 変数post_idを定義し、views.post_detail.htmlへ渡す
    # post_detailという名のurlで呼び出せる
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

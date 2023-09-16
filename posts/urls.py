# appのurlからviews呼び出すためのurls.py作成

# 同じ階層のviews.pyを呼び出し
from . import views

from django.urls import path
urlpatterns=[
    path('', views.index, name='index'),
]
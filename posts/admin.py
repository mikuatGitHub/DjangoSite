from django.contrib import admin
# Register your models here.

# 「from .models」=同じ階層のmodels.pyを参照し、クラスPostを読み込む
from .models import Post
# adminページの一覧にクラスPostを登録
admin.site.register(Post)

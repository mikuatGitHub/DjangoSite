# from django.shortcuts import render
# Create your views here.

# objectが存在しなければ404を返す
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# 同じ階層のmodels.pyからクラス定義Postを読み込む
from .models import Post

# このviewが呼び出された時の処理を関数defで定義
def index(request):
    # return HttpResponse("Hello World! このページは投稿のインデックス")

    # クラスPostのobjectを変数へ格納 公開日の降順でソート
    posts= Post.objects.order_by('-published')

    # 外部からtemplateを読み込んでブラウザへrenderする
    # 変数postsも一緒に渡す {'テンプレ内での変数名':渡す変数名}
    return render(request, 'posts/index.html',{'posts': posts})

# プロジェクトフォルダblogappのurls.pyから呼び出された時の処理を関数defを定義
# 引数post_idをviewからtemplateへ渡す
def post_detail(request, post_id):
# DBから取り出したobjectを変数へ格納、pkプライマリーキー
    # post= Post.objects.get(pk=post_id)
# 404エラーを返す
    post= get_object_or_404(Post, pk=post_id)
    # return render(request, 'posts/post_detail.html', {'post_id':post_id})
    return render(request, 'posts/post_detail.html', {'post':post})

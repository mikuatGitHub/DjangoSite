from django.db import models
# Create your models here.

class Post(models.Model):
    title= models.CharField(max_length=100)
    # published投稿日
    published= models.DateTimeField()
    # upload_to imageの保存先を指定
    image= models.ImageField(upload_to='media/')
    body= models.TextField()

    # オブジェクト＝クラスから作成された各データ
    # オブジェクト名にtitle文字列を設定したい 
    def __str__(self):
        return self.title
    
    # bodyから先頭30文字を切り出し
    # template> index.htmlで使用
    def summary(self):
        return self.body[:30]
    

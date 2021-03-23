from django.db import models


# Create your models here.

# python manage.py makemigrations
# 根據檢測到的模型創建新的遷移。遷移的作用，更多的是將數據庫的操作，以文件的形式記錄下來，方便以後檢查、調用、重做等等。
# python manage.py migrate
# 使數據庫狀態與當前模型集和遷移集同步。說白了，就是將對數據庫的更改，主要是數據表設計的更改，在數據庫中真實執行。
# 例如，新建、修改、刪除數據表，新增、修改、刪除某數據表內的字段等等
class Url(models.Model):
    link = models.CharField(max_length=10000)
    uuid = models.CharField(max_length=10)

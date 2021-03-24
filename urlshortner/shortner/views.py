import uuid  # 通用唯一辨識碼（Universally Unique Identifier，縮寫為 UUID）

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Url


# Create your views here.
def index(request):
    return render(request, "index.html")


def create(request):
    if request.method == "POST":
        link = request.POST["link"]
        uid = str(uuid.uuid4())[:5]  # 產生第四版 UUID（隨機）
        new_url = Url(link=link, uuid=uid)
        new_url.save()
        return HttpResponse(uid)


def go(request, pk):
    url_details = Url.objects.get(uuid=pk)  # 取得資料庫中uuid=input pk
    return redirect(url_details.link)  # 返回資料庫中指定object的連結


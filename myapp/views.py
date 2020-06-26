# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from .application import logs

def index(req):
    return render(req, 'index.html')
    # return HttpResponse('Hello World')

# SNS画面を開く
def sns(req):
    return render(req, 'sns.html')

# 検索画面を開く
def search(req):
    return render(req, 'search.html')

# プロフィール画面を開く
def profile(req):
    return render(req, 'profile.html')


# 操作ログの記録(ajaxを使用した時に実行される処理)
def logging(req):
    if req.method == 'GET':
        logs.regist_log(req.GET.get("time"),req.GET.get("user_id"),req.GET.get("about"),req.GET.get("data1"),req.GET.get("data2"))
        print("Success a logging.")
        return HttpResponse()
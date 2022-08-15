from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("<h1>Django Theme URL</h1>"
                        + "<a href='https://github.com/IIBlackCode/HtmlTemplate-DJANGO.git'>Github</a><br>"
                        + "<hr>"
                        + "<h1>LOCAL 퍼블 List</h1>"
                        + "<a href='http://127.0.0.1:8000/theme/XXX1/0001/01'>Local Theme Admin</a><br>"
                        + "<a href='http://127.0.0.1:8000/theme/XX1X/index/x/'>Local Theme Game</a><br>"
                        + "<a href='http://127.0.0.1:8000/theme/XX11/0001/01'>Local Theme Industrious</a><br>"
                        + "<h1>LOCAL WEB</h1>"
                        + "<a href='http://127.0.0.1:8000/BLACKCODE/XXX1/0001/01'>Local Theme Admin</a><br>"
                        + "<a href='http://127.0.0.1:8000/BLACKCODE/XX1X/index/x'>Local Theme Game</a><br>"
                        + "<a href='http://127.0.0.1:8000/BLACKCODE/XX11/0000/XX'>Local Theme Industrious</a><br>"
                        )

import imp
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

from .view.admin        import Theme as AdminTheme
from .view.game         import Theme as GameTheme
from .view.industrious  import Theme as IndustriousTheme

app_name = 'THEME'

urlpatterns = [
    # path('', views.index),
    
    path('XXX1/<menu>/<pages>/',       AdminTheme.url),
    path('XX1X/<menu>/<pages>/',        GameTheme.url),
    path('XX11/<menu>/<pages>/', IndustriousTheme.url),

]

"""gamesapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from games import views

urlpatterns = [
    url(r'^game-categories/$',
        views.GameCategoryList.as_view(),
        name=views.GameCategoryList.name),
    url(r'^game-categories/(?P<pk>[0-9]+)/$',
        views.GameCategoryDetail.as_view(),
        name=views.GameCategoryDetail.name),
    url(r'^games/$',
        views.GameList.as_view(),
        name=views.GameList.name),
    url(r'^games/(?P<pk>[0-9]+)/$',
        views.GameDetail.as_view(),
        name=views.GameDetail.name),
    url(r'^players/$',
        views.PlayerList.as_view(),
        name=views.PlayerList.name),
    url(r'^players/(?P<pk>[0-9]+)/$',
        views.PlayerDetail.as_view(),
        name=views.PlayerDetail.name),
    url(r'^player-scores/$',
        views.PlayerScoreList.as_view(),
        name=views.PlayerScoreList.name),
    url(r'^player-scores/(?P<pk>[0-9]+)/$',
        views.PlayerScoreDetail.as_view(),
        name=views.PlayerScoreDetail.name),
    url(r'^$',
        views.ApiRoot.as_view(),
        name=views.ApiRoot.name),
]

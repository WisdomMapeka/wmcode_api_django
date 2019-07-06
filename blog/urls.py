from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('article_detail/<int:pk>/', views.article_detail, name='article_detail'),
    # api urls
    path('articles/', views.article_list_api),
    path('articles/<int:pk>/', views.article_detail_api),
] 
urlpatterns = format_suffix_patterns(urlpatterns)
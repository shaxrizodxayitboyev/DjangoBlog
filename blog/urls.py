from django.urls import path
from blog import views

urlpatterns = [
    path('', views.home_view, name='home-view'),
    path('create-blog/', views.create, name='create-blog'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('update-blog/', views.update, name='update-blog'),
    path('blog-delete/', views.blog_delete, name='blog-delete'),
    path('search/', views.blog_search, name='blog-search'),
]
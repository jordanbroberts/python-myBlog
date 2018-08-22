from django.urls import path
from . import views



urlpatterns = [
        path('', views.home, name='home'),
	path('blog-index/', views.index, name='blog-index'),
        path('tag/<slug:tag_slug>/', views.index , name='post_list_by_tag'),
      

    ]

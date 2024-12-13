from django.urls import path
from blog.views import post_list_view, post_detail_view, post_create_view

urlpatterns = [
    path("", post_list_view, name = ""),
    path('<int:pk>', post_detail_view, name = 'post_detail'),
    path('blog/create/', post_create_view, name = 'post_create')
]
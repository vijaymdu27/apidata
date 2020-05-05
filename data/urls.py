from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('list_out/', views.list_out, name='list_our'),
    path('id_api/', views.id_api, name='id_api'),
    path('search_api/', views.search_api, name='Search_api'),
    path('userlist/', views.UserListView.as_view()),
]

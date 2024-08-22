from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('create/<int:pk>/', views.comics_create, name='comics_create'),
    path('detail/<int:pk>/', views.comic_detail, name='comics_detail'),
    path('int:pk/add_panel/', views.panel_add, name='panel_add'),
    path('int:pk/edit_panel/int:panel_pk/', views.panel_edit, name='panel_edit'),
    path('int:pk/delete_panel/int:panel_pk/', views.panel_delete, name='panel_delete'),
]

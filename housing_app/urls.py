from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('base/', views.base, name='base'),
    path('profile/<str:pk>',views.houseProfile,name='profile'),
    path('edit/<str:pk>',views.editHouse,name='edit'),
    path('delete/<str:pk>', views.deleteHouse, name='delete'),

]

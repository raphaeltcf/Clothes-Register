from django.contrib import admin
from django.urls import path
from clothes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clothes/', views.IndexView.as_view(), name='index'),
    path('clothes/<int:pk>/', views.ClothesDetailView.as_view(), name='detail'),
    path('clothes/edit/<int:pk>/', views.edit, name='edit'),
    path('clothes/create/', views.create, name='create'),
    path('clothes/delete/<int:pk>/', views.delete, name='delete'),
]
from django.urls import path 

from .views import detail, new, delete, edit, browse

app_name = 'item'

urlpatterns = [
    path('new/', new, name='new'),
    path('<int:pk>/', detail, name='detail'),
    path('<int:pk>/delete/', delete, name='delete'),
    path('<int:pk>/edit/', edit, name='edit'),
    path('browse/', browse, name='browse'),
]
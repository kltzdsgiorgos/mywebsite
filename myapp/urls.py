from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from myapp import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('myapp/', views.ReceiptList.as_view()),
    path('myapp/<int:pk>/', views.ReceiptDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
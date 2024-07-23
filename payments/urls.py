from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('fees/', views.FeeList.as_view()),
    path('fees/<int:pk>/', views.FeeDetail.as_view()),
    path('requests/', views.PaymentRequestList.as_view()),
    path('requests/pending', views.PendingPaymentRequestList.as_view()),
    path('requests/<int:pk>/', views.PaymentRequestDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

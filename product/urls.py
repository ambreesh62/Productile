from django.contrib import admin
from django.urls import path
from product.views import ProductAPIView,CategoryAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from product.filter import ProductFilterView

urlpatterns = [
    path('product/' ,ProductAPIView.as_view()),
    path('product/<int:pk>/' ,ProductAPIView.as_view()),
    path('category/' ,CategoryAPIView.as_view()),
    path('category/<int:pk>/' ,CategoryAPIView.as_view()),
    path('api/token/verify/', TokenVerifyView.as_view()),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('filter/' ,ProductFilterView.as_view()),

]

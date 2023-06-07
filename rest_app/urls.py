from django.urls import path
from . import views

urlpatterns = [
    path('productslist/', views.ProductAPIList.as_view(), name="ProductsList"),
    path('brandlist/', views.BrandAPIList.as_view(), name="BrandList"),

    path('cartlist/', views.CartAPIList.as_view(), name="CartList"),
    path('cartlist/<int:pk>/', views.CartList.as_view(), name="CartList"),


    path('orderlist/<int:pk>/', views.OrderAPIList.as_view(), name="OrderList"),
    path('orderlist/', views.OrderAPIList.as_view(), name="OrderList"),
    path('commentlist/', views.CommentAPIList.as_view(), name="CommentList"),

]
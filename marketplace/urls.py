from django.urls import path
from . import views

urlpatterns = [
    path('', views.marketplace, name='marketplace'),   
    path('<slug:vendor_slug>/', views.vendor_detail, name='vendor_detail'),
       # 添加至购物车
    path('add_to_cart/<int:food_id>/', views.add_to_cart, name='add_to_cart'),
        # 从购物车删除
    path('decrease_cart/<int:food_id>/', views.decrease_cart, name='decrease_cart'),
    # 删除购物车项目
    path('delete_cart/<int:cart_id>/', views.delete_cart, name='delete_cart'),

]
from django.urls import path
from . import views

urlpatterns = [
    path('list',views.index,name = "Product List"),
    path('detail/<int:product_id>',views.detail,name = "Product Detail"),
    path('create',views.create)
]
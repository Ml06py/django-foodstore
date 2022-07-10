from django.urls import path
from .views import HomePageView, FoodSearchView, CartPageView, CartAddView, CartRemoveView, OrderCreateView

app_name = "customer"

urlpatterns =[
    path("", HomePageView.as_view(), name= "home"),
    path("foods/", FoodSearchView.as_view(), name="food-result"),

    path("cart/", CartPageView.as_view(), name="cart-page"),

    path("add-cart/<int:food_id>/", CartAddView.as_view(), name="cart-add"),
    path("remove-cart/<int:food_id>/", CartRemoveView.as_view(), name="cart-remove"),

    path("add-order/", OrderCreateView.as_view(), name="order-create")
]
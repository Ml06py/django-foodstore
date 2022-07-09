from django.views.generic import TemplateView, ListView, View
from django.db.models import Q
from django.shortcuts import redirect, get_object_or_404, render

from restaurant.models import Food, Category

from .cart import Cart

class HomePageView(TemplateView):
    '''
        Home page
    '''
    template_name = "customer/home.html"


class CartPageView(View):
    '''
        Show user orders
    '''

    def get(self, request):
        cart = Cart(request)
        a = request.session.get('cart')
        print(a)
        return render(request, "customer/cart.html", {'cart': cart})

class CartAddView(View):

	def get(self, request, food_id):
		cart = Cart(request)
		food = get_object_or_404(Food, id= food_id)

		if food.is_available:
			cart.add(food, 1)
		return redirect('customer:cart-page')

class CartRemoveView(View):
    def get(self, request, food_id):
        cart = Cart(request)
        food = get_object_or_404(Food, id=food_id)
        cart.remove(food)
        return redirect('customer:cart-page')


class FoodSearchView(ListView):
    '''
        Show result of searched data
    '''
    template_name = "customer/food-list.html"
    context_object_name = "foods"

    def get_queryset(self):
        q = self.request.GET.get('q', None)
        return Food.objects.filter(
            Q(name__icontains=q) | Q(category__title= q)
        ).order_by("-is_available")

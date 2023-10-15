from order.models import Order, OrderItem
from django.contrib.auth.decorators import login_required

def account_base(request):
    if request.user.is_authenticated:
        orders = Order.objects.filter(user=request.user)

        return {'orders': orders}
    
    else:
        nothing = ''
        return {'nothing': nothing}
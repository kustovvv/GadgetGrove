from order.models import Order
from .models import PersonalInformation

def account_base(request):
    if request.user.is_authenticated:
        orders = Order.objects.filter(user=request.user)
        user_phone = ''
        profile_image = ''
        menu = {"account:history":['history', 'History of orders'],
                "item:favorites": ['favorites', 'Favorites'],
                "account:comments": ['comments', 'My comments'],
                "account:ads": ['ads', 'My ads'],
                "conversation:conversations": ['conversations', 'Conversations'],
                "account:card": ['card', 'My card'],
                "account:discounts": ['discounts', 'Discounts and bonuses'],
                "account:settings": ['settings', 'Settings'],
                "account:logout_user": ['', 'Log out'],
                }

        try:
            user_info = PersonalInformation.objects.get(user=request.user)
            user_phone = user_info.phone_number
            profile_image = user_info.avatar
        except:
            user_info = None
        
        return {'orders': orders, 
                'user_phone': user_phone,
                'profile_image': profile_image,
                'menu': menu,
                }
    
    else:
        nothing = ''
        return {'nothing': nothing}
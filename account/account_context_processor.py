from order.models import Order
from .models import PersonalInformation

def account_base(request):
    if request.user.is_authenticated:
        orders = Order.objects.filter(user=request.user)
        user_phone = ''
        profile_image = ''
        try:
            user_info = PersonalInformation.objects.get(user=request.user)
            user_phone = user_info.phone_number
            profile_image = user_info.avatar
        except:
            user_info = None
        

        return {'orders': orders, 
                'user_phone': user_phone,
                'profile_image': profile_image,}
    
    else:
        nothing = ''
        return {'nothing': nothing}
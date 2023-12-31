from django.shortcuts import render, redirect
from django.contrib.auth import logout

from order.models import Order
from item.models import Item
from authentication.models import User
from .models import PersonalInformation
from .forms import InfoForm, FullInfoForm, SettingsDateOfBirthForms
from item.models import Comments
from core.custom_functions import get_seller_info, search_results

from datetime import date, datetime

def history(request):
    if request.user.is_authenticated:
        orders = Order.objects.filter(user=request.user)
        option = 'history'
        query = request.GET.get('query', '')
        if query:
            return search_results(request, query)
        
        context = {'orders': orders,
                   'option': option}

        return render(request, 'account/history_orders.html', context)

    return redirect('login')


def order_details(request, pk):
    if request.user.is_authenticated:
        order = Order.objects.get(id=pk)
        info = get_seller_info(order.seller.id)
        seller_info = info[0]
        seller_additional_info = info[1]

        query = request.GET.get('query', '')
        if query:
            return search_results(request, query)

        context = {'order': order,
                   'seller_info': seller_info,
                   'seller_additional_info': seller_additional_info,
                   }

        return render(request, 'account/order_details.html', context)
    return redirect('login')


def logout_user(request):
    logout(request)

    return redirect('login')


def account_comments(request):
    if request.user.is_authenticated:
        comments = Comments.objects.filter(email=request.user.email)
        option = 'comments'
        query = request.GET.get('query', '')
        if query:
            return search_results(request, query)
        
        context = {'option': option,
                   'comments': comments,
                   }

        return render(request, 'account/account_comments.html', context)
    
    return redirect('login')


def card(request):
    if request.user.is_authenticated:
        query = request.GET.get('query', '')
        if query:
            return search_results(request, query)
         
        option = 'card'
        context = {'option': option}
        return render(request, 'account/account_card.html', context)
    else:
        return redirect('login')
    

def discounts(request):
    if request.user.is_authenticated:
        query = request.GET.get('query', '')
        if query:
            return search_results(request, query)
         
        option = 'discounts'
        context = {'option': option}
        return render(request, 'account/account_discounts.html', context)
    else:
        return redirect('login')
    

def ads(request):
    if request.user.is_authenticated:
        query = request.GET.get('query', '')
        if query:
            return search_results(request, query)
            
        option = 'ads'
        extra_option = request.GET.get('extra_option', 'active')
        items = Item.objects.filter(created_by=request.user)
        input_value = request.GET.get('input', '')
        if extra_option == 'active':
            items = items.filter(availability=True)
        elif extra_option == 'inactive':
            items = items.filter(availability=False)
        
        if input_value:
            items = items.filter(model__icontains=input_value)

        all_categories = set(item.category_brand.category for item in items)
        selected_category = request.GET.get('category', '-1')

        if selected_category:
            if selected_category != '-1':
                items = items.filter(category_brand__category = selected_category)

        context = {'items': items,
                'option': option,
                'extra_option': extra_option,
                'all_categories': all_categories,
                'selected_category': int(selected_category),
                }
        
        return render(request, 'account/account_ads.html', context)
    else:
        return redirect('login')

def settings(request):
    if request.user.is_authenticated:
        option = 'settings'         
        if request.method == 'POST':
            info_form = InfoForm(request.POST)
            full_info_form = FullInfoForm(request.POST, request.FILES)
            date_of_birth_form = SettingsDateOfBirthForms(request.POST)
            
            if full_info_form.is_valid() and date_of_birth_form.is_valid():
                try:
                    user_personal_info = PersonalInformation.objects.get(user=request.user)
                except:
                    user_personal_info = PersonalInformation(user=request.user)
                
                for field_name, field_value in full_info_form.cleaned_data.items():
                    setattr(user_personal_info, field_name, field_value)

                try:
                    user_personal_info.gender = request.POST.getlist('selected_gender')[0]
                except:
                    user_personal_info.gender = None
                user_personal_info.married = True if request.POST.get('is_married', '') else False
                user_personal_info.have_children = True if request.POST.get('have_children', '') else False

                user_fields = ["username", "first_name", "last_name"]
                user = User.objects.get(id=request.user.id)
                for field in user_fields:
                    data = request.POST.get(field)
                    if data:
                        setattr(user, field, data)
                user.save()

                birthday = date_of_birth_form.cleaned_data.get('selected_day')
                birthmonth = date_of_birth_form.cleaned_data.get('selected_month')
                birthyear = date_of_birth_form.cleaned_data.get('selected_year')
                if birthday and birthmonth and birthyear:
                    try:
                        birthday = int(birthday) + 1
                        birthmonth = int(birthmonth) + 1
                        birthyear = datetime.now().year - int(birthyear)

                        user_birthday = date(birthyear, birthmonth, birthday)
                    except ValueError:
                        pass
                else:
                    user_birthday = None

                user_personal_info.birthday = user_birthday
                
                user_personal_info.save()

                return redirect(request.META.get('HTTP_REFERER', 'frontpage'))
            
            return redirect('frontpage')

        else:
            user = User.objects.get(id=request.user.id)
            initial_info = {
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
            }
            initial = dict()
            initial_birhday = dict()
            gender = ''
            married = ''
            have_children = ''

            try:
                user_personal_info = PersonalInformation.objects.get(user=request.user.id)
                
                for field_name in [field.name for field in user_personal_info._meta.get_fields() if not field.is_relation]:
                    initial[field_name] = getattr(user_personal_info, field_name)
            
                gender = user_personal_info.gender
                married = user_personal_info.married
                have_children = user_personal_info.have_children
                
                day = user_personal_info.birthday.day - 1
                month = user_personal_info.birthday.month - 1
                year = datetime.now().year - user_personal_info.birthday.year

                initial_birhday = {
                    'selected_day': day,
                    'selected_month': month,
                    'selected_year': year
                }

            except:
                initial = {}

            info_form = InfoForm(initial=initial_info)
            full_info_form = FullInfoForm(initial=initial)
            date_of_birth_form = SettingsDateOfBirthForms(initial=initial_birhday)
        
        query = request.GET.get('query', '')
        if query:
            return search_results(request, query)
        
        context = {'option': option,
                    'info_form': info_form,
                    'full_info_form': full_info_form,
                    'date_of_birth_form': date_of_birth_form,
                    'gender': gender,
                    'married':married,
                    'have_children':have_children,
                    }
        
        return render(request, 'account/account_settings.html', context)
    
    return redirect('login')


def delete_profile(request):
    pass
from django.shortcuts import render, redirect
from django.contrib.auth import logout

from order.models import Order
from item.models import Item
from .models import PersonalInformation
from .forms import FullInfoForm, SettingsDateOfBirthForms
from item.views import search_results
from item.models import CategoryBrand, Category, Comments

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
        query = request.GET.get('query', '')
        if query:
            return search_results(request, query)

        return render(request, 'account/order_details.html', {'order': order})
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
    option = 'card'
    context = {'option': option}
    return render(request, 'account/account_card.html', context)


def discounts(request):
    option = 'discounts'
    context = {'option': option}
    return render(request, 'account/account_discounts.html', context)

def ads(request):
    option = 'ads'        
    items = Item.objects.filter(created_by=request.user)
    context = {'items': items,
               'option': option,}
    return render(request, 'account/account_ads.html', context)


def settings(request):
    if request.user.is_authenticated:
        option = 'settings'
        if request.method == 'POST':
            full_info_form = FullInfoForm(request.POST, request.FILES)
            date_of_birth_forms = SettingsDateOfBirthForms(request.POST)            

            if full_info_form.is_valid() and date_of_birth_forms.is_valid():
                try:
                    user_personal_info = PersonalInformation.objects.filter(user_id=request.user)[0]
                    
                    for field_name, field_value in full_info_form.cleaned_data.items():
                        setattr(user_personal_info, field_name, field_value)

                    try:
                        gender = request.POST.getlist('selected_gender')[0]
                        user_personal_info.gender = gender
                    
                    except:
                        user_personal_info.gender = ''

                    setattr(user_personal_info, 'avatar', full_info_form.cleaned_data['avatar'])
                    
                    user_personal_info.married = request.POST.get('is_married', '')
                    
                    user_personal_info.have_children = request.POST.get('have_children', '')

                    
                except:
                    user_personal_info = PersonalInformation(
                        user = request.user,
                        nickname = full_info_form.cleaned_data.get('nickname', None),
                        first_name = full_info_form.cleaned_data.get('first_name', None),
                        last_name = full_info_form.cleaned_data.get('last_name', None),
                        avatar = full_info_form.cleaned_data.get('avatar', None),
                        married = request.POST.get('is_married', ''),
                        have_children = request.POST.get('have_children', ''),
                        phone_number = full_info_form.cleaned_data.get('phone_number', None),
                        facebook = full_info_form.cleaned_data.get('facebook', None),
                        instagram = full_info_form.cleaned_data.get('instagram', None),
                        twitter = full_info_form.cleaned_data.get('twitter', None),
                        google = full_info_form.cleaned_data.get('google', None),
                        pinterest = full_info_form.cleaned_data.get('pinterest', None),
                        about = full_info_form.cleaned_data.get('about', None),
                        hobby = full_info_form.cleaned_data.get('hobby', None),
                        interests = full_info_form.cleaned_data.get('interests', None)
                    )
                
                    selected_genders = request.POST.getlist('selected_gender')
                    gender = selected_genders[0] if selected_genders else ""
                    user_personal_info.gender = gender

                birthday = date_of_birth_forms.cleaned_data.get('selected_day')
                birthmonth = date_of_birth_forms.cleaned_data.get('selected_month')
                birthyear = date_of_birth_forms.cleaned_data.get('selected_year')

                
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
            initial = dict()
            initial_birhday = dict()
            gender = ''
            married = ''
            have_children = ''

            try:
                user_personal_info = PersonalInformation.objects.filter(user=request.user)[0]
                
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
                initial = {'nickname': request.user.username,
                        'first_name': request.user.first_name,
                        'last_name': request.user.last_name,
                        }

            full_info_form = FullInfoForm(initial=initial)
            date_of_birth_forms = SettingsDateOfBirthForms(initial=initial_birhday)
        
        query = request.GET.get('query', '')
        if query:
            return search_results(request, query)
        
        context = {'option': option,
                    'full_info_form': full_info_form,
                    'date_of_birth_forms': date_of_birth_forms,
                    'gender': gender,
                    'married':married,
                    'have_children':have_children,
                    }
        
        return render(request, 'account/account_settings.html', context)
    
    return redirect('login')


def delete_profile(request):
    pass
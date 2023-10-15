from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from order.models import Order
from .models import PersonalInformation
from .forms import FullInfoForm, SettingsImageForm, SettingsSocialProfilesForm, SettingsAdditionalInfoForm, SettingsPhoneForm, SettingsDateOfBirthForms

@login_required
def history(request):
    orders = Order.objects.filter(user=request.user)
    option = 'history'

    return render(request, 'account/history_orders.html', {'orders': orders,
                                                           'option': option})

@login_required
def order_details(request, pk):
    order = Order.objects.get(id=pk)

    return render(request, 'account/order_details.html', {'order': order,
                                                          })

@login_required
def logout_user(request):
    logout(request)

    return redirect('frontpage')


@login_required
def favorites(request):
    option = 'favorites'

    return render(request, 'account/account_favorites.html', {'option': option})


@login_required
def settings(request):
    option = 'settings'
    if request.method == 'POST':
        full_name_form = FullInfoForm(request.POST)
        avatar_form = SettingsImageForm(request.POST)
        phone_form = SettingsPhoneForm(request.POST)
        date_of_birth_forms = SettingsDateOfBirthForms(request.POST)
        social_profiles_form = SettingsSocialProfilesForm(request.POST)
        additional_info_form = SettingsAdditionalInfoForm(request.POST)

        if full_name_form.is_valid() and avatar_form.is_valid() and phone_form.is_valid() and social_profiles_form.is_valid() and additional_info_form.is_valid():
            try:
                user_personal_info = PersonalInformation.objects.get(user=request.user)
                
                if full_name_form.cleaned_data['nickname']:
                    user_personal_info.nickname = full_name_form.cleaned_data['nickname']
                
                if full_name_form.cleaned_data['first_name']:
                    user_personal_info.first_name = full_name_form.cleaned_data['first_name']
                
                if full_name_form.cleaned_data['last_name']:
                    user_personal_info.last_name = full_name_form.cleaned_data['last_name']
                
                if avatar_form.cleaned_data['avatar']:
                    user_personal_info.avatar = avatar_form.cleaned_data['avatar']
                
                if request.POST.getlist('selected_gender')[0]:
                    user_personal_info.gender = request.POST.getlist('selected_gender')[0]
                
                if request.POST.get('is_married', ''):
                    user_personal_info.married = request.POST.get('is_married', '')
                
                if request.POST.get('have_children', ''):
                    user_personal_info.have_children = request.POST.get('have_children', '')
                
                if date_of_birth_forms.cleaned_data['selected_day']:
                    user_personal_info.birthday = date_of_birth_forms.cleaned_data['selected_day']
                
                if date_of_birth_forms.cleaned_data['selected_month']:
                    user_personal_info.birthmonth = date_of_birth_forms.cleaned_data['selected_month']
                
                if date_of_birth_forms.cleaned_data['selected_year']:
                    user_personal_info.birthyear = date_of_birth_forms.cleaned_data['selected_year']

                if phone_form.changed_data['phone_number']:
                    user_personal_info.phone_number = phone_form.changed_data['phone_number']
                
                if social_profiles_form.cleaned_data['facebook']:
                    user_personal_info.facebook = social_profiles_form.cleaned_data['facebook']
                
                if social_profiles_form.cleaned_data['instagram']:
                    user_personal_info.instagram = social_profiles_form.cleaned_data['instagram']

                if social_profiles_form.cleaned_data['twitter']:
                    user_personal_info.twitter = social_profiles_form.cleaned_data['twitter']

                if social_profiles_form.cleaned_data['google']:
                    user_personal_info.google = social_profiles_form.cleaned_data['google']

                if social_profiles_form.cleaned_data['pinterest']:
                    user_personal_info.pinterest = social_profiles_form.cleaned_data['pinterest']

                if additional_info_form.cleaned_data['about']:
                    user_personal_info.about = additional_info_form.cleaned_data['about']
                
                if additional_info_form.cleaned_data['hobby']:
                    user_personal_info.hobby = additional_info_form.cleaned_data['hobby']
                
                if additional_info_form.cleaned_data['interests']:
                    user_personal_info.interests = additional_info_form.cleaned_data['interests']

            except:
                user_personal_info = PersonalInformation(
                    user = request.user,
                    nickname = full_name_form.cleaned_data['nickname'],
                    first_name = full_name_form.cleaned_data['first_name'],
                    last_name = full_name_form.cleaned_data['last_name'],
                    avatar = avatar_form.cleaned_data['avatar'],
                    gender = request.POST.getlist('selected_gender')[0],
                    married = request.POST.get('is_married', ''),
                    have_children = request.POST.get('have_children', ''),
                    birthday = date_of_birth_forms.cleaned_data['selected_day'],
                    birthmonth = date_of_birth_forms.cleaned_data['selected_month'],
                    birthyear = date_of_birth_forms.cleaned_data['selected_year'],
                    phone_number = phone_form.changed_data['phone_number'],
                    facebook = social_profiles_form.cleaned_data['facebook'],
                    instagram = social_profiles_form.cleaned_data['instagram'],
                    twitter = social_profiles_form.cleaned_data['twitter'],
                    google = social_profiles_form.cleaned_data['google'],
                    pinterest = social_profiles_form.cleaned_data['pinterest'],
                    about = additional_info_form.cleaned_data['about'],
                    hobby = additional_info_form.cleaned_data['hobby'],
                    interests = additional_info_form.cleaned_data['interests'],
                )
            
            user_personal_info.save()

        return redirect(request.META.get('HTTP_REFERER', 'frontpage'))

    else:
        full_name_form = FullInfoForm(initial={'nickname': request.user.username,
                                               'first_name': request.user.first_name,
                                               'last_name': request.user.last_name,
                                               })
        avatar_form = SettingsImageForm()
        date_of_birth_forms = SettingsDateOfBirthForms()
        phone_form = SettingsPhoneForm()
        social_profiles_form = SettingsSocialProfilesForm()
        additional_info_form = SettingsAdditionalInfoForm()

    return render(request, 'account/account_settings.html', {'option': option,
                                                             'full_name_form': full_name_form,
                                                             'avatar_form': avatar_form,
                                                             'date_of_birth_forms': date_of_birth_forms,
                                                             'social_profiles_form': social_profiles_form,
                                                             'additional_info_form': additional_info_form,
                                                             'phone_form': phone_form})
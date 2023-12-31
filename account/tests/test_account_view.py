import pytest
from django.urls import reverse

from datetime import datetime

from account.models import PersonalInformation
from authentication.models import User

@pytest.mark.test_account_view
def test_account_view_history(db, client_user, order_factory):
    client, user = client_user
    orders = [order_factory.create(user=user) for _ in range(4)]
    url = reverse('account:history')
    response = client.get(url)

    assert response.status_code == 200
    assert len(response.context['orders']) == len(orders)


@pytest.mark.test_account_view
def test_account_view_order_details(db, client, custom_user_factory, personal_information_factory, order_factory):
    seller = custom_user_factory.create()
    personal_information_factory.create(user=seller)

    order = order_factory.create(seller=seller)

    url = reverse('account:order_details', args=[order.id])
    response = client.get(url)

    assert response.status_code == 200
    assert response.context['order'] == order
    assert response.context['seller_info'] is not None
    assert response.context['seller_additional_info'] is not None


@pytest.mark.test_account_view
def test_account_view_account_comments(db, client_user, comment_factory):
    client, user = client_user
    comments = [comment_factory.create(email=user.email) for _ in range(4)]

    url = reverse('account:comments')
    response = client.get(url)

    assert response.status_code == 200
    assert len(response.context['comments']) == len(comments)


@pytest.mark.test_account_view
def test_account_view_card(db, client):
    url = reverse('account:card')
    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.test_account_view
def test_account_view_discount(db, client):
    url = reverse('account:discounts')
    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.test_account_view
def test_account_view_ads(db, client_user, item_factory, category_brand_factory):
    client, user = client_user
    for _ in range(4):
        item_factory.create(created_by=user)
    
    category_brand = category_brand_factory.create()
    for _ in range(3):
        item_factory.create(created_by=user, category_brand=category_brand)

    item_factory.create(created_by=user, availability=False)

    extra_option = 'active'
    data = {'extra_option': extra_option,}
    url = reverse('account:ads')
    response = client.get(url, data)

    assert response.status_code == 200
    assert len(response.context['items']) == 7
    assert len(response.context['all_categories']) == 5
    assert response.context['selected_category'] == -1

    data['category'] = category_brand.category.id
    response = client.get(url, data)

    assert response.status_code == 200
    assert len(response.context['items']) == 3
    assert response.context['selected_category'] == category_brand.category.id

    extra_option = 'inactive'
    data = {'extra_option': extra_option,}
    response = client.get(url, data)

    assert response.status_code == 200
    assert len(response.context['items']) == 1


@pytest.mark.test_account_view
def test_account_view_settings(db, client_user): 
    client, user = client_user

    url = reverse('account:settings')
    response = client.get(url)

    assert response.status_code == 200
    assert response.context["info_form"].initial['first_name'] == user.first_name
    assert response.context["info_form"].initial['last_name'] == user.last_name
    assert response.context["info_form"].initial['username'] == user.username
    assert response.context["married"] == ''
    assert response.context["have_children"] == ''
    assert response.context["gender"] == ''


@pytest.mark.test_account_view
def test_account_view_settins_GET(db, client_user, personal_information_factory):
    client, user = client_user
    personal_information = personal_information_factory.create(user=user)
    url = reverse('account:settings')
    response = client.get(url)

    assert response.status_code == 200
    info_form = ["first_name", "last_name", "username"]
    for info_filed in info_form:
        assert response.context["info_form"].initial[info_filed] == getattr(user, info_filed)

    full_info = ["avatar_url", "phone_number", "facebook_url", "instagram_url", "twitter_url", "google_url", "pinterest_url", "about", "hobby", "interests"]
    for full_field in full_info:
        assert response.context['full_info_form'].initial[full_field] == getattr(personal_information, full_field)

    additional_info = ["married", "have_children", "gender"]
    for additional_field in additional_info:
        assert response.context[additional_field] == getattr(personal_information, additional_field)

    date_of_birth_info = ["selected_day", "selected_month", "selected_year"]
    numbers = list()
    for birth_field in date_of_birth_info:
        numbers.append(response.context['date_of_birth_form'].initial[birth_field])
    date = datetime(2023-numbers[2], numbers[1]+1, numbers[0]+1)
    assert date.date().strftime('%Y-%m-%d') == personal_information.birthday


@pytest.mark.test_account_view
@pytest.mark.parametrize(
    "username, first_name, last_name, avatar_url, phone_number, have_children, married, gender, facebook_url, instagram_url, twitter_url, google_url, pinterest_url, about, hobby, interests, day_of_birth, month_of_birth, year_of_birth",
    [
        ("user1", "John1", "Doe1", "avatar.jpg", "1234567890", True, False, "male", "https://facebook.com/johndoe", "https://instagram.com/johndoe", "https://twitter.com/johndoe", "https://plus.google.com/johndoe", "https://pinterest.com/johndoe", "I'm a software engineer with a passion for technology.", "Playing guitar", "Reading, coding, hiking", "15", "5", "1990"),
        ("user2", "John2", "Doe2", "", "", "", "", "female", "", "", "", "", "", "", "", "", "15", "5", "1990"),
    ]
)
def test_account_view_settings_POST(db, 
                               client_user, 
                               username, 
                               first_name, 
                               last_name, 
                               avatar_url, 
                               phone_number, 
                               have_children, 
                               married, 
                               gender, 
                               facebook_url, 
                               instagram_url, 
                               twitter_url, 
                               google_url, 
                               pinterest_url, 
                               about, 
                               hobby, 
                               interests, 
                               day_of_birth, 
                               month_of_birth, 
                               year_of_birth):
    client, user = client_user
    info_form_data = {
        'username': username,
        'first_name': first_name,
        'last_name': last_name,
    }
    full_info_form_data = {
        "avatar_url": avatar_url, 
        "phone_number": phone_number, 
        "facebook_url": facebook_url, 
        "instagram_url": instagram_url, 
        "twitter_url": twitter_url, 
        "google_url": google_url, 
        "pinterest_url": pinterest_url, 
        "about": about, 
        "hobby": hobby, 
        "interests": interests,
    }
    date_of_birth_form_data = {
        "selected_day": str(int(day_of_birth)-1),
        "selected_month": str(int(month_of_birth)-1),
        "selected_year": str(datetime.now().year-int(year_of_birth)),
    }
    additional_post_data = {
        'is_married': married,
        'have_children': have_children,
        'selected_gender': gender,
    }

    data = {**info_form_data, **full_info_form_data, **date_of_birth_form_data, **additional_post_data}

    url = reverse('account:settings')
    response = client.post(url, data, follow=True)

    assert response.status_code == 200
    assert PersonalInformation.objects.get(user=user)
    
    user = User.objects.get(id=user.id)
    assert user.username == username
    assert user.first_name == first_name
    assert user.last_name == last_name

    personal_info = PersonalInformation.objects.get(user=user)
    full_info_fields = ["phone_number", "facebook_url", "instagram_url", "twitter_url", "google_url", "pi1nterest_url"]
    for field in full_info_fields:
        if full_info_form_data[field]:
            assert getattr(personal_info, field) == full_info_form_data[field]
        else:
            assert getattr(personal_info, field) == None

    full_info_fields = ["about", "hobby", "interests"]
    for field in full_info_fields:
        assert getattr(personal_info, field) == full_info_form_data[field]

    if gender:
        assert personal_info.gender == gender
    if married:
        assert personal_info.married == married
    if have_children:
        assert personal_info.have_children == have_children

    date = datetime(int(year_of_birth), int(month_of_birth), int(day_of_birth))
    assert date.date() == personal_info.birthday

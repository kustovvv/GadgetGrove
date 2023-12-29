import pytest
from django.db import IntegrityError
from django.contrib.auth.models import User

from authentication.models import User as CustomUser

@pytest.fixture
def new_user_factory(db):
    def create_app_user(
            username: str,
            password: str = None,
            first_name: str = "firstname",
            last_name: str = "lastname",
            email: str = "test@test.com",
            is_staff: str = False,
            is_superuser: str = False,
            is_active: str = True,
            is_email_verified: str = False
    ):
        user = CustomUser.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
            is_email_verified=is_email_verified,
        )
        return user
    return create_app_user


def test_create_user(db, new_user_factory):
    """
    Test creating a User instance
    """
    user = new_user_factory("Test_user", "password", "MyName")

    count = CustomUser.objects.all().count()

    assert user.username is not None
    assert user.first_name is not None
    assert user.is_email_verified is False
    assert user.check_password("password")
    assert count == True


@pytest.mark.test_account_db
def test_create_user2(db, custom_user_factory):
    """
    Test creating a User instance
    """
    user = custom_user_factory.create()
    count = CustomUser.objects.all().count()

    assert user.username is not None
    assert user.email is not None
    assert user.is_email_verified is False
    assert user.check_password('password')
    assert count == True


@pytest.mark.test_account_db
@pytest.mark.parametrize(
    "avatar_url, gender, married, have_children, birthday, phone_number, facebook_url, instagram_url, twitter_url, google_url, pinterest_url, about, hobby, interests",
    [
        ("avatar_123.jpg", "female", False, True, "1987-05-12", "1234567890", "facebook.com/ariathompson", "instagram.com/sunnydaze87", "twitter.com/sunny_aria", "plus.google.com/ariathompson", "pinterest.com/sunnydaze", "Adventure seeker with a love for photography.", "Hiking, photography, reading", "Hiking, photography, reading"),
        ("avatar_tech.jpg", "male", True, False, "1990-09-28", "9876543210", "facebook.com/maxtechwizard", "instagram.com/tech_max", "twitter.com/tech_wizard", "plus.google.com/maxjohnson", "pinterest.com/techwizard", "Software engineer passionate about innovation.", "Coding, robotics, sci-fi movies", "Coding, robotics, sci-fi movies"),
        ("avatar_nature.jpg", "female", False, False, "1985-03-17", "5551234567", "facebook.com/evasmith_nature", "instagram.com/nature_eva", "twitter.com/natureexplorer", "plus.google.com/evasmith_nature", "pinterest.com/naturelover_eva", "Ecologist fascinated by biodiversity and conservation.", "Birdwatching, hiking, environmental advocacy", "Birdwatching, hiking, environmental advocacy"),
    ]
)
def test_account_db_personal_information_insert_data(db, 
                                                     personal_information_factory, 
                                                     avatar_url, 
                                                     gender, 
                                                     married, 
                                                     have_children, 
                                                     birthday, 
                                                     phone_number, 
                                                     facebook_url, 
                                                     instagram_url, 
                                                     twitter_url, 
                                                     google_url, 
                                                     pinterest_url, 
                                                     about, 
                                                     hobby, 
                                                     interests):
    """
    Test inserting a data into personal_information model
    """
    new_personal_info = personal_information_factory.create(avatar_url=avatar_url, 
                                                            gender=gender, 
                                                            married=married, 
                                                            have_children=have_children, 
                                                            birthday=birthday, 
                                                            phone_number=phone_number, 
                                                            facebook_url=facebook_url, 
                                                            instagram_url=instagram_url, 
                                                            twitter_url=twitter_url, 
                                                            google_url=google_url, 
                                                            pinterest_url=pinterest_url, 
                                                            about=about, 
                                                            hobby=hobby, 
                                                            interests=interests)
    
    assert new_personal_info.user is not None 
    assert new_personal_info.avatar_url == avatar_url
    assert new_personal_info.gender == gender
    assert new_personal_info.married == married
    assert new_personal_info.have_children == have_children
    assert new_personal_info.birthday == birthday
    assert new_personal_info.phone_number == phone_number
    assert new_personal_info.facebook_url == facebook_url
    assert new_personal_info.instagram_url == instagram_url
    assert new_personal_info.twitter_url == twitter_url
    assert new_personal_info.google_url == google_url
    assert new_personal_info.pinterest_url == pinterest_url
    assert new_personal_info.about == about
    assert new_personal_info.hobby == hobby
    assert new_personal_info.interests == interests
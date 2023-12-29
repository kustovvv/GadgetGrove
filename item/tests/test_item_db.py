import pytest
from django.db import IntegrityError

@pytest.mark.test_item_db
@pytest.mark.parametrize(
        "name, validity", 
        [
            ("category1", True),
            ("category2", True),
            ("category3", True),
        ]
)
def test_item_db_category_insert_data(db, category_factory, name, validity):
    """
    Test inserting a data into category model
    """
    result = category_factory.create(name=name)

    assert result.name == name


@pytest.mark.test_item_db
def test_item_db_category_uniqueness_integrity(db, category_factory):
    """
    Test the uniqueness integrity on category 
    """
    category = category_factory.create()
    with pytest.raises(IntegrityError):
        category_factory.create(name=category.name)


@pytest.mark.test_item_db
@pytest.mark.parametrize(
    "name, validity",
    [
        ("brand1", True),
        ("brand2", True),
        ("brand3", True),
    ]
)
def test_item_bd_brand_insert_data(db, brand_factory, name, validity):
    """
    Test inserting a data into brand model
    """
    result = brand_factory.create(name=name)

    assert result.name == name


@pytest.mark.test_item_db
def test_item_db_brand_uniqueness_integrity(db, brand_factory):
    """
    Test the uniqueness integrity on brand 
    """
    brand = brand_factory.create()
    with pytest.raises(IntegrityError):
        brand_factory.create(name=brand.name)


@pytest.mark.test_item_db
def test_create_category_brand(db, category_factory, brand_factory, category_brand_factory):
    """
    Test creating a category_brand instance
    """
    category = category_factory.create()
    brand = brand_factory.create()
    category_brand = category_brand_factory.create(category=category, brand=brand)

    assert category_brand.category == category
    assert category_brand.brand == brand
    assert str(category_brand) == f"{category.name} {brand.name}"


@pytest.mark.test_item_db
def test_item_db_category_brand_uniqueness_integrity(db, category_brand_factory):
    """
    Test the uniqueness integrity on category and brand
    """
    category_brand = category_brand_factory.create()
    with pytest.raises(IntegrityError):
        category_brand_factory.create(category=category_brand.category, brand=category_brand.brand)


@pytest.mark.test_item_db
@pytest.mark.parametrize(
    "category_name, brand_name, model, description, price, availability, image_url",
    [
        ("Electronics", "TechZone", "X9000", "Smartphone with advanced features and sleek design.", 799.99, True, "phone_x9000.jpg"),
        ("Fashion", "StyleMasters", "ElegancePro", "Classic black dress perfect for any formal occasion.", 129.99, True, "dress_elegancepro.jpg"),
        ("Home & Living", "CozyNest", "DreamComfort", "Premium memory foam mattress for a restful sleep experience.", 899.99, True, "mattress_dreamcomfort.jpg"),
    ]
)
def test_item_db_item_insert_data(db, item_factory, category_name, brand_name, model, description, price, availability, image_url):
    """
    Test inserting a data into item model
    """
    new_item = item_factory.create(category_brand__category__name=category_name, 
                                   category_brand__brand__name=brand_name, 
                                   model=model, 
                                   description=description,
                                   price=price,
                                   availability=availability,
                                   image_url=image_url,
                                   )

    assert new_item.created_by is not None
    assert new_item.created_at is not None
    assert new_item.model == model
    assert new_item.category_brand.category.name == category_name
    assert new_item.category_brand.brand.name == brand_name
    assert new_item.description == description
    assert new_item.price == price
    assert new_item.availability == availability
    assert new_item.image_url == image_url


@pytest.mark.test_item_db
def test_item_db_item_uniqueness_integrity(db, item_factory):
    """
    Test the uniqueness integrity on item
    """
    category_name = "new_category"
    brand_name = "new_brand"
    new_item = item_factory.create(category_brand__category__name=category_name, category_brand__brand__name=brand_name)
    with pytest.raises(IntegrityError):
        item_factory.create(category_brand__category__name=category_name, category_brand__brand__name=brand_name)


@pytest.mark.test_item_db
def test_item_db_create_comment(db, comment_factory):
    """
    Test create a comment instance
    """
    new_comment = comment_factory.create()
    assert new_comment.first_name is not None
    assert new_comment.last_name is not None


@pytest.mark.test_item_db
def test_item_db_comment_insert_data(db, comment_factory):
    """
    Test inserting a data into comment model
    """
    advantages = "new_advantages"
    disadvantages = "new_disadvantages"
    rating_1 = 5
    new_full_comment = comment_factory.create(advantages=advantages, disadvantages=disadvantages, rating=rating_1)

    assert new_full_comment.item.category_brand.category is not None
    assert new_full_comment.rating == rating_1
    assert new_full_comment.first_name is not None
    assert new_full_comment.last_name is not None
    assert new_full_comment.email is not None
    assert new_full_comment.comment is not None
    assert new_full_comment.advantages == advantages
    assert new_full_comment.disadvantages == disadvantages
    assert new_full_comment.comment_date is not None


@pytest.mark.test_item_db
def test_item_db_favorite_compare_insert_data(db, favorite_compare_factory):
    """
    Test inserting a data into favorite_compare model
    """
    new_favorite_compare = favorite_compare_factory.create()

    for item in new_favorite_compare.favorite_items.all():
        assert item.item.category_brand.category is not None
        assert item.item.category_brand.band is not None

    for item in new_favorite_compare.compare_items.all():
        assert item.item.category_brand.category is not None
        assert item.item.category_brand.band is not None
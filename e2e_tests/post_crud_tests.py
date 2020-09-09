import pytest
import allure
from api_helpers import posts


@allure.description("User should be able to create and delete a post")
def test_create_and_delete_posts():
    posts.get_posts()

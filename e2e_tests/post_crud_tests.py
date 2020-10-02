import pytest
import allure
from actions import post_actions as post
from faker import Faker

fake = Faker()


@allure.description("User should be able to get all posts")
def test_get_all_posts():
    result = post.get_posts()
    assert result.status_code == 200
    assert result.json()[0]["userId"] is not None
    assert result.json()[0]["id"] is not None
    assert result.json()[0]["title"] is not None
    assert result.json()[0]["body"] is not None


@allure.description("User should be able to create and delete posts")
def test_create_and_delete_posts():
    user_id = 1
    post_title = fake.name()
    post_body = fake.sentence()

    # Create a new post
    result = post.create_posts(post_title, post_body, user_id)
    assert result.status_code == 201
    post_id = result.json()["id"]
    assert post_id is not None

    # Delete the created post
    result = post.delete_post(post_id)
    assert result.status_code == 200

import allure
import json
from actions import base_actions
import requests
from faker import Faker

fake = Faker()


@allure.step("Get all posts")
def get_posts(client=requests, **kwargs):
    return base_actions.get(client, "posts", **kwargs)


@allure.step("Create posts")
def create_posts(title, post_body, user_id, client=requests, **kwargs):
    body = f"""{{"title": "{title}", "body": "{post_body}", "userId": {user_id}}}"""
    return base_actions.post(client, "posts/", data=body)


@allure.step("Get a post")
def get_post(post_id, client=requests, **kwargs):
    return base_actions.get(client, "posts/" + str(post_id))


@allure.step("Delete a post")
def delete_post(post_id, client=requests, **kwargs):
    return base_actions.delete(client, "posts/" + str(post_id))

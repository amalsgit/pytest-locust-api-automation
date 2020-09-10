import allure
from api_helpers import api_base
import requests


@allure.step("Get all posts")
def get_posts(client=requests, **kwargs):
    return api_base.get(client, "posts", **kwargs)

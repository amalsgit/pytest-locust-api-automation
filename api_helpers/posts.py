import allure
from api_helpers import api_base
import requests


@allure.step("Get all posts")
def get_posts():
    return requests.get(api_base.host_url + "/posts")
